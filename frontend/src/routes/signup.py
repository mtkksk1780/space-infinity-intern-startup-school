from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_signup_page():
    return Html(
        Head(
            Title("Signup Page"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/signup.css"),
        ),
        Body(
            header_html(), 
            Section(
                Div(
                    Img(src="/static/images/signup/signup.png",_class="signup"),
                ),
                Div(
                    Input(placeholder="First Name", _class="first_name"),
                    Input(placeholder="Email Address", _class="email"),
                    Input(placeholder="Password", _class="password"),
                    Input(placeholder="Confirm Password", _class="confirm_password"),
                    _class="input_section"
                ),
                _class="signup_section"
            ),
            footer_html()
        ),
    )
           