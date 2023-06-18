from note_controller import NoteController
from settings import FILE_NAME

ctrl = NoteController(FILE_NAME)
exit_code = 1
input_code = 0
while input_code != exit_code:
    try:
        ctrl.show_commands()
        input_code = int(input("Введите команду: ").strip())
        input_code = ctrl.workflow(input_code)
    except ValueError:
        print("Invalid integer!")

print(f"Result: {input_code}")
