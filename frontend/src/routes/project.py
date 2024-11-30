from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_project_page():
    return Html(
        Head(
            Title("Project Page"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/project.css"),
        ),
        Body(
            header_html(), 
            Section(
                Div(
                    Img(src="/static/images/project/project.png",_class="project_img"),
                ),
                Div(
                    H1("Project Page", _class="project_titel"),
                    Input(placeholder="Project Name", _class="project_name"),
                    Input(placeholder="One Liner", _class="one_liner"),
                    P(
                      "One liner is a short summary of your goal. ",
                      A("Check Category Page", href="/category", _class="link"),
                        " for the examples.",_class="check"),
                    Input(placeholder=" Project Detail", _class="project_detail"),
                    _class="input_section"
                ),
                Div(
                   Button("SUBMIT",_class="submit") 
                ),

                _class="project_section"
            ),
            footer_html()
        ),
    )
           