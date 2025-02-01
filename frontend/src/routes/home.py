import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html
from components.utils import *

def create_home_page():
    return Html(
        Head(
            Title("Home Page"),
            Base(href="/"),
            Link(rel="stylesheet", href="/static/styles/style.css"),
            # Link(rel="stylesheet", href="/static/styles/home.css"),
            Link(rel="stylesheet", href="/static/images/home/backk.png"),
        ),
        Body(
            add_jquery(),
            get_session_info("/"),
            header_html(), 
            Section(
                Div(
                    Img(src="/static/images/home/backk.png",_class="hero-img"),
                    Div(
                        Button("Join Now", _class="join_btn"),
                        _class="hero-content"
                    ),
                    _class="hero-section"
                )
            ),
            # Section(
            #     Div(
            #         H2("4 Weeks", _class="week"),
            #         H2("Develop Your Idea", _class="develop_your_idea"),
            #         H2("Launch", _class="launch"),
            #         _class="steps-section"
            #     )
            # ),
            # Section(
            #     Div(
            #         Div( 
            #             P("Launch your creativity, develop bold ideas, and transform visions into reality with our four-week program designed to push boundaries. Inspired by the vast cosmos and Buildspace community, Space Infinity connects you with a community that fuels your growth.", _class="creativity"),
            #             _class="welcome-text"
            #         ),    
            #         _class="welcome-container"
            #     ),
            # ),
            # Section(
            #     Div(
            #         Div(
            #             H2("1st Week"),
            #             H3("Pitch Ideas"),
            #             P("Decide what your goals are.")
            #         ),
            #         Div(
            #             H2("2nd Week"),
            #             H3("Develop your ideas"),
            #             P("Develop your project & Get/give feedback from fellow participants"),
            #         ),
            #         Div(
            #             H2("3rd Week"),
            #             H3("Prepare for launch"),
            #             P("Develop your project & start preparing.")
            #         ),
            #         Div(
            #             H2("4th Week"),
            #             H3("Launch your project"),
            #             P("Learn from other participants' projects.")
            #         ),
            #         _class="schedule-container"
            #     ),
                # _class="home-section"
            # ),
            footer_html() 
        ),  
    )
