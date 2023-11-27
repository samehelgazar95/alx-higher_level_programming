#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """text_indentation function for adding 2 lines after .:?

        Args:
            text: the string text

        Raises:
            TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ('.', ':', '?'):
            print(text[i], end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            if i < len(text):
                print('\n\n', end='')
        else:
            print(text[i], end='')
            i += 1


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
