from enum import Enum


class Formatter(Enum):
    PLAIN = 'plain'
    BOLD = 'bold'
    ITALIC = 'italic'
    HEADER = 'header'
    LINK = 'link'
    INLINE = 'inline-code'
    ORDERED_LIST = 'ordered-list'
    UNORDERED_LIST = 'unordered-list'
    NEW_LINE = 'new-line'

    @classmethod
    def get_values_as_tuple(cls):
        return (formatter.value for formatter in cls)

    @classmethod
    def get_available_formatters(cls) -> str:
        return 'Available formatters: ' + ' '.join(formatter for formatter in cls.get_values_as_tuple())

    @classmethod
    def print_values(cls) -> None:
        print(cls.get_available_formatters())


class Features(Enum):
    HELP = '!help'
    DONE = '!done'

    @classmethod
    def get_special_commands(cls) -> str:
        return 'Special commands: ' + ' '.join(command.value for command in cls)

    @classmethod
    def print_special_commands(cls) -> None:
        print(cls.get_special_commands())


class Text:
    pass


def prompt_formater() -> str:
    return input("Choose a formatter: ")


def plain() -> str:
    return input()


def bold() -> str:
    return f'**{input()}**'


def italic() -> str:
    return f'*{input()}*'


def inline_code() -> str:
    return f'`{input()}`'


def header() -> str:
    try:
        level = int(input('Level: '))
        if level < 1:
            raise ValueError

        text = input()
        return '#' * level + text

    except ValueError:
        print("Error: Enter a valid number")


def link() -> str:
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def new_line() -> str:
    return '\n'


def ordered_list():
    pass


def unordered_list():
    pass


def run():
    while True:
        option = prompt_formater()

        if option == Features.DONE.value:
            break

        if option == Features.HELP.value:
            Formatter.print_values()
            Features.print_special_commands()

        elif option in Formatter.get_values_as_tuple():
            pass

        else:
            print('Unknown formatting type or command')


def main():
    run()


if __name__ == '__main__':
    main()
