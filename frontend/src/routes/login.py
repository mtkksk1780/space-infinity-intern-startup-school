from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_login_page():
  return Html(
    Head(
      Title("Login Page"),
      Base(href="/login"),
      Link(rel="stylesheet", href="/static/styles/style.css"),
      Link(rel="stylesheet", href="/static/styles/login.css"),
    ),
    Body(
      add_jquery(),
      get_session_info("/login"),
      header_html(),
      Section(
        Div(
          Img(src="/static/images/login/login.png",_class="login-img"),
        ),
        Form(
          get_form_attributes("/login"),
          Div(
            Input(placeholder="Email Address", name="email", _class="email"),
            Input(placeholder="Password", name="password" ,_class="password"),
          ),
          Div(
            A("Forgot password?", _class="Forgot_password",href="#"),
          ),
          Div(
            A("Sign Up", _class="sign_up",href="/signup"),
          ),
          Div(
            Button("Enter", type="submit", _class="enter submit-btn"),
          ),
        ),
        _class="login_section"
      ),
      add_sweet_alert(),
      footer_html(),
      submit_form("/login", "/"),
    ),
  )