from fasthtml.common import *

# Footer
def footer_html():
    return Footer(
        Div(
          Input(_type='text', placeholder='Type your email', _class='footer-input'),
          Button('Subscribe', _class='footer-button'),
          Div(
            Nav(
              Ul(
                Li(A('Home', href='/')),
                Li(A('About Us', href='/about')),
                Li(A('Submission', href='/submission')),
                Li(A('Progress Tracking', href='/progress-tracking')),
                Li(A('Login', href='/login'))
              ),
            ),  
            Div(
              P('Contact Us'), 
              P('tenatch10@gmail.com'),
              P('ONRamp, 100 College St.'),
              P('Toronto, ON Canada M5G1L5'),
              _class='footer-text'
            ),
            _class='footer-container02'
          ),
          _class='footer-container01'
        ),
        P('copyright@2024'),
    )

def footer_css():
    return Style('''
    footer {
      background-image:url(../../images/footer/footer_background.svg);
      padding: 10px 0;
    }
    .footer-container01 {      
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 30px auto;
      padding: 10px 20px;
    }
    .footer-container02 {
      display: flex;
      background-color: #FFFFFF;
      Nav{
        margin: 0;      
        Ul{
         padding: 0;
         li{
           list-style:none;
           a{
             font-size: 15px;
             font-weight: lighter;
             text-decoration: underline;
              color: #000000;
           }
         },
       }
      },
    }
    .footer-input {
      width: 200px;
      height: 30px;
      padding: 2px 5px;
      margin-right: 10px;
      border: 1px solid #FFFFFF;
    }
    .footer-text {
      margin: 10px 20px 0 0; 
      line-height: 0.3;
    }
    .footer-button {
      background-color: #000000;
      border: none;
      color: #FFFFFF;
      padding: 8px 20px;
      margin: 0 10px 0 0;
      text-align: center;
      text-decoration: none;
    }

    

    ''')
