import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_submission_page():
    return Html(
        Head(
            Title("Submission"),
            Link(rel="stylesheet", href="/static/styles/style.css "),
            Link(rel="stylesheet", href="/static/styles/submission.css"),
        ),
        Body(
            header_html(), 
            Section(
                Div(
                    Img(src="/static/images/feedback/new_submissions.png", alt="back", _class="back"),
                ),
                Form(
                    get_form_attributes("/submission/complete/{project_id}"),
                    H2("Week 1", _class="weeks"),
                    P("Deadline: October 21st 11:59PM "),
                    Input(placeholder="[Project Name]", _class="project_input"),
                    Input(placeholder="[One liner]", _class="liner_input"),
                    P("On a scale of 1 - 10, how’s your progress?", _class="progress"),
                    Input(placeholder="[Progress]", _class="progress_input"),
                    Input(placeholder="[Upload files]", _class="upload_input"),
                    Button("SUBMIT", type="submit", _class="submit"),
                    H3("Feeling stuck?", _class="stuck"),
                    H3("Check Category Page", _class="category"),
                ),
                _class="submission-section"
            ),
            add_jquery(),
            get_session_info(),
            add_sweet_alert(),
            footer_html(),
            submit_form("/submission", "None"),
            clear_form(),
        ),
    )
