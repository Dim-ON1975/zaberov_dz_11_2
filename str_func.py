def text_upper(text: str) -> str:
    """
    Функция, которая переводит все буквы текста
    в верхний регистр, т.е. делает их заглавными.
    :param text: строка, str
    :return: строка в верхнем регистре, str
    """
    return text.upper()


def text_title(text: str) -> str:
    """
    Функция, которая делает заглавными
    первые буквы каждого слова
    :param text: строка, str
    :return: строка из слов, начинающихся с заглавных букв, str
    """
    return text.title()
