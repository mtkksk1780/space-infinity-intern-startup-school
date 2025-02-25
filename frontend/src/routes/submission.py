import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_submission_page(project_id: str):
    endpoint = get_backend_path() + "/submission/project/" + project_id

    # Get project information from backend
    project_info = get_data(endpoint)

    # Extract project information
    project_name = project_info["name"]
    one_liner = project_info["one_liner"]
    deadline = project_info["deadline"]
    current_week = project_info["current_week"]

    return Html(
        Head(
            Title("Submission Page"),
            Base(href="/submission"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/submission.css"),
        ),
        Body(
            add_jquery(),
            get_session_info("/submission"),
            header_html(),
            Section(
                Div(
                    Img(src="/static/images/submission/backk.png", alt="back", _class="back"),
                ),
                Form(
                    get_form_attributes("/submission/complete/" + project_id),
                    H2("Week" + current_week, _class="weeks"),
                    P("Deadline:" + deadline),
                    Input(placeholder="[Project Name]", _class="project_input input-form", readonly=True, value=project_name),
                    Input(placeholder="[One liner]", _class="liner_input input-form", readonly=True, value=one_liner),
                    P("On a scale of 1 - 10, how’s your progress?", _class="progress"),
                    Input(placeholder="[Progress]", name="progress_comment", _class="progress_input input-form"),
                    Input(placeholder="[Upload files]", name="upload_link", _class="upload_input input-form"),
                    Button("CONFIRM", _class="submit confirm-btn"),
                    Button("SUBMIT", _class="submit disabled submit-btn"),
                    H3("Feeling stuck?", _class="stuck"),
                    H3("Check Category Page", _class="category"),
                    _class="input_section"
                ),
                _class="submission-section"
            ),
            add_sweet_alert(),
            footer_html(),
            disable_button(),
            confirm_form("None"),
            back_form(),
            submit_form("/submission", "None"),
        ),
    )
