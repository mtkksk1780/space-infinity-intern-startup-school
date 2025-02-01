from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_history_page(project_id: str):
    endpoint = get_backend_path() + "/history/" + project_id

    # Get history data from backend
    history_data = get_data(endpoint)

    # Extract project information
    project_info = history_data["project_info"]
    project_name = project_info["name"]
    one_liner = project_info["one_liner"]
    project_detail = project_info["description"]

    # Extract submission history
    submission_history = history_data["submission_history"]

    # Store submission and feedback data in dictionary
    weeks_data = {}
    submission = {}
    feedback = {}

    for i in range(min(len(submission_history), 4)):
        week = submission_history[i]
        week_key = f"week{i+1}"
        submission[week_key] = {
            "notes": week["progress_comment"],
            "url": week["output_url"],
            "feedback": week["feedback"]
        }
        print("submission for Week:", week_key, submission[week_key])

        feedback_list = week["feedback"]
        feedback[week_key] = []
        for f in feedback_list:
            feedback[week_key].append({
                "user_name": f["user_name"],
                "evaluation_rate": f["evaluation_rate"],
                "evaluation_comment": f["evaluation_comment"],
                "is_anonymous": f["is_anonymous"]
            })
            print("Organized Feedback for Week:", week_key, feedback[week_key])

    return Html(
        Head(
            Title("History"),
            Base(href="/history"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            Link(rel="stylesheet", href="/static/styles/history.css")
        ),
        Body(
            add_jquery(),
            get_session_info("/history"),
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
                        Input(placeholder="Enter project name", _class="project-field", readonly=True, value=project_name),
                        _class="input-row"
                    ),
                    Div(
                        Label("One liner -", _class="liner"),
                        Input(placeholder="Enter one liner", _class="liner-field", readonly=True, value=one_liner),
                        _class="input-row"
                    ),
                    Div(
                        Label("Project detail -", _class="detail"),
                        Input(placeholder="Enter project detail", _class="detail-field", readonly=True, value=project_detail),
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
                    Input(placeholder="Enter notes", _class="note-field", readonly=True, value=submission["week1"]["notes"]),
                    _class="input-row"
                ),
                Div(
                    Label("Output URL -", _class="url"),
                    Input(placeholder="[URL]", _class="url-field", readonly=True, value=submission["week1"]["url"]),
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
                    Label("Notes -", _class="notes"),
                    Input(placeholder="Enter notes", _class="note-field", readonly=True, value=submission["week2"]["notes"]),
                    _class="input-row"
                ),
                Div(
                    Label("Output URL -", _class="url"),
                    Input(placeholder="[URL]", _class="url-field", readonly=True, value=submission["week2"]["url"]),
                    _class="input-row"
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
                    Label("Notes -", _class="notes"),
                    Input(placeholder="Enter notes", _class="note-field", readonly=True, value=submission["week3"]["notes"]),
                    _class="input-row"
                ),
                Div(
                    Label("Output URL -", _class="url"),
                    Input(placeholder="[URL]", _class="url-field", readonly=True, value=submission["week3"]["url"]),
                    _class="input-row"
                ),
                Div(
                    Div(
                        Button("Check Feedback", _class="feedback3"),
                    ),
                ),
                Div(
                    H3("Week 4",_class="week4"),
                ),
                Div(
                    Img(src="/static/images/history/box.png", alt="box",_class="box4"),
                ),
                Div(
                    Label("Notes -", _class="notes"),
                    Input(placeholder="Enter notes", _class="note-field", readonly=True, value=submission["week4"]["notes"]),
                    _class="input-row"
                ),
                Div(
                    Label("Output URL -", _class="url"),
                    Input(placeholder="[URL]", _class="url-field", readonly=True, value=submission["week4"]["url"]),
                    _class="input-row"
                ),
                Div(
                    Div(
                        Button("Check Feedback", _class="feedback4"),
                    ),
                ),
                _class="input-container"
            ),
            _class="history-section"    
        ),
        footer_html(),
    ),
