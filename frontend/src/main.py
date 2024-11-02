from fasthtml.common import *
from routes.home import create_home_page
from routes.about import create_about_page
from routes.submission import create_submission_page
from routes.login import create_login_page

app, rt = fast_app()

# Home Page
@rt("/")
def index():
    return create_home_page()

# About Page
@rt("/about")
def about():
    return create_about_page()

# Submission Page
@rt("/submission")
def submission():
    return create_submission_page() 

# Login Page
@rt("/login")
def login():
    return login_page()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)

serve()
