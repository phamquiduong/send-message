import os

from services.slack import SlackService
from utils.sns import get_sns_msg


def handler(event, context):    # pylint: disable=W0613
    record = event["Records"][0]
    message = get_sns_msg(record)

    slack = SlackService(
        slack_token=os.environ['TOKEN'],
        channel=os.environ['CHANNEL']
    )

    slack.send_message(message)
