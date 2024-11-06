from fasthtml.common import *

# Footer
def footer_html():
  return Footer(
    Div(
      # Email subscription 
      Div(
        Img(src="static/images/footer.png", alt=" Image", _class="footer_img"),
        _class="fotter-section"
      ),
      Div(
        Form(
          Input(placeholder="Type your email", name="email", _class="footer_input"),
          Button("Subscribe", type="submit", _class="footer_btn"),
          action="http://127.0.0.1:8000/footer",
          method="post",
          target="hidden_iframe",
        ),
        _class="footer_subscribe"
      ),
        
      # hidden iframe to handle the response
      Iframe(name="hidden_iframe", style="display:none;"),

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
    )
  )