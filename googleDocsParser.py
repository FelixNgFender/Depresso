# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
#     http://www.apache.org/licenses/LICENSE-2.0
#
"""
Recursively extracts the text from a Google Doc.
"""

import os.path
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import prediction


def getIdFromUrl(url):
    # with open('the-zen-of-python.txt') as f:
    #     contents = f.read()
    # url = getIdFromUrl(contents)
    # url = 'https://docs.google.com/document/d/1W1zQptWSTjCS_EzvrMPFx-2jsh0Neqe5Ug3K8qquw2g/edit'

    if url.startswith("https://docs.google.com/document/d/"):
        id = url[35 : url.find("/", 35)]

    else:
        id = url

    if re.match("^([a-zA-Z0-9]|_|-)+$", id) is None:
        raise ValueError("url argument must be an alphanumeric id or a full URL")
    return id

def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')


def read_structural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be
            # nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_structural_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_structural_elements(toc.get('content'))
    return text


SCOPES = 'https://www.googleapis.com/auth/documents.readonly'
DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'
DOCUMENT_ID = None

def updateIdFromURL(url):
    global DOCUMENT_ID
    DOCUMENT_ID = getIdFromUrl(url)

def main():
    """Uses the Docs API to print out the text of a document."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('ExtensionReadingInputTest/token.json'):
        creds = Credentials.from_authorized_user_file('ExtensionReadingInputTest/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_582987600031-02pt483eljqito783ob7jrfak0923a13.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('ExtensionReadingInputTest/token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    doc_content = document.get('body').get('content')
    bodyoutput = read_structural_elements(doc_content)
    print(bodyoutput)
    print(prediction.predict(bodyoutput))


    # id_test = getIdFromUrl(
    #     'https://docs.google.com/document/d/1W1zQptWSTjCS_EzvrMPFx-2jsh0Neqe5Ug3K8qquw2g/edit?fbclid=IwAR1EXDDtx9L_Jz9VWeSiJW8bXS_lYBAm4415nkkylo21d2fImDPfNlwrb5k')

if __name__ == '__main__':
    main()
