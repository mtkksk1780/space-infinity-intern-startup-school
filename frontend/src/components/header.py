from fasthtml.common import *
from components.utils import *

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
            P(_class="logged-in"),
            Nav(
                Ul(
                    Li(A("Home", href="/")),
                    Li(A("Submission", href="/login", _id="submission_link")),
                    Li(A("Login", href="/login")),
                    Li(A("Sign Up", href="/signup")),
                    Li(A("Project", href="/project", _id="project_link")),
                    Button("Explorer", _class="hamburger", onclick="toggleMenu()"),
                    _class="main-nav"
                )
            ),
            Div(
                Ul(
                    Li(A("About", href="#")),
                    Li(A("History", href="/login", _id="history_link")),
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
        ),
        add_jquery(),
        Script('''
            // Get user id from the hidden input field
            $(document).ready(function() {
                const user_id = $('#user_id').val();
                console.log('header.py user_id:', user_id);

                if (user_id === undefined) {
                    console.error("User id is undefined");
                    return;
                }

                // Update the project link with the user id
                $('#submission_link').attr('href', '/project');

                // Fetch the user's latest project id from the server
                fetch('http://127.0.0.1:8000/project/' + user_id, {
                    method: 'POST',
                    credentials: 'include',
                })
                .then(response => response.json())
                .then(data => {
                    const project_id = data;
                    console.log("header.py latest project id:", project_id);

                    if (project_id === undefined || typeof project_id !== 'string') {
                        console.error("Error fetching project id");
                        return;
                    }
                    // Update links with the project id
                    $('#submission_link').attr('href', '/submission/' + project_id);
                    $('#history_link').attr('href', '/history/' + project_id);
                })
                .catch(error => console.error("Error fetching project id:", error));
            });
        '''),
    )
