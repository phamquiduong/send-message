def get_sns_msg(record: dict) -> str:
    sns = record["Sns"]
    return sns["Message"]
