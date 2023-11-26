from pywebio.input import textarea
from pywebio.output import *
from pywebio.pin import *
import pyperclip as clip


def lowercase():
    """Функция понижает регистр в основном окошке до строчного и выводит оповещение"""
    text = pin.text.lower()
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Lowered successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def uppercase():
    """Функция повышает регистр в основном окошке до заглавного и выводит оповещение"""
    text = pin.text.upper()
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is UpperCased successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def capitalized():
    """Функция делает первую букву текста заглавной и выводит оповещение"""
    text = pin.text.capitalize()
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Capitalized successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def trim():
    """Функция удаляет все переносы строки в окошке и выводит оповещение"""
    text = pin.text
    text = " ".join(text.split())
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Trimmed successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def paste():
    """Функция вставляет текст из буфера обмена в поле ввода текста и выводит оповещение"""
    text = clip.paste()
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text Pasted successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def copy():
    """Функция копирует текст из поля ввода в буфер обмена и выводит оповещение"""
    clip.copy(pin.text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Copied successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def clear_text():
    """Функция полностью очищает поле ввода текста и выводит оповещение"""
    text = ''
    pin_update('text', value=text)
    clear("alert")
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Cleared successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def replace_first(old, new):
    """
    Функция меняет первое появление подстроки old, на new и выводит оповещение

    old - подстрока, которую следует заменить на new
    new - подстрока, на которую следует заменить old
    """
    text = pin.text
    text = text.replace(old, new, 1)
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Replaced successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def replace_all(old, new):
    """
    Функция меняет все подстроки old, на new и выводит оповещение

    old - подстрока, которую следует заменить на new
    new - подстрока, на которую следует заменить old
    """
    text = pin.text
    text = text.replace(old, new)
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> All text Replaced successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')
