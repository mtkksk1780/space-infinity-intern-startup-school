from fasthtml.common import *

def header_html():
    return Header(
        Head(
            Title("Home Page"),
            Link(rel="stylesheet", href="/static/style/style.css"),
            Link(rel="stylesheet", href="/static/style/header.css"),
        ),
        Div(
             A(
                Img(src="/static/images/header/space_infinity_log.png", alt="Space Infinity Logo", _class="logo"),
                href="/"
                ),
            Nav(
                Ul(
                    Li(A("Home", href="/")),
                    Li(A("About", href="#")),
                    Li(A("Explorer", href="#")),
                    Li(A("Contact", href="#")),
                    Li(A("Submission", href="/submission")),
                    Li(A("Login", href="/login")),
                    Li(A("Sign Up", href="/signup")),
                    Button("☰", _class="hamburger", onclick="toggleMenu()"),
                    _class="main-nav"
                )
            ),
            Div(
                Ul(
                    Li(A("History", href="/history")),
                    Li(A("Feedback", href="/feedback")),
                    Li(A("Contact", href="#")),
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
