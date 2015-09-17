from __future__ import print_function
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import csv

SCOPE = ["https://spreadsheets.google.com/feeds"]

####  !!CHANGE THESE TWO VARIABLES!! ####
SECRETS_FILE = "service_account_file_from_google.json"
SPREADSHEET = "The Name of Your Spreadsheet" ### Remember to share it with the Google Service Account!!

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)

gc = gspread.authorize(credentials)

############
#
## Shows Accessible Spreadsheets - Good for Troubleshooting/Checking Access##
#print("The following sheets are available")
#for sheet in gc.openall():
#    print("{} - {}".format(sheet.title, sheet.id))
#
############

workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1
data = sheet.get_all_values()
tempfilename = 'temp.csv'

with open (tempfilename, 'wb') as f:
  for line in data:
    print(line, file=f) 


## There is definitely a more efficient way of doing this, but it is clear and easy to change

filename = 'newsheet.csv'
with open (tempfilename, 'r') as f:
  with open(filename, "wb") as wf:
    data=f.read()
    data=data.replace("[", "")
    data=data.replace("]", "")
    data=data.replace("'", "")
    data=data.replace(", ", ",")
    wf.write(data)
