from fasthtml.common import *
from components.header import header_html, header_css
from routes.home import home_page
from routes.about import about_page
from routes.submission import submission_page
from routes.login import login_page

app, rt = fast_app()

# Home Page
@rt('/')
def home_page_handler():
    return home_page()

# About Page
@rt('/about')
def about_page_handler():
    return about_page()

# Submission Page
@rt('/submission')
def submission_page_handler():
    return submission_page()

# Login Page
@rt('/login')
def login_page_handler():
    return login_page()

serve()
