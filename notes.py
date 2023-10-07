from note_controller import NoteController, show_commands
from settings import FILE_NAME

ctrl = NoteController(FILE_NAME)
exit_code = 1
input_code = 0

while input_code != exit_code:
    try:
        show_commands()
        input_code = int(input("Введите команду: ").strip())
        input_code = ctrl.workflow(input_code)
    except Exception as e:
        print(e.message)
