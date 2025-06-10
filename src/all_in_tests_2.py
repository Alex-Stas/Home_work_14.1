class ShellScriptError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class ShellScriptEmpty(ShellScriptError):
    """Класс исключения при отсутствии кода скрипта"""

    def __init__(self, *args, **kwargs):
        self.message = 'Файл пустой.'


class ShellScriptShebang(ShellScriptError):
    """Класс исключения при отсутствии shebang"""

    def __init__(self, *args, **kwargs):
        self.message = 'В файле отсутствует shebang.'

#************************************************
class ShellScript:
    """Класс для работы с шелл-скриптами."""

    def __init__(self, script: str):
        if not script:  # Если скрипт пустой
            raise ShellScriptEmpty
        elif script[0:2] != '#!':  # Если отсутствует shebang
            raise ShellScriptShebang
        else:
            self.script = script

    def evaluate(self):
        # Код исполнения скрипта
        pass


if __name__ == '__main__':

    content = '#!'
    try:
        script = ShellScript(content)
        print('Скрипт прекрасен!')
    except ShellScriptEmpty:
        print('Отсутствует текст скрипта.')
    except ShellScriptShebang:
        print('Добавьте шебанг в скрипт.')
    except ShellScriptError:
        print('Ошибка при работе скрипта.')