from fasthtml.common import *

def footer_html():
    return Div(
        Head(
            Link(rel="stylesheet", href="/static/style/style.css"),
            Link(rel="stylesheet", href="/static/style/footer.css"),
        ),
        Div(
            Footer(
                Img(src="/static/images/footer/footer.png", alt="Footer Image", _class="footer_img"),
                Div(
                    Div(
                        Input(placeholder="Type your email", _class="footer_input"),
                        Button("Subscribe", _class="footer_btn"),
                        _class="footer_subscribe"
                    ),
                    Div(
                    Div(
                        A("Home Page", href="/"),
                        A("About Us", href="#"),
                        A("Submission", href="/submission"),
                        A("Progress Tracking", href="#"),
                        A("Log In", href="/login"),
                        _class="footer-links"
                    ),
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
            )
        )
    )
