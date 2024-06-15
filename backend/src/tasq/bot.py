import asyncio
import json
import os

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


async def component(am: TraqMessage, payload: MessageCreatedPayload | BotMessageStampsUpdatedPayload):
    am.write(f"```json\n{json.dumps(jsonable_encoder(payload), indent=2)}\n```")
    # long task
    with am.spinner():
        await asyncio.sleep(3)
    am.write(":done: Done!")


@bot.event("BOT_MESSAGE_STAMPS_UPDATED")
async def on_stamps_updated(payload: BotMessageStampsUpdatedPayload) -> None:
    message_id = payload.messageId

    res = await get_message.asyncio(message_id=message_id, client=client)
    if res is None:
        return
    channel_id: str = res.channel_id

    await response(component, channnel_id=channel_id, payload=payload)


@bot.event("MESSAGE_CREATED")
async def on_message_created(payload: MessageCreatedPayload) -> None:
    channel_id = payload.message.channelId
    # message = payload.message.plainText

    await response(component, channnel_id=channel_id, payload=payload)

if __name__ == "__main__":
    bot.run(port=8080)
