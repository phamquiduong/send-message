from rocketchat.api import RocketChatAPI


class RocketChatService:
    def __init__(self, **settings) -> None:
        self.api = RocketChatAPI(settings=settings)

    @classmethod
    def from_auth(cls, username: str, password: str, domain: str):
        return cls(username=username, password=password, domain=domain)

    @classmethod
    def from_token(cls, token: str, user_id: str, domain: str):
        return cls(token=token, user_id=user_id, domain=domain)

    def send_message(self, room_id: str, message: str):
        self.api.send_message(message=message, room_id=room_id)
