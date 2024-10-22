from enum import Enum


def main():
    pass


if __name__ == '__main__':
    main()


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


class Features(Enum):
    HELP = '!help!'
    DONE = '!done'


def prompt_formater() -> str:
    return input("Choose a formatter: ")

def run():
    pass

