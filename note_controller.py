import json
from datetime import datetime
from enum import IntEnum
from os.path import isfile

from note import Note


class Operations(IntEnum):
    EXIT = 1
    SHOW_ALL = 2
    ADD = 3
    REMOVE = 4
    MODIFIED = 5


def show_commands():
    print("Команды:")
    print("1. выход")
    print("2. показать все")
    print("3. добавить заметку")
    print("4. удалить заметку")
    print("5. изменить заметку")


class NoteController:
    def __init__(self, f_name):
        self.f_name = f_name

    def create_file_if_not_existed(self):
        check_file = isfile(self.f_name)
        if not check_file:
            data = {"notes": []}
            data = json.dumps(data)
            data = json.loads(str(data))
            with open(self.f_name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

    def workflow(self, input_code):

        match input_code:
            case Operations.EXIT:
                return Operations.EXIT
            case Operations.SHOW_ALL:
                self.show_all()
            case Operations.ADD:
                self.add()
            case Operations.REMOVE:
                self.remove()
            case Operations.MODIFIED:
                self.modified()
        return input_code

    def show_all(self):
        check_file = isfile(self.f_name)
        data = {"notes": []}
        if check_file:
            with open(self.f_name, "r", encoding="utf-8") as f_out:
                data = json.load(f_out)
        sorted_lst = sorted(data["notes"], key=lambda x: datetime.strptime(x['modified_time'], '%d.%m.%Y %H:%M:%S'))
        for c, n in enumerate(sorted_lst, 1):
            print(f"---------------------------------------\n")
            print(f" номер строки {c}\n")
            print(f" id {n['id']}\n")
            print(f" modified time {n['modified_time']}\n")
            print(f" title {n['title']}\n")
            print(f" message body  {n['msg']}\n")
            print(f"---------------------------------------\n")

    def add(self):
        note = Note(
            input("Введите заголовок заметки: "),
            input("Введите тело заметки: ")
        ).__dict__
        check_file = isfile(self.f_name)
        data = {"notes": []}
        if check_file:
            with open(self.f_name, "r", encoding="utf-8") as f_out:
                data = json.load(f_out)

        with open(self.f_name, "w", encoding="utf-8") as f_in:
            data["notes"].append(note)
            data = json.dumps(data)
            data = json.loads(str(data))
            json.dump(data, f_in, indent=4)

    def modified(self):
        input_code = int(input("Для изменения записи введите ID заметки: ").strip())
        note = Note(
            input("Введите заголовок заметки: "),
            input("Введите тело заметки: ")
        ).__dict__
        data = {"notes": []}
        if isfile(self.f_name):
            with open(self.f_name, "r", encoding="utf-8") as f_out:
                data = json.load(f_out)
                data["notes"] = [x for x in data["notes"] if x["id"] != input_code]
                data["notes"].append(note)

        with open(self.f_name, "w", encoding="utf-8") as f_in:
            data = json.dumps(data)
            data = json.loads(str(data))
            json.dump(data, f_in, indent=4)

    def remove(self):
        input_code = int(input("Для удаления записи введите ID заметки: ").strip())
        data = {"notes": []}
        if isfile(self.f_name):
            with open(self.f_name, "r", encoding="utf-8") as f_out:
                data = json.load(f_out)
                data["notes"] = [x for x in data["notes"] if x["id"] != input_code]

        with open(self.f_name, "w", encoding="utf-8") as f_in:
            data = json.dumps(data)
            data = json.loads(str(data))
            json.dump(data, f_in, indent=4)
