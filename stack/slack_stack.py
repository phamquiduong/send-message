from pathlib import Path

from aws_cdk import Duration, Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class SlackStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, config: dict[str, dict], **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.config = config

        # Email lambda layer
        layer_path = str(Path('lambda_layers/slack_sdk').resolve())
        slack_sdk_layer = _lambda.LayerVersion(
            self,
            'SlackChatLayer',
            code=_lambda.Code.from_asset(layer_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_13],
            description='Shared layer for slack lambda',
        )

        # Lambda function
        for config_id, connection in self.config.items():
            _lambda.Function(
                self,
                f'SendSlackMessageLambda{config_id}',
                function_name=f'send-slack-message-{config_id}',
                runtime=_lambda.Runtime.PYTHON_3_13,
                handler='send_message.handler',
                code=_lambda.Code.from_asset('lambda_functions/send_slack'),
                timeout=Duration.seconds(30),
                memory_size=256,
                layers=[slack_sdk_layer],
                environment={
                    'TOKEN': connection['token'],
                    'CHANNEL': connection['channel'],
                },
            )
