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
                Form(
                    get_form_attributes("/signup"),
                    Div(
                        Img(src="/static/images/signup/signup.png", _class="signup"),
                    ),
                    Div(
                        Input(placeholder="First Name", name="first_name", _class="first_name input-form"),
                        Input(placeholder="Email Address", name="email", _class="email input-form"),
                        Input(placeholder="Password", type="password", name="password", _class="password input-form"),
                        Input(placeholder="Confirm Password", type="password", name="confirm_password", _class="confirm_password input-form"),
                        _class="input_section"
                    ),
                    Div(
                        Button("CONFIRM", _class="submit confirm-btn"),
                        Button("SUBMIT", _class="submit disabled submit-btn"),
                    ),
                    _class="signup_section form_section"
                ),
            ),
            add_sweet_alert(),
            footer_html(),
            disable_button(),
            confirm_form("None"),
            back_form(),
            submit_form("/signup", "/login"),
        ),
    )
           