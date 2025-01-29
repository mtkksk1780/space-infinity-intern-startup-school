from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html

def create_history_page():
    return Html(
        Head(
            Title("History"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/history.css")
        ),
        Body(
            header_html(),
            Section(
                Div(
                    Img(src="/static/images/history/historyy.png", alt="history", _class="history"),
                    Img(src="/static/images/history/box.png", alt="box",_class="box"),
                    Div(
                        H3("Your project",_class="your_project"),
                    ),
                    Div(
                        Label("Project name -", _class="project"),
                        Input(placeholder="Enter project name", _class="project-field"),
                        _class="input-row"
                    ),
                    Div(
                        Label("One liner -", _class="liner"),
                        Input(placeholder="Enter one liner", _class="liner-field"),
                        _class="input-row"
                    ),
                    Div(
                        Label("Project detail -", _class="detail"),
                        Input(placeholder="Enter project detail", _class="detail-field"),
                        _class="input-row"
                    ),
                    _class="input-container"
                ),
                Div(
                    H3("Week 1",_class="week"),
                ),
                Div(
                    Img(src="/static/images/history/box.png", alt="box2",_class="box2"),
                ),
                Div(
                    Label("Notes -", _class="notes"),
                    Input(placeholder="Enter notes", _class="note-field"),
                    _class="input-row"
                ),
                Div(    
                    Input(placeholder="[URL]", _class="url-field"),
                    _class="input-row"
                ),
                Div(
                    Button("Check Feedback", _class="feedback"),
                ),
                Div(
                    H3("Week 2",_class="week2"),
                ),
                Div(
                    Img(src="/static/images/history/box.png", alt="box",_class="box3"),
                ),
                Div(
                    Div(
                        Button("Check Feedback", _class="feedback2"),
                    ),
                ),
                Div(
                    H3("Week 3",_class="week3"),
                ),
                Div(
                    Img(src="/static/images/history/box.png", alt="box",_class="box4"),
                ),
                Div(
                    Div(
                        Button("Check Feedback", _class="feedback3"),
                    ),
                ),
                _class="input-container"
            ),
            _class="history-section"    
        ),
        footer_html()
    ),
    


    