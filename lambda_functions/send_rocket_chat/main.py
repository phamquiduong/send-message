import os

from services.rocket_chat import RocketChatService
from utils.sns import get_sns_msg


def handler(event, context):    # pylint: disable=W0613
    record = event["Records"][0]
    message = get_sns_msg(record)

    rocket = RocketChatService.from_token(
        token=os.environ['TOKEN'],
        user_id=os.environ['USER_ID'],
        domain=os.environ['DOMAIN']
    )

    rocket.send_message(room_id=os.environ['ROOM_ID'], message=message)
