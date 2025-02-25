from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_account_page(user_id: str):
    endpoint = get_backend_path() + "/account/" + user_id

    # Get user account information from backend
    account_info = get_data(endpoint)

    print("account_info:", account_info)

    # Extract project information
    name = account_info["account_info"]["name"]
    email = account_info["account_info"]["email"]
    password = account_info["account_info"]["password"]

    return Html(
        Head(
            Title("Account Information Page"),
            Base(href="/account"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/account.css"),
        ),
        Body(
            add_jquery(),
            get_session_info("/account"),
            header_html(),
            Section(
                Form(
                    get_form_attributes("/account"),
                    Div(
                        Img(src="/static/images/account/account.png",_class="account_img"),
                    ),
                    Div(
                        H1("Your account information", _class="project_titel"),
                        H3("Name",_class="name"),
                        Input(placeholder="First Name", name="first_name", _class="input_name input-form", value=name),
                        H3("Email Address",_class="email"),
                        Input(placeholder="Email Address", name="email", _class="input_email input-form", value=email),
                        H3("Password",_class="password"),
                        Input(placeholder="Password", type="password", name="password", _class="input_password input-form", value=password),
                        H3("Confirmation",_class="confirm_password"),
                        Input(placeholder="Confirm Password", type="password", name="confirm_password", _class="input_confirm_password input-form", value=password),

                        _class="input_section"
                    ),
                    Div(
                        Button("CONFIRM", _class="submit confirm-btn"),
                        Button("UPDATE", _class="submit disabled submit-btn"),
                    ),

                    _class="project_section form_section"
                ),
            ),
            add_sweet_alert(),
            footer_html(),
            disable_button(),
            confirm_form("None"),
            back_form(),
            submit_form("/account", "None"),
        ),
    )
