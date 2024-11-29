from fasthtml.common import *

# This file is for storing utility functions that can be reused in multiple components

# Get form attributes
def get_form_attributes(path: str, target: str = None):
    attributes = {
        "action": "http://127.0.0.1:8000" + path,
        "method": "post",
    }
    # Add target attribute if it exists
    if target:
        attributes["target"] = target
    return attributes

# Add iframe
def add_iframe():
    return Iframe(name="response_iframe", style="display:block; border:none;", _class="response_iframe")

# Add jQuery
def add_jquery():
    return Script(src="https://code.jquery.com/jquery-3.6.0.min.js")

# Clear form input field
def clear_form():
    return Script("""
        $(document).ready(function() {
            $('.submit-btn').click(function() {
                setTimeout(function() {
                    $('.input-form').val('');
                }, 50);
            });
        });
    """)

