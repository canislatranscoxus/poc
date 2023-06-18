from __future__ import print_function

import os.path
import google.auth

from google.oauth2.credentials      import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow      import InstalledAppFlow

from googleapiclient.discovery      import build
from googleapiclient.errors         import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_creds():
    try:

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # If there are no (valid) credentials available, let the user log in.
        '''if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    #'credentials.json'
                    '/home/art/git/poc/gcp/sheets_api/credentials.json'
                    , SCOPES)
                
                creds = flow.run_local_server(port=0)
        '''


        flow = InstalledAppFlow.from_client_secrets_file(
            #'credentials.json'
            '/home/art/git/poc/gcp/sheets_api/credentials.json'
            , SCOPES)
                
        creds = flow.run_local_server(port=0)
        return creds

    except Exception as e:
        print( 'get_creds: {}'.format( e ) )
        raise

def create(title):
    """
    Creates the Sheet the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
        """
    
    #creds, _ = google.auth.default()
    
    creds = get_creds()

    # pylint: disable=maybe-no-member

    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                    fields='spreadsheetId') \
            .execute()
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    # Pass: title
    create( "gato_sheet01" )
    print( '\n\n look in Google Sheets, you must have a new spreadSheet \n\n ' )