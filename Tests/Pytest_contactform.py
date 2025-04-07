"""
This file is for testing the input allowance of the contact form. In this script the testing is done with pytesting.
For the correct input, regex is used to check if there is a correct input.

Author: Gea Bakker
Date 06-04-2025
Version 1.0

"""

import pytest #import the used modules
import re
from flask import Flask, request, render_template_string

contact_template = """  
<form method="POST">
    <input type="text" name="name" pattern="[A-Za-z-]{1,}" required><br>
    <input type="email" name="email" pattern="[A-Za-z0-9-._]{1,}@[A-Za-z0-9-._]{1,}\.[a-z]{2,} required><br>
    <textarea name="message" required></textarea><br>
    <button type="submit">Submit</button>
</form>
""" #made a template based on the parameters that are in the contact_page.html

@pytest.fixture #add the code that needs testing
def app():  #to call Flask for a test route
    """
    This function calls on FLask to create a test route.

    :return: app
    """
    app = Flask(__name__)

    @app.route('/contact', methods=['GET', 'POST']) #making a specific route for the contact form
    def contact():
        """
        This function makes the contact form based on the template made above. In this function the input is created
        and checked. For the input, regex is used to check if there is a correct input.
        :return: data check, contact_template
        """
        if request.method == 'POST': #when the user posts the name, email and message will be sent and collected by this code
            name = request.form.get('name') #this collects the name
            email = request.form.get('email') #this collects the email
            message = request.form.get('message') #this collects the message

            if not name or not email or not message: #to check if every item is filled by the user
                return "Missing data", 401 #if a space is left empty invalid data will show

            if not re.fullmatch(r'[A-Za-z]+(-[A-Za-z]+)?', name): #to check the user put in a real name
                return "Invalid data", 400 #if not a real name, invalid data will show

            if not re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
                return "Invalid data", 400 #if not a real emailaddress, invalid data will show

            return 'Success', 200 #if all the data is correct, success will be shown
        return render_template_string(contact_template) #returning the contact_template

    return app #returning the app route

@pytest.mark.parametrize('name, email, message, expected', [
    ('John','john@example.com', 'Hello, world!', 200),
    ('', 'jane@example.com','Hi!', 401),
    ('', '', '', 401),
    ('John','john', 'Hello, world!', 400),
    ('-John-', 'john@example.com', 'Hello!', 400),
    ('John', 'invalid@', 'Hello!', 400)
]) #testing data for the code

def test_templates(app, name, email, message, expected):
    """
    Executing the test.
    :param app:
    :param name:
    :param email:
    :param message:
    :param expected:
    :return: None
    """
    client = app.test_client() #calling the app route
    response = client.post('/contact', data={
        'name': name,
        'email': email,
        'message': message
    }) #calling the contact form
    assert response.status_code == expected #checking if the found outcome is the same as the expected (given) outcome

