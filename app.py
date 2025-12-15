import aws_cdk as cdk
import yaml

from send_message.rocket_stack import RocketStack

with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

app = cdk.App()

RocketStack(app, 'RocketStack', config=config['rocket_chat'])

app.synth()
