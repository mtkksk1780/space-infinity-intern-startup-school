import requests
from fasthtml.common import *
from time import sleep

# Get endpoint path for frontend
def get_frontend_path():
    return "http://127.0.0.1:5001"

# Get endpoint path for backend
def get_backend_path():
    return "http://127.0.0.1:8000"

# Get session data from the server
def get_session_info(source_path: str):
    return Script("""
        // Get session ID from cookies
        function getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        }
        const source_path = '""" + source_path + """';
        const session_id = getCookie('session_id');

        if (!session_id && source_path !== '/login') {
            // Redirect to login page if session ID is not found
            window.location.href = '/login';
        }

        // Fetch session data from the server
        fetch('http://127.0.0.1:8000/get-user-cookie/' + session_id, {
            method: 'POST',
            credentials: 'include',
        })
        .then(response => response.json())
        .then(data => {
            console.log("Session data:", data);
            const { role, user_id, user_name } = data.user_data;

            // Add form and hidden input fields
            const hiddenUserFieldsForHeader = `
                <input type="hidden" id="user_id" name="user_id" value="${user_id}">
                <input type="hidden" id="user_name" name="user_name" value="${user_name}">
            `;
            $('.header-container').append(hiddenUserFieldsForHeader);

            const hiddenUserFields = `
                <input type="hidden" name="role" value="${role}">
                <input type="hidden" name="user_id" value="${user_id}">
            `;
            $('.form_section').append(hiddenUserFields);

            // Display logged-in user
            $(document).ready(function() {
                if ($('#user_name').val() != undefined) {
                    $('.logged-in').text('Logged in: ' + $('#user_name').val());
                }
            });
        })
        .catch(error => console.error("Error fetching session data:", error));        
    """)


# Get data from backend
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

# Get form attributes
def get_form_attributes(path: str):
    backend = get_backend_path() 
    attributes = {
        "action": backend + path,
        "method": "post",
    }
    print("get_form_attributes:", attributes)
    return attributes

# Add jQuery
def add_jquery():
    return Script(src="https://code.jquery.com/jquery-3.6.0.min.js")

# Add SweetAlert
def add_sweet_alert():
    return Script(src="https://cdn.jsdelivr.net/npm/sweetalert2@11")

# Clear form input field
# def clear_form():
#     return Script("""
#         $(document).on('click', '.submit-btn', function() {
#             // $('.submit-btn').click(function() {
#                 setTimeout(function() {
#                     $('.input-form').val('');
#                 }, 50);
#         });
#     """)

# Confirm form
def confirm_form():
    return Script(f"""
        $(document).on('click', '.confirm-btn', async function(event) {{
            event.preventDefault();

            // Check if all fields are filled
            let allFieldsFilled = true;
            $('.input-form').each(function() {{
                if ($(this).val().trim() === '') {{
                    allFieldsFilled = false;
                    return false;
                }}
            }});
            if (!allFieldsFilled) {{
                await Swal.fire({{
                    title: 'Please fill in all required fields.',
                    icon: 'error',
                }});
                return;
            }}

            // Show confirmation message
            Swal.fire({{
                title: "Please confirm all inputs are correct before submitting.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Confirm",
                cancelButtonText: "Back",
            }}).then((result) => {{
                const isConfirmed = result.isConfirmed;
                if (isConfirmed) {{
                    // Change the class name from confirm-btn to submit-btn
                    $(this).removeClass('confirm-btn').addClass('submit-btn');
                    // Change the button text from CONFIRM to SUBMIT
                    $('.submit-btn').text('SUBMIT');
                    // Add "BACK" button in the form section
                    $('.input_section').append('<button class="submit-tentative back-btn">BACK</button>');
                }}
            }});
        }});
    """)

# Go back to the previous button
def back_form():
    return Script("""
        $(document).on('click', '.back-btn', function(event) {{
            event.preventDefault();
            // Delete BACK button
            $('.back-btn').remove();
            // Change the class name from submit-btn to confirm-btn
            $('.submit-btn').removeClass('submit-btn').addClass('confirm-btn');
            // Change the button text from SUBMIT to CONFIRM
            $('.confirm-btn').text('CONFIRM');
        }});
    """)

# Submit form
def submit_form(source_path: str, redirect_path: str):
    return Script(f"""
        function resultAlert(data, type, sourcePath, redirectPath) {{
            const message = data.message;
            Swal.fire({{
                title: message,
                icon: type,
            }}).then((result) => {{
                // Store session in cookies
                if (sourcePath === '/login') {{
                    const session_id = data.session_id;
                    document.cookie = `session_id=${{session_id}}`;
                }}
                // Redirect to the source page
                if (result.isConfirmed && redirectPath) {{
                    setTimeout(function() {{
                        window.location.href = redirectPath;
                    }}, 500);
                }}
            }});
        }}

        $(document).on('click', '.submit-btn', function(event) {{
            event.preventDefault();

            const form = $(this).closest('form');
            const formData = new FormData(form[0]);
            const sourcePath = '{source_path}';
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

                // Show alert message            
                if (result) {{
                    resultAlert(data, 'success', sourcePath, redirectPath);
                    // Clear input fields
                    setTimeout(function() {{
                        $('.input-form').val('');
                    }}, 50);
                }} else {{
                    resultAlert(data, 'error', sourcePath, null);
                }}
            }})
            .catch(error => {{
                console.error('Error:', error);
                const message = "An error occurred while submitting the form.";
                resultAlert(message, 'error', null);
            }});
        }});
    """)
