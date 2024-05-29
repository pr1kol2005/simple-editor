from pywebio.output import *
from pywebio.pin import *
import pyperclip as clip


def lowercase():
    """Функция понижает регистр в основном окошке до строчного и выводит оповещение в случае изменений"""
    text = pin.text
    pin_update('text', value=text.lower())
    clear("alert")
    if pin.text != text:
        put_success(put_html("<b>Success</b> Lowered successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def uppercase():
    """Функция повышает регистр в основном окошке до заглавного и выводит оповещение в случае изменений"""
    text = pin.text
    pin_update('text', value=text.upper())
    clear("alert")
    if pin.text != text:
        put_success(put_html("<b>Success</b> UpperCased successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def capitalized():
    """Функция делает первую букву текста заглавной и выводит оповещение в случае изменений"""
    text = pin.text
    pin_update('text', value=text.capitalize())
    clear("alert")
    if pin.text != text:
        put_success(put_html("<b>Success</b> Capitalized successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def trim():
    """Функция удаляет все переносы строки в окошке и выводит оповещение в случае изменений"""
    text = pin.text
    pin_update('text', value=" ".join(text.split()))
    clear("alert")
    if pin.text != text:
        put_success(put_html("<b>Success</b> Trimmed successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def paste():
    """Функция вставляет текст из буфера обмена в поле ввода текста и выводит оповещение"""
    text = clip.paste()
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Pasted successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def copy():
    """Функция копирует текст из поля ввода в буфер обмена и выводит оповещение"""
    clip.copy(pin.text)
    clear("alert")
    put_success(put_html("<b>Success</b> Copied successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def clear_text():
    """Функция полностью очищает поле ввода текста и выводит оповещение"""
    text = ''
    pin_update('text', value=text)
    clear("alert")
    put_success(put_html("<b>Success</b> Cleared successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def replace_first(old, new):
    """
    Функция меняет первое появление подстроки old, на new и выводит оповещение в случае изменений

    old - подстрока, которую следует заменить на new
    new - подстрока, на которую следует заменить old
    """
    text = pin.text
    pin_update('text', value=text.replace(old, new, 1))
    clear("alert")
    if pin.text != text:
        put_success(put_html("<b>Success</b> Replaced successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def replace_all(old, new):
    """
    Функция меняет все подстроки old, на new и выводит оповещение в случае изменений

    old - подстрока, которую следует заменить на new
    new - подстрока, на которую следует заменить old
    """
    text = pin.text
    pin_update('text', value=text.replace(old, new))
    clear("alert")
    if pin.text != text:
        put_success(put_html("<b>Success</b> Replaced successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def upload():
    """Функция помещает содержимое загруженного текстового файла в окно для редактирования и выводит оповещение"""
    clear("alert")
    if pin.file_upload:
        file = pin.file_upload['content'].decode()
        pin_update('text', value=file)
        put_success(put_html("<b>Success</b> File uploaded successfully!"), closable=True, scope="alert")
    scroll_to("alert", position='bottom')


def show_popup():
    """Функция открывает всплывающее окошко с возможностью скачать измененый файл"""
    popup('Download file', put_file('edited_file.txt', content=(pin.text.encode() if pin.text else bytes())),
          size=PopupSize.NORMAL)


def sum_of_digits(number):
    return sum([int(i) for i in list(number)])
