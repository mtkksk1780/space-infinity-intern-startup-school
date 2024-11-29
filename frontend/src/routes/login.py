from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from urllib.parse import parse_qs
from components.utils import *

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
        Form(
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
            Button("Enter", type="submit", _class="enter"),
          ),
          **get_form_attributes("/login"),
        ),
        _class="login_section"
      ),
      footer_html(),
      Script("""
                $(document).ready(function() {
                    $('form').on('submit', function(event) {
                        event.preventDefault();
                        
                        const form = $(this);
                        const formData = new FormData(this);

                        $.ajax({
                            url: form.attr('action'),
                            method: form.attr('method'),
                            data: formData,
                            processData: false,
                            contentType: false,
                            success: function() {
                                alert("Login successful!");
                                window.location.href = "/";
                            },
                            error: function(xhr) {
                                const errorDetail = xhr.responseJSON?.detail || "Something went wrong!";
                                alert(errorDetail);
                            }
                        });
                    });
                });
            """),
      add_jquery(),
    ),
  )