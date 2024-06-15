import os
import re

from aiotraq import AuthenticatedClient
from aiotraq.api.message import edit_message, get_message, remove_message_stamp
from aiotraq.models.message import Message
from aiotraq.models.post_message_request import PostMessageRequest
from aiotraq_bot import TraqHttpBot
from aiotraq_bot.models.event import (
    BotMessageStampsUpdatedPayload,
    MessageCreatedPayload,
)
from aiotraq_message import TraqMessage, TraqMessageManager

from src.bot.stamps import ampmstamps, clockstamps, daystamps, stamp_ids_rev
from src.bot.util import remove_bot_stamps

base_url = "https://q.trap.jp/api/v3"
bot_verification_token = os.getenv("BOT_VERIFICATION_TOKEN", "")
bot_access_token = os.getenv("BOT_ACCESS_TOKEN", "")

bot = TraqHttpBot(verification_token=bot_verification_token)
response = TraqMessageManager(bot, bot_access_token, base_url=base_url, base_client_url="https://q.trap.jp")

client = AuthenticatedClient(base_url=base_url, token=bot_access_token)

リマインドしたい曜日を選択してね = "リマインドしたい曜日を選択してね"
リマインドしたい時間を選択してね = "リマインドしたい時間を選択してね"
選択した曜日 = "選択した曜日"


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
    am.write(f"この投稿をタスクに追加するよ！\n{リマインドしたい曜日を選択してね}！直近一週間以降やリマインドがいらない場合は :day7_darkday:を選択してね！ \nhttps://q.trap.jp/messages/{message_id}")
    for s in daystamps:
        am.stamp(s)


@bot.event("BOT_MESSAGE_STAMPS_UPDATED")
async def on_stamps_updated(payload: BotMessageStampsUpdatedPayload) -> None:
    message_id = payload.messageId

    res = await get_message.asyncio(message_id=message_id, client=client)
    if res is None or not isinstance(res, Message):
        return

    message_text = re.search(r"https://q.trap.jp/messages/([0-9a-f-]+)", res.content)
    if message_text is None:
        return
    message_id = message_text.group(1)

    # 任意のbotのスタンプを削除したいかも
    stamps = remove_bot_stamps(res.stamps)

    if リマインドしたい曜日を選択してね in res.content:
        # stampsの中で daystamps に含まれていてかつ一番 createdAt が新しいものを取得
        selected_stamp = None
        for stamp in stamps:
            if stamp.stamp_id in daystamps:
                if selected_stamp is None or selected_stamp.created_at < stamp.created_at:
                    selected_stamp = stamp
        if selected_stamp is None:
            return

        text = f"この投稿をタスクに追加するよ！\n{選択した曜日}: :{stamp_ids_rev[selected_stamp.stamp_id]}:\n{リマインドしたい時間を選択してね}！\nhttps://q.trap.jp/messages/{message_id}"
        await edit_message.asyncio_detailed(
            message_id=message_id,
            client=client,
            body=PostMessageRequest(content=text)
        )

        for s in daystamps:
            if s != selected_stamp.stamp_id:
                await remove_message_stamp.asyncio_detailed(
                    message_id=message_id,
                    stamp_id=s,
                    client=client
                )

    elif リマインドしたい時間を選択してね in res.content:
        # stampsの中で clockstamps に含まれていてかつ一番 createdAt が新しいものを取得
        selected_clock = None
        for stamp in stamps:
            if stamp.stamp_id in clockstamps:
                if selected_clock is None or selected_clock.created_at < stamp.created_at:
                    selected_clock = stamp
        if selected_clock is None:
            return

        # stampsの中で ampmstamps に含まれていてかつ一番 createdAt が新しいものを取得
        selected_ampm = None
        for stamp in stamps:
            if stamp.stamp_id in ampmstamps:
                if selected_ampm is None or selected_ampm.created_at < stamp.created_at:
                    selected_ampm = stamp
        if selected_ampm is None:
            return

        for s in clockstamps + ampmstamps:
            if s != selected_clock.stamp_id and s != selected_ampm.stamp_id:
                await remove_message_stamp.asyncio_detailed(
                    message_id=message_id,
                    stamp_id=s,
                    client=client
                )

        text = f":loading: リマインドを設定中だよ！\nhttps://q.trap.jp/messages/{message_id}"
        await edit_message.asyncio_detailed(
            message_id=message_id,
            client=client,
            body=PostMessageRequest(content=text)
        )

        day_text = re.search(rf"{選択した曜日}: :([^:]+):", res.content)
        if day_text is None:
            return
        day_stamp = day_text.group(1)
        # day_index = daystamps.index(stamp_ids[day_stamp])

        # todo

        text = f"リマインドが設定されたよ！\n{選択した曜日}: :{day_stamp}:\n選択した時間: :{stamp_ids_rev[selected_ampm.stamp_id]}::{stamp_ids_rev[selected_clock.stamp_id]}:\nhttps://q.trap.jp/messages/{message_id}"
        await edit_message.asyncio_detailed(
            message_id=message_id,
            client=client,
            body=PostMessageRequest(content=text)
        )


@bot.event("MESSAGE_CREATED")
async def on_message_created(payload: MessageCreatedPayload) -> None:
    channel_id = payload.message.channelId
    await response(on_reply, channnel_id=channel_id, payload=payload)

if __name__ == "__main__":
    bot.run(port=8080)
