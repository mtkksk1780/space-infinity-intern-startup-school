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
                Img(src="/static/images/footer/footerr.png", alt="Footer Image", _class="footer_img"    
            ),
            # Contact
            Div(
                P("Contact:tenatch10@gmail.com"),
                P("ONRamp, 100 College St.Toronto, ON Canada M5G1L5"),
                _class="footer-contact"
            ),
            _class="footers"
            ),
        ),
        add_jquery(),
    )
