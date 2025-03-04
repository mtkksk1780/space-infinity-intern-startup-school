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

                    // Get current time
                    const current_date = new Date();
                    console.log('header.py current_date:', current_date);

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
                        $('#project_link').attr('href', '/project/' + project_id);
                        $('#submission_link').attr('href', '/submission/' + project_id);
                        $('#history_link').attr('href', '/history/' + project_id);
                        $('#feedback_link').attr('href', '/feedback');

                        // Get the project's countdown time
                        fetch(backend_path + '/countdown/' + project_id, {
                            method: 'POST',
                            credentials: 'include',
                        })
                        .then(response => response.json())
                        .then(data => {
                            const countdown = data.countdown;
                            let current_week = data.current_week;
                            console.log("header.py countdown:", countdown);
                            console.log("header.py current_week:", current_week);

                            if (countdown === undefined || typeof countdown !== 'string') {
                                console.error("Error fetching countdown");
                                return;
                            }

                            // If the previous week's progress is not submitted, automatically update the status as incomplete.
                            if (current_week !== 1) {
                                console.log(`Check if the previous weeks' progress has been submitted`);
                                if (current_week > 5) {
                                    current_week = 5;
                                }
                                for (let i = 1; i < parseInt(current_week); i++) {
                                    fetch(backend_path + '/submission/status/' + project_id + '/' + i, {
                                        method: 'POST',
                                        credentials: 'include',
                                    })
                                    .then(response => response.json())
                                    .then(data => {
                                        const submission_status = data.submission_status;
                                        console.log(`header.py week${i}'s status:`, submission_status);

                                        // If the target week's progress is not submitted, update the progress as incomplete
                                        if (submission_status === "Working" || submission_status === "Pending") {
                                            console.log(`The week${i}'s progress is not submitted`);
                                            fetch(backend_path + '/submission/incomplete/' + project_id, {
                                                method: 'POST',
                                                credentials: 'include',
                                            })
                                            .then(response => response.json())
                                            .then(data => {
                                                console.log(`header.py update week${i}'s incomplete progress successfully:`, data);
                                            })
                                            .catch(error => console.error(`Error updating week${i}'s incomplete progress:`, error));
                                        } else {
                                            console.log(`The previous week${i}'s progress has already been updated`);
                                        }
                                    })
                                    .catch(error => console.error(`Error fetching target week${i} status:`, error));
                                }
                            }
                        })
                        .catch(error => console.error("Error fetching countdown:", error));
                    })
                    .catch(error => console.error("Error fetching project id:", error));
                }, 1000);
            });
        '''),
    )

