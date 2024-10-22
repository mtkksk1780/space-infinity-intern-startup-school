import requests
from fasthtml.common import *
from components.header import header_html, header_css

def login_page():
    return Html(
        Head(
            Title('Login'),
            header_css()
        ),
        Body(
            header_html(),
            H1('Login Page')
        )
    )