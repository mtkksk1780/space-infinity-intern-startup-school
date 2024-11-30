from fasthtml.common import *

def header_html():
    return Header(
        Head(
            Title("Home Page"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="static/styles/header.css"),
        ),
        Div(
             A(
                Img(src="/static/images/header/space_infinity_log.png", alt="Space Infinity Logo", _class="logo"),
                href="/"
                ),
            Nav(
                Ul(
                    Li(A("Home", href="/")),
                    Li(A("Submission", href="/submission")),
                    Li(A("Login", href="/login")),
                    Li(A("Sign Up", href="/signup")),
                    Li(A("Project",href="/project")),
                    Button("Explorer", _class="hamburger", onclick="toggleMenu()"),
                    _class="main-nav"
                )
            ),
            Div(
                Ul(
                    Li(A("About", href="#")),
                    Li(A("History", href="/history")),
                    Li(A("Feedback", href="/feedback")),
                    Li(A("Contact", href="/contact")),
                    _class="hamburger-menu"
                ),
                _class="hamburger-menu-container"
            ),
            Script(
                """
                function toggleMenu() {
                    const menu = document.querySelector('.hamburger-menu-container');
                    menu.classList.toggle('active');
                }
                """
            ),
            _class="header-container"
        )
    )
