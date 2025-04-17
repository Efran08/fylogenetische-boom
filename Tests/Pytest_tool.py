"""
This file is for testing the input allowance of the tool input. In this script the testing is done with pytesting.
For the correct input,  is used to check if there is a correct input.

Author: Herke Wilts
Date 09-04-2025
Version 1.0
"""

import io
import pytest
from app import app

@pytest.fixture
def client():
    """
    Creates a Flask test client.
    Return: return_description
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_tool_get(client):
    """
    Test GET request loads the tool page successfully
    b turns the string into raw binary data (via ChatGPT). Because of this, no decoding HTML is necessary.
    """
    response = client.get('/tool')
    assert response.status_code == 200
    assert b'Entry for your phylogenetic tree' in response.data

def test_tool_post_valid_file(client):
    """
    Test POST with valid .fasta file and default options.
    """
    data = {
        'file': (io.BytesIO(b'>seq1\nACTG\n>seq2\nACTA'), 'example.fasta') # BytesIO simulates a file.
    }
    # follow redirects is necessary because the image is displayed on another HTML file.
    response = client.post('/tool', data=data, content_type='multipart/form-data', follow_redirects=True)
    assert response.status_code == 200 # Confirms valid upload
    assert b'/static/tree.png' in response.data # Checks valid filepath

def test_tool_post_invalid_file_type(client):
    """
    Test POST with unsupported file extension. The example used here is a .txt. Our supported filetypes include:
    * .fa(sta)
    * .phy(lip)
    """
    data = {
        'file': (io.BytesIO(b'Some random content'), 'badfile.txt')
    }
    # follow redirects is necessary because the image is displayed on another HTML file.
    response = client.post('/tool', data=data, content_type='multipart/form-data', follow_redirects=True)
    assert b'Invalid file type' in response.data or response.status_code in [400, 422]

def test_tool_post_missing_file(client):
    """Test POST with no file"""
    # follow redirects is necessary because the image is displayed on another HTML file.
    response = client.post('/tool', data={}, content_type='multipart/form-data', follow_redirects=True)
    assert response.status_code in [400, 422]