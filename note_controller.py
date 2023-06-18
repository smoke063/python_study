from enum import IntEnum

from note import Note


class Operations(IntEnum):
    EXIT = 1
    SHOW_ALL = 2
    ADD = 3
    REMOVE = 4
    READ = 5


class NoteController:
    def __init__(self, f_name):
        self.f_name = f_name

    def show_commands(self):
        print("Команды:")
        print("1. выход")
        print("2. показать все")
        print("3. добавить заметку")
        print("4. удалить заметку")

    def workflow(self, input_code):
        match input_code:
            case Operations.EXIT:
                return Operations.EXIT
            case Operations.SHOW_ALL:
                return Operations.EXIT
            case Operations.ADD:
                self.add()
        return input_code

    def add(self):
        note = Note(
            input("Введите заголовок заметки: "),
            input("Введите тело заметки: ")
        ).to_json()

        with open(self.f_name, "a+") as f:
            f.write(note)
            f.write("\n")
