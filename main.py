import pywebio
from pywebio import config, start_server
from pywebio.session import go_app

from text_edit_functions import *


def change_theme(theme_color):
    """
    Функция меняет тему страницы на заданную

    btn_colot - тема, которую следует установить (светлая / темная)
    """
    if theme_color == 'dark':
        put_row([None, put_button('Dark mode', color=theme_color, outline=True,
                                  onclick=lambda: go_app(theme_color, new_window=False))], size="75% 20%")
    else:
        put_row([None, put_button('Light mode', color=theme_color, outline=True,
                                  onclick=lambda: go_app('index', new_window=False))], size="75% 20%")
    put_html("<h1>Simple Text Editor</h1>")
    put_buttons([
        {'label': 'LowerCase', 'value': 'lower', "color": theme_color},
        {'label': 'UpperCase', 'value': 'upper', "color": theme_color},
        {'label': 'Capitalize', 'value': 'capital', "color": theme_color},
        {'label': 'Trim', 'value': 'trim', "color": theme_color},
        {'label': 'Copy', 'value': 'copy', "color": theme_color},
        {'label': 'Paste', 'value': 'paste', "color": theme_color},
        {'label': 'Clear', 'value': 'clear', "color": theme_color}],
        onclick=[lowercase, uppercase, capitalized, trim, copy, paste, clear_text], outline=True).style(
        "margin-bottom:20px;")
    put_file_upload('file_upload', accept='.txt', placeholder='Choose a .txt file (max size is 1 megabyte)',
                    max_size='4m')
    put_row([put_button(label='Download file', color=theme_color, onclick=show_popup, outline=True),
             put_button(label='Upload file', color=theme_color, onclick=upload, outline=True)], size="150px 200px")
    put_textarea('text', rows=7, placeholder="type something...").style("margin-bottom:30px;")
    put_row([put_button("ReplaceOnce", color=theme_color,
                        onclick=lambda: replace_first(pin.replace_old, pin.replace_new), outline=True), None,
             put_textarea('replace_old', rows=2, help_text="Substring to be replaced"), None,
             put_textarea('replace_new', rows=2, help_text="New text")],
            size="100px 40px 200px 20px 200px").style("margin-bottom:20px;")
    put_row([put_button("ReplaceAll", color=theme_color,
                        onclick=lambda: replace_all(pin.replaceall_old, pin.replaceall_new), outline=True), None,
             put_textarea('replaceall_old', rows=2, help_text="Substring to be replaced"), None,
             put_textarea('replaceall_new', rows=2, help_text="New text")],
            size="100px 40px 200px 20px 200px").style("margin-bottom:5px;")
    put_scope("alert").style("position:relative;left:80%;width:400px;")


@config(theme='default', title="Simple Text Editor")
def index():
    """Создание светлой версии страницы"""
    change_theme('dark')


@config(theme='dark', title="Simple Text Editor")
def dark():
    """Создание темной версии страницы"""
    change_theme('light')


if __name__ == "__main__":
    start_server([index, dark], debug=True, remote_access=True, max_payload_size='4m')
