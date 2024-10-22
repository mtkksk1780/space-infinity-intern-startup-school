import requests
from fasthtml.common import *
from components.header import header_html, header_css

def about_page():
    return Html(
        Head(
            Title('About Us'),
            header_css()
        ),
        Body(
            header_html(),
            H1('About Us'),
        )
    )
