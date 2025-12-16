import aws_cdk as cdk
import yaml

from stack.rocket_stack import RocketStack
from stack.slack_stack import SlackStack

with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

app = cdk.App()

RocketStack(app, 'RocketStack', config=config['rocket_chat'])
SlackStack(app, 'SlackStack', config=config['slack'])

app.synth()
