import json
from datetime import datetime

def save_log_to_file(log):
    with open("logger/log.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")


def log(message):
    log_message = {"timestamp": str(datetime.now()) ,"message": message}
    save_log_to_file(log_message)