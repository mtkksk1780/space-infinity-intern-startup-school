from fasthtml.common import *
from urllib.parse import parse_qs
from components.utils import *

# Footer
def footer_html():
  return Footer(
    Div(
      # Email subscription 
      Div(
        Img(src="static/images/footer/footer.png", alt=" Image", _class="footer_img"),
        _class="fotter-section"
      ),
      Div(
        Form(
          Input(placeholder="Type your email", name="email", _class="footer_input input-form"),
          Button("Subscribe", type="submit", _class="footer_btn submit-btn"),
          **get_form_attributes("/footer"),
        ),
        _class="footer_subscribe"
      ),
      # Response Iframe
      add_iframe(),
      # Links 
      Div(
        A("Home Page", href="/"),
        A("About Us", href="#"),
        A("Submission", href="/submission"),
        A("Progress Tracking", href="#"),
        A("Log In", href="#"),
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
      _class="footer-container"
    ),
    add_jquery(),
    clear_form(),
  )