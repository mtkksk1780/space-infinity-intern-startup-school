import json
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_feedback_page():
    endpoint = get_backend_path() + "/feedback"

    # Get all active submissions
    submission_data = get_data(endpoint)
    print("feedback.py submission_data:", submission_data)

    # Convert submission_data to JSON string
    submission_data_json = json.dumps(submission_data)

    return Html(
        Head(
            Title("Feedback Page"),
            Base(href="/feedback"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/feedback.css"),
        ),
        Body(
            add_jquery(),
            get_session_info("/feedback"),
            header_html(),
            Section(
                Div(
                    Img(src="/static/images/feedback/backk.png", alt="feedback", _class="feedback"),
                    Div(
                        Img(src="/static/images/feedback/new_submissions.png", alt="new_submissions", _class="new_submissions"),
                    ),
                    Div(
                        Input(placeholder="[Name]", _class="input-name"),
                        Input(placeholder="[Project Name]", _class="input-project"),
                        _class="input-container list"
                    ),
                    Div(
                        Input(type="checkbox", _class="input-checkbox"),
                        Label(
                            "Leave feedback anonymously?",
                            Br(),
                            "If yes, check the box",
                            _class="checkbox-label"
                        ),
                        _class="checkbox-container"
                    ),
                    Div(
                        Label("What do you rate for their progress this week?", _class="rate-label"),
                        Div(
                            Input(type="radio", name="rating", value="1", id="rate1"),
                            Label("1", _for="rate1", _class="rate1-label"),
                            Input(type="radio", name="rating", value="2", id="rate2"),
                            Label("2", _for="rate2", _class="rate2-label"),
                            Input(type="radio", name="rating", value="3", id="rate3"),
                            Label("3", _for="rate3", _class="rate3-label"),
                            Input(type="radio", name="rating", value="4", id="rate4"),
                            Label("4", _for="rate4", _class="rate4-label"),
                            Input(type="radio", name="rating", value="5", id="rate5"),
                            Label("5", _for="rate5", _class="rate5-label"),
                            _class="rating-container"
                        )
                    ),
                    Div(
                        Label("How they can improve their project? Give them feedback.", _class="coment"),
                        Input(placeholder="", _class="coment-field"),
                    ),
                    Div(
                        Button("CONFIRM", _class="submit confirm-btn"),
                        Button("SUBMIT", _class="submit disabled submit-btn"),
                    ),
                    _class="feedbuck_section"
                ),
            ),
            add_sweet_alert(),
            footer_html(),
            disable_button(),
            confirm_form("None"),
            back_form(),
            submit_form("/feedback", "None"),
            Script(f'''
                const submissions = JSON.parse('{submission_data_json}');
                console.log("feedback.py submissions:", submissions);

                // Create ul and li elements based on the number of submissions
                // Display User Name and Project Name in the submission list
                const list = document.querySelector('.list');
                submissions.forEach(submission => {{
                    const {{submission_id, user_name, project_name}} = submission; 
                    const li = document.createElement('li');
                    // Set submission_id as a link
                    li.innerHTML = `<a href="/feedback/${{submission_id}}">${{user_name}} - ${{project_name}}</a>`;
                    list.appendChild(li);
                }});
            ''')
        ),
    )