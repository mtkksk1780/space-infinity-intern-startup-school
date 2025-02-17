import os
from fasthtml.common import *
from components.utils import *

def header_html():
    backend_path = get_backend_path()
    print("header.py backend_path:", backend_path)

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
                    
                    Li(A("About", href="#")),
                    Li(A("Login", href="/login")),
                    # Li(A("Sign Up", href="/signup")),
                    Button("☰", _class="hamburger", onclick="toggleMenu()"),
                    _class="main-nav"
                )
            ),
            Div(
                Ul(
                    Li(A("History", href="/login", _id="history_link")),
                    Li(A("Feedback", href="/login", _id="feedback_link")),
                    Li(A("Submission", href="/login", _id="submission_link")),
                    Li(A("Project", href="/login", _id="project_link")),
                    Li(A("Account",href="/login", _id="account_link")),
                    Li(A("countdown",href="/countdown")),
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
            $(window).on('load', function() {
                setTimeout(() => {
                    const user_id = $('#user_id').val();
                    console.log('header.py user_id:', user_id);

                    if (user_id === undefined) {
                        console.log("User id is undefined");
                        return;
                    }

                    // Update links [1]
                    $('#project_link').attr('href', '/project');
                    $('#submission_link').attr('href', '/project');
                    $('#account_link').attr('href', '/account/' + user_id);

                    // Fetch the user's latest project id from the server
                    fetch(backend_path + '/project/' + user_id, {
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
                        
                        // Update links [2]
                        $('#submission_link').attr('href', '/submission/' + project_id);
                        $('#history_link').attr('href', '/history/' + project_id);
                        $('#feedback_link').attr('href', '/feedback');
                    })
                    .catch(error => console.error("Error fetching project id:", error));
                }, 1000);
            });
        '''),
    )
