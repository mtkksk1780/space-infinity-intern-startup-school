from fasthtml.common import *
from header import header_html
from footer import footer_html
from home import create_home_page
from submission import create_submission_page
from confirmation import create_confirmation_page
from history import create_history_page
from feedback import create_feedback_page
from login import create_login_page
from signup import create_signup_page

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



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
