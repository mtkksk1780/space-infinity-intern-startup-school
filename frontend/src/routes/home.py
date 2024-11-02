import requests
from fasthtml.common import *
from components.header import header_html
from components.footer import footer_html


def create_home_page():
    return Html(
        Head(
            Title("Home Page"),
            Link(rel="stylesheet", href="/static/style.css"),
        ),
        Body(
            header_html(),
            Section(
                Div(
                    Img(src="../../static/images/space_infinity_banner.png", alt="Hero Image", _class="hero-img"),
                    Img(src="../../static/images/possibilities.png", alt="The Possibilities Are Endless",_class="possibility-img"),
   
                    Div(  
                        Button("Join Now", _class="join_btn"),
                        _class="hero-content"
                    ),
                    _class="hero-section"
                )
            ),

            Section(
                Div(
                    H2("4 Weeks", _class="week"),
                    H2("Develop Your Idea", _class="develop_your_idea"),
                    H2("Launch", _class="launch"),
                    _class="steps-section"
                )
            ),

            Section(
                Div(
                    Div(
                        Img(src="../../static/images/develop_idea.png", alt="Develop Your Idea", _class="step-img")
                    ),
                    _class="develop-section"
                )
            ),

            Section(
                Div(
                    Img(src="../../static/images/welcome.png", alt="Welcom", _class="welcome-img")
                ),
                _class="welcome-space"
            ),
            
            Section(
                Div(
                    Div(
                       
                        P("Launch your creativity, develop bold ideas, and transform visions into reality with our four-week program designed to push boundaries. Inspired by the vast cosmos and Buildspace community, Space Infinity connects you with a community that fuels your growth.", _class="creativity"),
                        _class="welcome-text"
                    ),
                    Div(
                        Img(src="../../static/images/layer_3.png", alt="Welcome Image",_class="laer_3"),
                       
                        Img(src="../../static/images/isolation_mode.png", 
                        alt="isolation Image",_class="isolation"),
                       
                        Img(src="../../static/images/layer_1-2.png",alt="small_star",_class="small_star"),
                        Img(src="../../static/images/layer_1-3.png",alt="large_star",_class="large_star"),
                        Img(src="../../static/images/layer_1.png",alt="red_circle",_class="red_circler"),
                        _class="welcome-image"
                    ),
                    _class="welcome-container"
                )
            ),

            Section(
                Img(src="../../static/images/schedule.png",alt="schedule",_class="schedule"),

                Div(
                    Div(
                        H2("1st Week"),
                        H3("Pitch Ideas"),
                        P("Decide what your goals are.")
                    ),
                    Div(
                        H2("2nd Week"),
                        H3("Develop your ideas"),
                        P("Develop your project & Get/give feedback from fellow participants")
                    ),
                    Div(
                        H2("3rd Week"),
                        H3("Prepare for launch"),
                        P("Develop your project & start preparing.")
                    ),
                    Div(
                        H2("4th Week"),
                        H3("Launch your project"),
                        P("Learn from other participants' projects.")
                    ),
                    _class="schedule-container"
                )
            ),
            footer_html(),
        )
    )