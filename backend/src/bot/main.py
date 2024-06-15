import asyncio
import json
import os
import re

from aiotraq import AuthenticatedClient
from aiotraq_bot import TraqHttpBot
from aiotraq_bot.models.event import MessageCreatedPayload, BotMessageStampsUpdatedPayload
from aiotraq_message import TraqMessage, TraqMessageManager
from fastapi.encoders import jsonable_encoder

from aiotraq.api.message import get_message


base_url = "https://q.trap.jp/api/v3"
bot_verification_token = os.getenv("BOT_VERIFICATION_TOKEN", "")
bot_access_token = os.getenv("BOT_ACCESS_TOKEN", "")

bot = TraqHttpBot(verification_token=bot_verification_token)
response = TraqMessageManager(bot, bot_access_token, base_url=base_url, base_client_url="https://q.trap.jp")

client = AuthenticatedClient(base_url=base_url, token=bot_access_token)


async def on_stamp(am: TraqMessage, payload: BotMessageStampsUpdatedPayload):
    am.write(f"```json\n{json.dumps(jsonable_encoder(payload), indent=2)}\n```")
    # long task
    with am.spinner():
        await asyncio.sleep(3)
    am.write(":done: Done!")


async def on_reply(am: TraqMessage, payload: MessageCreatedPayload):
    # 正規表現で先頭の `!{.*} ` を削除
    text = payload.message.text
    text = re.sub(r"^!\\{[^}]*\\}", "", text).lstrip()

    # 正規表現で https://q.trap.jp/messages/{message_id} を抽出
    message_text = re.search(r"https://q.trap.jp/messages/([0-9a-f-]+)", text)
    if message_text is None:
        # 引用投稿がなかったとき
        am.write("投稿を引用すると、タスクに追加できるよ！")
        return
    message_id = message_text.group(1)
    am.write(f"この投稿をタスクに追加するよ！\nhttps://q.trap.jp/messages/{message_id}")


@bot.event("BOT_MESSAGE_STAMPS_UPDATED")
async def on_stamps_updated(payload: BotMessageStampsUpdatedPayload) -> None:
    message_id = payload.messageId

    res = await get_message.asyncio(message_id=message_id, client=client)
    if res is None:
        return
    channel_id: str = res.channel_id

    await response(on_stamp, channnel_id=channel_id, payload=payload)


@bot.event("MESSAGE_CREATED")
async def on_message_created(payload: MessageCreatedPayload) -> None:
    channel_id = payload.message.channelId
    await response(on_reply, channnel_id=channel_id, payload=payload)

if __name__ == "__main__":
    bot.run(port=8080)
