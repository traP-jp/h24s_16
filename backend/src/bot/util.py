from aiotraq.models.message_stamp import MessageStamp


bot_id = "e2ea7f48-e60d-46ff-9a6e-3b043a8a71bc"


def remove_bot_stamps(stamps: list[MessageStamp]) -> list[MessageStamp]:
    return [stamp for stamp in stamps if stamp.user_id != bot_id]
