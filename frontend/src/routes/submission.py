import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_submission_page():
    return Html(
        Head(
            Title("Submission"),
            Link(rel="stylesheet", href="../../static/style.css"),
        ),
        Body(
            header_html(),
            Section(
                Div(
                    Img(src="../../static/images/space_infinity_back.png", alt="back", _class="back"),
                    Img(src="../../static/images/submission.png", alt="submission", _class="submission")
                ),
                Form(
                    H2("Week 1", _class="weeks"),
                    P("Deadline: October 21st 11:59PM "),
                    Input(placeholder="[Project Name]", name="project_name", _class="project_input"),
                    Input(placeholder="[One liner]", name="one_liner", _class="liner_input"),
                    P("On a scale of 1 - 10, how's your progress?", _class="progress"),
                    Input(placeholder="[Progress]", name="progress_comment", _class="progress_input"),
                    Input(placeholder="[Upload files]", name="upload_link", _class="upload_input"),
                    Button("SUBMIT", type="submit", _class="submit"),
                    H3("Feeling stuck?", _class="stuck"),
                    action="http://127.0.0.1:8000/submission",
                    method="post",
                    target="hidden_iframe",
                ),
                _class="submission-section"
            ),

            # hidden iframe to handle the response
            Iframe(name="hidden_iframe", style="display:none;"),
            footer_html(),
        )
    )
