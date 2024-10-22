import requests
from fasthtml.common import *
from components.header import header_html, header_css

def submission_page():
    return Html(
        Head(
            Title('Submission'),
            header_css()
        ),
        Body(
            header_html(),
            H1('Submission Page')
        )
    )
