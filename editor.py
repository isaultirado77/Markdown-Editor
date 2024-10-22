from enum import Enum


def prompt_formater() -> str:
    option = input("Choose a formatter: ")
    if '-' in option:
        option = option.replace('-', '_')

    return option


def plain() -> str:
    return input('Text: ')


def bold() -> str:
    return f'**{input('Text: ')}**'


def italic() -> str:
    return f'*{input('Text: ')}*'


def inline_code() -> str:
    return f'`{input('Text: ')}`'


class LevelError(Exception):
    """Exception raised for errors in the level input."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def header() -> str:
    while True:
        try:
            level = int(input('Level: '))
            if level < 1:
                raise ValueError("Error: Enter a valid number")
            elif level > 6:
                raise LevelError("The level should be within the range of 1 to 6.")

            text = input('Text: ')
            return f"{'#' * level} {text}\n"

        except ValueError as ve:
            print(f"Error: {ve}")
        except LevelError as le:
            print(f"Error: {le}")


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


class FormatterOptions(Enum):
    PLAIN = 'plain'
    BOLD = 'bold'
    ITALIC = 'italic'
    HEADER = 'header'
    LINK = 'link'
    INLINE_CODE = 'inline-code'
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


class MarkdownDocument:
    def __init__(self):
        self.content = ""

    def add_text(self, new_text: str) -> None:
        self.content += new_text

    def get_content(self) -> str:
        return self.content

    def clear(self) -> None:
        self.content = ""

    def print_content(self) -> None:
        print(self.get_content())


# Mapping functions
formatter_functions = {
    FormatterOptions.PLAIN: plain,
    FormatterOptions.BOLD: bold,
    FormatterOptions.ITALIC: italic,
    FormatterOptions.HEADER: header,
    FormatterOptions.LINK: link,
    FormatterOptions.INLINE_CODE: inline_code,
    FormatterOptions.ORDERED_LIST: ordered_list,
    FormatterOptions.UNORDERED_LIST: unordered_list,
    FormatterOptions.NEW_LINE: new_line,
}


def run():
    document = MarkdownDocument()

    while True:
        try:
            option = prompt_formater()

            if option == Features.DONE.value:
                break

            if option == Features.HELP.value:
                FormatterOptions.print_values()
                Features.print_special_commands()

            formatter_option = FormatterOptions[option.upper()]
            result = formatter_functions[formatter_option]()

            document.add_text(result)
            document.print_content()

        except KeyError:
            print('Unknown formatting type or command')


def main():
    run()


if __name__ == '__main__':
    main()
