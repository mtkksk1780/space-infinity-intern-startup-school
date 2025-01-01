from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_signup_page():
    return Html(
        Head(
            Title("Signup Page"),
            Base(href="/signup"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/signup.css"),
        ),
        Body(
            add_jquery(),
            get_session_info("/signup"),
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
            add_sweet_alert(),
            footer_html(),
            confirm_form(),
            back_form(),
            submit_form("/signup", "/login"),
        ),
    )
           