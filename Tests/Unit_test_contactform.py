"""
This file is for testing the input allowance of the contact form. In this script the testing is done with unit testing.
For the correct input, regex is used to check if there is a correct input.

Author: Gea Bakker
Date 06-04-2025
Version 1.0

"""
import unittest
import re
from flask import Flask, request, render_template_string #importing the necessary modules

contact_template = """
<form method="POST">
    <input type="text" name="name" pattern="[A-Za-z-]{1,}"><br>
    <input type="email" name="email" pattern="[A-Za-z0-9-._]{1,}@[A-Za-z0-9-._]{1,}.[a-z]{2,}><br>
    <textarea name="message"></textarea><br>
    <button type="submit">Submit</button>
</form>
""" #a quick template to test the input

class ContactFormTest(unittest.TestCase):
    """
    A class for testing the contact form via unit testing.
    """
    def setUp(self):
        """
        To call the Flask app to make a route for the contact form.
        """
        self.app = Flask(__name__) #rename flask to self.app

        @self.app.route('/contact', methods=['GET', 'POST']) #creating the route app for the contact form
        def contact():
            """
            This function contains the code that will be tested. Regex will be used to check if the input is correct.
            :return: data check, contact_template
            """
            if request.method == 'POST': #this collects the information that the user sent
                name = request.form.get('name') #collects the name
                email = request.form.get('email') #collects the email
                message = request.form.get('message') #collects the message

                if not name or not email or not message: #checks if every item is filled
                    return "Invalid data", 400 #if not filled, it will return invalid data

                if not re.fullmatch(r'[A-Za-z-]{1,}', name): #checks if the name is real
                    return "Invalid data", 400 #if not a real name is entered, it will return invalid data

                if not re.fullmatch(r'[A-Za-z0-9-._]{1,}@[A-Za-z0-9-._]{1,}\.[a-z]{2,}', email): #checks if the email is real
                    return "Invalid data", 400 #if not a valid email, it will return invalid data

                return 'Success', 200 #if everything is correct it will return success

            return render_template_string(contact_template) #returns the filled in template and the corresponding code

        self.client = self.app.test_client() #returns the app route for further testing

    def test_get_contact_page(self):
        """
        In this function the post request is tested.

        :return: status code
        """
        response = self.client.get('/contact') #this collects the route made in the function contact()
        self.assertEqual(response.status_code, 200) #the true status code and the expected status code is compared
        self.assertIn(b'<form method="POST">', response.data) #the expected text and the data is given

    def test_post_valid_data(self):
        """
        This function gives the input for the function
        :return: status code
        """
        response = self.client.post('/contact', data={'name': 'John',
                                                      'email': 'john@example.com',
                                                      'message': 'Hello, world!'}) #information that will be given
        self.assertEqual(response.status_code, 200) #the true status code and the expected status code is compared
        self.assertIn(b'Success', response.data) #the expected text and the data is given

    def test_post_missing_data(self):
        """
        This function gives the input for the function
        :return: status code
        """
        response = self.client.post('/contact', data={'name': '',
                                                      'email': 'jane@example.com',
                                                      'message': 'Hi!'}) #information that will be given
        self.assertEqual(response.status_code, 400) #the true status code and the expected status code is compared
        self.assertIn(b'Invalid data', response.data) #the expected text and the data is given

    def test_post_invalid_email(self):
        """
        This function gives the input for the function
        :return: status code
        """
        response = self.client.post('/contact', data={'name': 'John',
                                                      'email': 'john',
                                                      'message': 'Hello, world!'}) #information that will be given
        self.assertEqual(response.status_code, 400) #the true status code and the expected status code is compared
        self.assertIn(b'Invalid data', response.data) #the expected text and the data is given

if __name__ == '__main__':
    unittest.main()
