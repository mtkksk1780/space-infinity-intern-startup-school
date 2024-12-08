from fasthtml.common import *

# This file is for storing utility functions that can be reused in multiple components

# Get form attributes
def get_form_attributes(path: str):
    attributes = {
        "action": "http://127.0.0.1:8000" + path,
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
            // Prevent default form submission
            event.preventDefault();

            // Collect form data
            const form = $(this).closest('form');
            const formData = new FormData(form[0]);

            // Define redirectPath from Python
            const redirectPath = '{redirect_path}' === 'None' ? null : '{redirect_path}';

            // Debugging
            console.log("form", form); 
            console.log("form.action", form.attr('action')); 
            console.log("form.method", form.attr('method')); 
            console.log("redirectPath", redirectPath);

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
