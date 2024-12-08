from fasthtml.common import *
from urllib.parse import parse_qs
from components.utils import *

def footer_html():
    return Div(
        Head(
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/footer.css"),
        ),
        Div(
            Footer(
                Img(src="/static/images/footer/footer.png", alt="Footer Image", _class="footer_img"),
                Div(
                    # Email subscription 
                    # Div(
                    #     Form(
                    #         Input(placeholder="Type your email", name="email", _class="footer_input input-form"),
                    #         Button("Subscribe", type="submit", _class="footer_btn submit-btn"),
                    #     ),
                    #     _class="footer_subscribe"
                    # ),
                    Div(
                        # Links 
                        Div(
                            A("Home Page", href="/"),
                            A("About Us", href="#"),
                            A("Submission", href="/submission"),
                            A("Progress Tracking", href="#"),
                            A("Log In", href="/login"),
                            _class="footer-links"
                        ),
                        # Contact
                        Div(
                            P("Contact Us"),
                            P("tenatch10@gmail.com"),
                            P("ONRamp, 100 College St."),
                            P("Toronto, ON Canada M5G1L5"),
                            _class="footer-contact"
                        ),
                        _class="footers"
                    ),
                    _class="footer-container"
                ),
            ),
        ),
        add_jquery(),
        clear_form(),
    )
