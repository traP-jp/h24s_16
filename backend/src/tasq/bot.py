import asyncio
import json
import os


from aiotraq_bot import TraqHttpBot
from aiotraq_message import TraqMessage, TraqMessageManager


async def component(am: TraqMessage, payload: dict):
    am.write(json.dumps(payload))
    # long task
    with am.spinner():
        await asyncio.sleep(3)
    am.write(":done: Done!")

bot = TraqHttpBot(verification_token=os.getenv("BOT_VERIFICATION_TOKEN"))
response = TraqMessageManager(bot, os.getenv("BOT_ACCESS_TOKEN", ""), "https://q.trap.jp/api/v3", "https://q.trap.jp")


@bot.event("MESSAGE_CREATED")
async def on_message_created(payload) -> None:
    channel_id = payload.message.channelId
    # message = payload.message.plainText

    await response(component, channnel_id=channel_id, payload=payload)

if __name__ == "__main__":
    bot.run(port=8080)
