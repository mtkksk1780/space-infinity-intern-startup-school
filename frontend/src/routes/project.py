from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_project_page(project_id: str):

    print("create_project_page project_id:", project_id)

    return Html(
        Head(
            Title("Project Page"),
            Base(href="/project"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/project.css"),
        ),
        Body(
            add_jquery(),
            get_session_info("/project"),
            header_html(),
            Section(
                Form(
                    get_form_attributes("/project"),
                    Div(
                        Img(src="/static/images/project/projectt.png", _class="project_img"),
                    ),
                    Div(
                        H1("Project Page", _class="project_title"),
                        Input(placeholder="Project Name", name="project_name", _class="project_name input-form"),
                        Input(placeholder="One Liner", name="one_liner", _class="one_liner input-form"),
                        P(
                            "One liner is a short summary of your goal. ",
                            A("Check Category Page", href="/category", _class="link"),
                            " for the examples.", _class="check"
                        ),
                        Input(placeholder="Project Detail", name="description", _class="project_detail input-form"),
                        _class="input_section"
                    ),
                    Div(
                        Button("CONFIRM", _class="submit confirm-btn"),
                        Button("SUBMIT", _class="submit disabled submit-btn"),
                    ),
                    
                    _class="project_section form_section"
                ),
            ),
            add_sweet_alert(),
            footer_html(),
            disable_button(),
            confirm_form(project_id),
            back_form(),
            submit_form("/project", "/"),
        ),
    )
     