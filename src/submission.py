from fasthtml.common import *
from header import header_html
from footer import footer_html

def create_submission_page():
    return Html(
        Head(
            Title("Submission"),
            Link(rel="stylesheet", href="/static/style/style.css "),
            Link(rel="stylesheet", href="/static/style/submission.css"),
            Script(
                """
                function handleSubmit(event) {
                    event.preventDefault();  // Prevent the default form submission
                    const form = event.target;
                    const formData = new FormData(form);

                    fetch(form.action, {
                        method: form.method,
                        body: formData
                    })
                    .then(response => {
                        if (response.ok) {
                            window.location.href = "/confirmation";  // Redirect on success
                        } else {
                            alert("Submission failed. Please try again.");  // Show error message
                        }
                    })
                    .catch(() => {
                        alert("An error occurred. Please try again.");  // Show error message
                    });
                }
                """
            )
        ),
        Body(
                        header_html(), 

            Section(
                Div(
                    Img(src="/static/images/feedback/new_submissions.png", alt="back", _class="back"),
                    
                ),
                Div(
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
                    action="/submission",  # Set backend URL
                    method="post",  
                ),
                _class="submission-section"
            ),
            footer_html()
        )
                    

    )
