from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_contact_page():
    return Html(
        Head(
            Title("Contact age"),
            Base(href="/contact"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/contact.css"),
        ),
        Body(
            header_html()

        ),

        Section(
        Div(
        Img(src="/static/images/contact/contact.png",_class="contact")    
        ),
        Div(
            Input(placeholder="Your Name", _class="input-name"),
            Input(placeholder="Email Address",_class="input-email"),
                        Input(placeholder="Questions / Coments",_class="quesiotns"),

        ),
        Div(
            Button("Send",_class="send")
        ),
        _class="contact-seciton"
    ),


         footer_html() 

      )

          