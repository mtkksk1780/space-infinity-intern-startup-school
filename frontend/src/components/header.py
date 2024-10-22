from fasthtml.common import *

# Header
def header_html():
    return Header(
        Div(
          A(
            Img(src='../../images/logo.svg', alt='Home Page'),
            href='/'
          ),
          _class='logo'
        ),
        Nav(
          A('Home', href='/'),
          A('About Us', href='/about'),
          A('Submission', href='/submission'),
          A('Login', href='/login')
        )
    )


def header_css():
    return Style('''
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
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
