import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_home_page():
    return Html(
        Head(
            Title("Home Page"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/images/home/backk.png"),
        ),
        Body(
            header_html(), 
            Section(
                Div(
                    Img(src="/static/images/home/backk.png",_class="hero-img"),
                    Div(
                        Button("Join Now", _class="join_btn"),
                        _class="hero-content"
                    ),
                    _class="hero-section"
                )
            ),
            
            
                _class="home-section"
            ),
            footer_html() 
        ),  
    

        



        