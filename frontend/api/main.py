import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src'))
from fasthtml.common import *
from routes.home import create_home_page
from routes.submission import create_submission_page
from routes.confirmation import create_confirmation_page
from routes.history import create_history_page
from routes.feedback import create_feedback_page
from routes.login import create_login_page
from routes.signup import create_signup_page
from routes.contact import create_contact_page
from routes.project import create_project_page
from routes.account import create_account_page
from routes.countdown import create_count_down_page

app, rt = fast_app()

@app.route("/")
def index():
    return create_home_page() 

@app.route("/submission/{project_id}")
def submission(project_id: str):
    return create_submission_page(project_id = project_id)

@app.route("/confirmation")
def confirmation():
    return create_confirmation_page()

@app.route("/history/{project_id}")
def history(project_id: str):
    return create_history_page(project_id = project_id)

@app.route("/feedback/{submission_id}")
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

@app.route("/account")
def account():
    return create_account_page()

@app.route("/countdown")
def countdown():
    return create_count_down_page()

serve()