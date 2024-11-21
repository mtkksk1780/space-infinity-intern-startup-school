from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_login_page():
  return Html(
    Head(
      Title("Login Page"),
      Link(rel="stylesheet", href="/static/styles/style.css"),
      Link(rel="stylesheet", href="/static/styles/login.css"),
    ),
    Body(
      header_html(),      
      Section(
        Div(
          Img(src="/static/images/login/login.png",_class="login-img"),
        ),
        Div(
          Input(placeholder="Email Address", _class="email"),
          Input(placeholder="Password", _class="password"),
        ),
        Div(
          A("Forgot password?", _class="Forgot_password",href="#"),
        ),
        Div(
          A("Sign Up", _class="sign_up",href="/signup"),
        ),
        Div(
          Button("Enter", _class="enter",href="#"),
        ),
        _class="login_section"
      ),
      footer_html()
    ),
  )