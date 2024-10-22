import requests
from fasthtml.common import *
from components.header import header_html, header_css


def home_page():
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Home Page'),
            header_css(),
            home_page_css()
        ),
        Body(
            header_html(),
            Div(
                Img(src='../../images/home/home01.svg', alt='home01', _class='full-width-image'),
                Div(
                    H1('Unleash creativity,'),
                    H1('expand your'),
                    H1('potential to infinity.'),
                    Button(
                        'Join Now',
                        _class='button',
                    ),
                    _class='container02'
                ),
                _class='container01'
            ),
            Div(
                H1('4 Weeks'),
                H1('Develop Your Idea'),
                H1('Launch'),
                _class='container03'
            ),
            Img(src='../../images/home/home02.svg', alt='home02', _class='full-width-image'), 
            Div(
                H1('Welcome to Space Infinity!'),   
                Div(
                    P('Launch your creativity, develop bold ideas, and transform visions into reality with our four-week program designed to push boundaries. Inspired by the vast cosmos and Bulidspace community, Space Infinity connects you with a community that fuels your growth.'),
                    Img(src='../../images/home/home03.svg', alt='home03', _class='half-width-image'),
                    _class='container05',
                ),    
                _class='container04',
            ),
            Hr(_class='horizontal-line'),
            Div(
                H1('Schedule'),
                Div(
                    Div(
                        H2('1st week', style ='color: #E11F2E;'),
                        H3('Pitch Ideas'),
                        P('Decide what your goals are'),
                        _class='container08',
                    ),
                    Div(
                        H2('2nd week', style ='color: #F5BC18;'),
                        H3('Develop your ideas'),
                        P('Develop your project & Get/give feedback from fellow participants'),
                        _class='container08',
                    ),    
                    _class='container07',
                ),
                Div(
                    Div(
                        H2('3rd week', style ='color: #2C699D;'),
                        H3('Prepare for launch'),
                        P('Develop your project & Start preparing the launch'),
                        _class='container08',
                    ), 
                    Div(
                        H2('4th week', style ='color: #008753;'),
                        H3('Launch your project'),
                        P('Learn from other participants’ projects'),
                        _class='container08',
                    ),
                    _class='container07',
                ),

                _class='container06',
            ),

        )
    )

def home_page_css():
    return Style('''

    Body {
        font-family: 'Arial';
        margin: 0;
        padding: 0;
    }

    .container01 {
        width: 100%;
        position: relative;
    }

    .container02 {
        width: 35%;
        position: absolute;
        top:300px;
        left:40px;
        margin:0 0 0 20px;
        background-color: orange;
    }

    .container03 {
        display: flex;
        justify-content: space-around;
        margin-top: 50px;
        font-size: 25px;
    }

    .container04 {
        margin: 0 50px 0 50px;
        text-align: left;
        font-size: 40px;

        p {
            font-size: 30px;
            line-height: 1.5;
            margin: 0 0 20px 0;
        }
    }

    .container05 {
        display: flex;
        justify-content: space-around;
        text-align: left;

        p {
            font-size: 30px;
            line-height: 1.5;
            margin: 0 0 20px 0;
        }

        img {
            margin: 0 0 0 40px;
        }
    }

    .container06 {
        margin: 0 50px 0 50px;
        text-align: left;
        font-size: 30px;

        p {
            font-size: 30px;
            line-height: 1.5;
            margin: 0 0 20px 0;
        }
    }

    .container07 {
        display: flex;
        justify-content: space-around;
    }

    .container08 {
        width: 45%;
        margin: 20px 50px 20px 50px;
        border: 5px solid black;
        border-radius: 50px;
        text-align: center;
    }

    .full-width-image {
        width: 100%;
        height: auto;
        margin: 0 0 30px 0;
    }

    .half-width-image {
        width: 50%;
        height: auto;
        margin: 0 0 30px 0;
    }

    .button {
        background-color: #2C699D;
        border: none;
        color: white;
        padding: 14px 40px;
        margin: 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
    }

    .horizontal-line {
        width: 90%;
        height: 1px;
        background-color: #000000;
        border: none;
    }
    ''')
