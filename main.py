from fasthtml.common import *
app, rt = fast_app()

def common_header():
    return Header(
        Nav(
            A('About Us', href='/about'),
            A('Submission', href='/submission'),
            A('Feedback', href='/feedback')
        )
    )

def common_css():
    return Style('''
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
      background-color: #F8F8F8;
      border-bottom: 1px solid #ccc;
    }
    nav {
      display: flex;
      justify-content: center;
      margin-top: 20px;
    }
    nav a {
      margin: 0 30px;
      text-decoration: none;
      color: #333;
      font-weight: bold;
      font-size: 24px;
    }
    nav a:hover {
      color: #007BFF;
    }
    @media (max-width: 768px) {
      nav a {
        margin: 0 10px;
        font-size: 18px;
      }
    }
    ''')

# Home Page
@rt('/')
def get():
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Space Infinity'),
            common_css()
        ),
        Body(
            common_header(),
            H1('Welcome to Space Infinity')
        )
    )

# About Page
@rt('/about')
def about_page():
    return Html(
        Head(
            Title('About Us'),
            common_css()
        ),
        Body(
            common_header(),
            H1('About Us'),
        )
    )

# Submission Page
@rt('/submission')
def submission_page():
    return Html(
        Head(
            Title('Submission'),
            common_css()
        ),
        Body(
            common_header(),
            H1('Submission Page')
        )
    )

# Feedback Page
@rt('/feedback')
def feedback_page():
    return Html(
        Head(
            Title('Feedback'),
            common_css()
        ),
        Body(
            common_header(),
            H1('Feedback Page')
        )
    )

serve()
