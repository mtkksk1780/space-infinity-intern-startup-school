import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_submission_page():
    return Html(
        Head(
            Title('Submission'),
            Link(rel="stylesheet", href="/static/style.css"),
        ),
        Body(
            header_html(),
            Section(
                Div(
                    Img(src="../../static/images/space_infinity_back.png", alt="back", _class="back"),
                    Img(src="../../static/images/submission.png", alt="submission", _class="submission")
                ),
                Div(
                    H2("Week 1", _class="weeks"),
                    P("Deadline: October 21st 11:59PM "),
                    Input(placeholder="[Project Name]", _class="project_input"),
                    Input(placeholder="[One liner]", _class="liner_input"),
                    P("On a scale of 1 - 10, how’s your progress?", _class="progress"),
                    Input(placeholder="[Progress]", _class="progress_input"),
                    Input(placeholder="[Upload files]", _class="upload_input"),
                    Button("SUBMIT", _class="submit"),
                    H3("Feeling stuck?", _class="stuck")
                ),
                _class="submission-section"
            ),
            footer_html(),
        )
    )
