from datetime import datetime
from random import randint

import jsons

format_date = "%d.%m.%Y %H:%M:%S"


class Note:
    def __init__(self, title: str, msg: str):
        self.id = randint(1, 1000000)
        self.title = title
        self.msg = msg
        self.modified_time = datetime.now().strftime(format_date)

    def __str__(self):
        return (f"id {self.id}\n"
                f" modified time {self.modified_time}\n"
                f" title {self.title}\n"
                f" message body {self.msg}\n")

    def to_json(self) -> str:
        return jsons.dumps(self)

    @staticmethod
    def from_json(s: str):
        data = jsons.load(s)
        return Note(
            data["title"],
            data["msg"],
            data["id"],
            data["modified_time"]
        )
