from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_account_page():
    return Html(
        Head(
            Title("Account Infromation Page"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/account.css"),
        ),
        Body(
            header_html(), 
            Section(
                Div(
                    Img(src="/static/images/account/account.png",_class="account_img"),
                ),
                Div(
                    H1("Your account information", _class="project_titel"),
                    H3("Name",_class="name"),
                    Input(_class="input_name"),
                    H3("Email Address",_class="email"),
                    Input( _class="input_email"),
                    H3("Password",_class="password"),
                    Input( _class="input_password"),
                  
                    _class="input_section"
                ),
                Div(
                   Button("Update",_class="update") 
                ),

                _class="project_section"
            ),
            footer_html()
        ),
    )
           