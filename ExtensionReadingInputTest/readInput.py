#Install this
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Importing the HTTP library
import requests as req

# Requesting for the website
page = req.get('https://docs.google.com/document/d/1W1zQptWSTjCS_EzvrMPFx-2jsh0Neqe5Ug3K8qquw2g/edit?fbclid=IwAR1EXDDtx9L_Jz9VWeSiJW8bXS_lYBAm4415nkkylo21d2fImDPfNlwrb5k')
soup = BeautifulSoup(page.content, 'html.parser')

# Creating a BeautifulSoup object and specifying the parser

# Using the prettify method
print(soup.get(35))
