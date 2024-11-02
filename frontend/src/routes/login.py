import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_login_page():
    return Html(
        Head(
            Title("Login"),
            Link(rel="stylesheet", href="../../static/style.css"),
        ),
        Body(
            header_html(),
            H1("Login Page"),
            footer_html(),
        )
    )