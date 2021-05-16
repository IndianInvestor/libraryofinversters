#!/Users/utpalkumar50/miniconda3/bin/python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# from pprint import pprint

# use creds to create a client to interact with the Google Drive API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

secret_cred_loc = (
    "/Users/utpalkumar50/GoogleDrive/earthinversion/POSTS-CODE/SubscriberInfo/"
)
creds = ServiceAccountCredentials.from_json_keyfile_name(
    secret_cred_loc + "secret_cred.json", scope
)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("EarthInversionSubscribers").sheet1

# Extract and print all of the values
data = sheet.get_all_records()

row = sheet.row_values(2)
col = sheet.col_values(2)

totalSubscribers = len(data)
print(totalSubscribers)

# pprint(data)

# pprint(row)
# pprint(col)