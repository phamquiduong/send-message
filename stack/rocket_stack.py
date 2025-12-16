from pathlib import Path

from aws_cdk import Duration, Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class RocketStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, config: dict[str, dict], **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.config = config

        # Email lambda layer
        layer_path = str(Path('lambda_layers/rocket_chat').resolve())
        rocket_chat_layer = _lambda.LayerVersion(
            self,
            'RocketChatLayer',
            code=_lambda.Code.from_asset(layer_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_13],
            description='Shared layer for rocket lambda',
        )

        # Lambda function
        for config_id, connection in self.config.items():
            _lambda.Function(
                self,
                f'SendRocketMessageLambda{config_id}',
                function_name=f'send-rocket-message-{config_id}',
                runtime=_lambda.Runtime.PYTHON_3_13,
                handler='send_message.handler',
                code=_lambda.Code.from_asset('lambda_functions/send_rocket_chat'),
                timeout=Duration.seconds(30),
                memory_size=256,
                layers=[rocket_chat_layer],
                environment={
                    'TOKEN': connection['token'],
                    'USER_ID': connection['user_id'],
                    'DOMAIN': connection['domain'],
                    'ROOM_ID': connection['room_id'],
                },
            )
