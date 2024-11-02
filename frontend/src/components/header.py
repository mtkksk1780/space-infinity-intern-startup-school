from fasthtml.common import *

# Header
def header_html():
  return Header(
    Div(
      Img(src="static/images/space_infinity_log.png", alt="Space Infinity Logo", _class="logo"),
    ),
    Div(
      Nav(
        Ul(
          Li(A("Home", href="/")),
          Li(A("About", href="#")),
          Li(A("Explorer", href="#")),
          Li(A("Contact", href="#")),
          Li(A("Submission", href="/submission")),
          Li(A("Login", href="#"))
        )
      ),
      _class="nav"
    ),
    _class="header-container"
  ),

