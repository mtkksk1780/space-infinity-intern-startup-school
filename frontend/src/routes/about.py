import requests
from fasthtml.common import *
from global_css import global_css
from components.header import header_html, header_css
from components.footer import footer_html, footer_css

def about_page():
    return Html(
        Head(
            Title('About Us'),
            global_css(),
            header_css(),
            footer_css(),
        ),
        Body(
            header_html(),
            H1('About Us'),
            footer_html(),
        )
    )
