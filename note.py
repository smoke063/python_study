import uuid
from datetime import datetime, timezone

import jsons


class Note:
    def __init__(self, title: str, msg: str):
        self.id = uuid.uuid4()
        self.title = title
        self.msg = msg
        self.modifiedTime = datetime.now(timezone.utc)

    def to_json(self) -> str:
        return jsons.dumps(self)
