from fasthtml.common import *

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.home import create_home_page

from routes.submission import create_submission_page

from routes.confirmation import create_confirmation_page

from routes.history import create_history_page

from routes.feedback import create_feedback_page

from routes.login import create_login_page

from routes.signup import create_signup_page

from routes.contact import create_contact_page

from routes.project import create_project_page

app, rt = fast_app()

@app.route("/")
def index():
    return create_home_page() 

@app.route("/submission")
def submission():
    return create_submission_page()  

@app.route("/confirmation")
def confirmation():
    return create_confirmation_page()

@app.route("/history")
def history():
    return create_history_page()

@app.route("/feedback")
def feedback():
    return create_feedback_page()

@app.route("/login")
def login():
    return create_login_page()

@app.route("/signup")
def signup():
    return create_signup_page()


@app.route("/contact")
def contact():
    return create_contact_page()

@app.route("/project")
def project():
    return create_project_page()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)