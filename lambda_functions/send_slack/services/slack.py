import logging

from slack_sdk import WebClient
from slack_sdk.web.slack_response import SlackResponse

logger = logging.getLogger()


class SlackService:
    def __init__(self, slack_token: str, channel: str) -> None:
        self.client = WebClient(token=slack_token)
        self.channel = channel

    def send_message(self,  message: str, is_markdown: bool = False) -> SlackResponse:
        return self.client.chat_postMessage(
            channel=self.channel,
            text=message,
            mrkdwn=is_markdown
        )

    def send_message_visible_for_user(self,  message: str, user_id: str) -> SlackResponse:
        return self.client.chat_postEphemeral(
            channel=self.channel,
            text=message,
            user=user_id
        )

    def send_to_thread(self,  message: str, thread_ts: str) -> SlackResponse:
        return self.client.chat_postMessage(
            channel=self.channel,
            thread_ts=thread_ts,
            text=message
        )

    def update_message(self,  message: str, message_ts: str) -> SlackResponse:
        return self.client.chat_update(
            channel=self.channel,
            ts=message_ts,
            text=message
        )

    def delete_message(self,  message_ts: str) -> SlackResponse:
        return self.client.chat_delete(
            channel=self.channel,
            ts=message_ts
        )
