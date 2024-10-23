from fasthtml.common import Style

def global_css():
    return Style('''

    Body {
        font-family: 'Arial';
        margin: 0;
        padding: 0;
    }

    ''')
