from __future__ import print_function

import os.path
import google.auth

from google.oauth2.credentials      import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow      import InstalledAppFlow

from googleapiclient.discovery      import build
from googleapiclient.errors         import HttpError


SAMPLE_SPREADSHEET_ID = '1FuTG3zZP1dtjgCAHCAVBFC62HHEJaI_M8chbSkqI9x0'
SAMPLE_RANGE_NAME = 'A1:B10'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_creds():
    try:
        creds = None

        flow = InstalledAppFlow.from_client_secrets_file(
            '/home/art/git/poc/gcp/sheets_api/credentials.json'
            , SCOPES)
                
        creds = flow.run_local_server(port=0)
        return creds

    except Exception as e:
        print( 'get_creds: {}'.format( e ) )
        raise


def update_values( spreadsheet_id, range_name, value_input_option,
                  values ):
    try:
        creds = get_creds()
        service = build('sheets', 'v4', credentials=creds)

        #values = [
        #    [
        #        # Cell values ...
        #    ],
        #    # Additional rows ...
        #]

        body = {
            'values': values
        }
        
        result = service.spreadsheets().values().update(
            spreadsheetId    = spreadsheet_id, 
            range            = range_name,
            valueInputOption = value_input_option, 
            body             = body ).execute()
        
        print( result )



    except Exception as e:
        print( 'write(), error: {}'.format( e ) )

if __name__ == '__main__':
    # Pass: title

    values = [ ['A', 'B'],
               ['C', 'D']
             ]

    update_values( SAMPLE_SPREADSHEET_ID
                  , 'A15:C16'
                  
                  , 'RAW'
                  #, 'USER_ENTERED'

                  , values

                  )

    print( '\n\n look the Gatojazz Dictionary Google Sheets \n\n ' )