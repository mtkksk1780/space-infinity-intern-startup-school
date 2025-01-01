from fasthtml.common import *
#from components.header import header_html
#from components.footer import footer_html

def create_confirmation_page():
    return Html(
        Head(
            Title("Submission Page (Confirmation)"),
            Base(href="/confirmation"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
        ),
        Body(
            header_html(),
            Section(
                Div(
                    Img(src="/static/images/confirmation/back.png", alt="back", _class="back"),
                    Img(src="/static/images/confirmation/thankyou.png", alt="Thank you", _class="thankyou"),
                    Img(src="/static/images/confirmation/check_mark.png", alt="Checkmark", _class="checkmark"),
                    Img(src="/static/images/confirmation/complete.png", alt="complete", _class="complete"),                        Img(src="space-infinity/static/images/confirmation/layer.png", alt="layer", _class="layer"),
                    _class="confirmation-section"
                ),
                Div(
                    Input(placeholder="Type your email", _class="email_input"),
                    Button("Subscribe", _class="subscribe_button"),
                    _class="subscribe_section"
                ),
                Div(
                    P("Contact Us"),
                    P("contact@spaceinfinity.com"),
                    P("Space Infinity HQ"),
                    P("101 College St, Toronto, ON Canada M5G 1L7"),
                    _class="contact_section"
                ),
            ),
            footer_html(),
        ),
    )
