from fasthtml.common import *
from header import header_html
from footer import footer_html

def create_feedback_page():
    return Html(
        Head(
            Title("Feedback Page"),
            Link(rel="stylesheet", href="/static/style/style.css"),
            Link(rel="stylesheet", href="/static/style/feedback.css"),
        ),
        Body(
            header_html(), 
           
     Section(
         Div(
             Img(src="/static/images/feedback/backg.png",alt="feedback",_class="feedback"),
             
             Div(
             Img(src="/static/images/feedback/new_submissions.png",alt="new_submissions",_class="new_submissions"),
             ),

             Div(
                Input(placeholder="[Name]", _class="input-name"),
                Input(placeholder="[Project Name]", _class="input-project"),
                _class="input-container"

                ),
               
                Div(
                  Input(type="checkbox", _class="input-checkbox"),
                      Label(
                          "Leave feedback anonymously?",
                          Br(), 
                          "If yes, check the box",
                          _class="checkbox-label"
                      ),
                  _class="checkbox-container"
                ),

              
                  Div(
                      Label("What do you rate for their progress this week?", _class="rate-label"),
                      Div(
                          Input(type="radio", name="rating", value="1", id="rate1"),
                          Label("1", _for="rate1", _class="rate1-label"),
                          Input(type="radio", name="rating", value="2", id="rate2"),
                          Label("2", _for="rate2", _class="rate2-label"),
                          Input(type="radio", name="rating", value="3", id="rate3"),
                          Label("3", _for="rate3", _class="rate3-label"),
                          Input(type="radio", name="rating", value="4", id="rate4"),
                          Label("4", _for="rate4", _class="rate4-label"),
                          Input(type="radio", name="rating", value="5", id="rate5"),
                          Label("5", _for="rate5", _class="rate5-label"),
                          _class="rating-container"
                      )
                  ),
                  Div(
                     Label("How they can improve their project? Give them feedback.",_class="coment"),
                     Input(placeholder="", _class="coment-field"),

                  ),

         Div(
              Button("SUBMIT", _class="submit_btn"),
         ),
         _class="feedbuck_section"
     ),
     ),
     footer_html()
     ) 
    
    )