import requests
from fasthtml.common import *
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_about_page():
    return Html(
        Head(
            Title("About Us"),
            Base(href="/about"),
            Link(rel="stylesheet", href="../../static/styles/style.css"),
        ),
        Body(
            header_html(),
            H1("About Us"),
            footer_html(),
        )
    )
