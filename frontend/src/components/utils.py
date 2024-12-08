import requests
from fasthtml.common import *

# This file is for storing utility functions that can be reused in multiple components

# Get history data from backend
def get_data(endpoint: str):
    print("endpoint:", endpoint)
    try:
        response = requests.post(endpoint)
        print("utils.py get_data response:", response.json())
        return response.json()
    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except Exception as error:
        print(f"An error occurred: {error}")
    return {"error": "Failed to fetch data"}

# Get endpoint path for backend
def get_endpoint_path():
    return "http://127.0.0.1:8000"

# Get form attributes
def get_form_attributes(path: str):
    backend = get_endpoint_path() 
    attributes = {
        "action": backend + path,
        "method": "post",
    }
    print("get_form_attributes:", attributes)
    return attributes

# Add iframe
# def add_iframe():
#     return Iframe(name="response_iframe", style="display:block; border:none;", _class="response_iframe")

# Add jQuery
def add_jquery():
    return Script(src="https://code.jquery.com/jquery-3.6.0.min.js")

# Add SweetAlert
def add_sweet_alert():
    return Script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11")

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

# Submit form
def submit_form(redirect_path: str):
    return Script(f"""
        function resultAlert(message, type, redirectPath) {{
            Swal.fire({{
                title: message,
                icon: type,
            }}).then((result) => {{
                if (result.isConfirmed && redirectPath) {{
                    setTimeout(function() {{
                        window.location.href = redirectPath;
                    }}, 500);
                }}
            }});
        }}

        $('.submit-btn').on('click', function(event) {{
            event.preventDefault();

            const form = $(this).closest('form');
            const formData = new FormData(form[0]);
            const redirectPath = '{redirect_path}' === 'None' ? null : '{redirect_path}';

            // Send data to the server using FormData
            fetch(form.attr('action'), {{
                method: form.attr('method'),
                body: formData,
            }})
            .then(response => response.json())
            .then(data => {{
                console.log("Response from server:", data);
                const result = data.result;
                const message = data.message;
                if (result) {{
                    // Show alert and redirect after confirmation
                    resultAlert(message, 'success', redirectPath);
                }} else {{
                    resultAlert(message, 'error', null);
                }}
            }})
            .catch(error => {{
                console.error('Error:', error);
                const message = "An error occurred while submitting the form.";
                resultAlert(message, 'error', null);
            }});
        }});
    """)
