# GSD
Google Spreadsheet Diff

This is a collection of scripts (bash and Python) that help automate and record the changes to a Google Spreadsheet.

The basic flow is that the Google Spreadsheet is accessed, read, and written to a CSV file.  The excellent csvdiff is then used to check for changes, and the changes are then appended to a changelog with timestamp.

You can use cron to automate this further. 

You will need to download/install the csvdiff file from here:  https://pypi.python.org/pypi/csvdiff

You will also need to enable the Google Drive API and get your service account setup.  I used this very nice guide by Chris Moffitt as a starting point for the Google stuff:  http://pbpython.com/pandas-google-forms-part1.html

Make sure you edit the appropriate areas of the scripts :)  As this was set up to be automated the script does not prompt the user for information.
