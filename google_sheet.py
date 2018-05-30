import gspread
from oauth2client.service_account import ServiceAccountCredentials

#為了記錄到spreadsheet
def auth_gss_client(path, scopes):
	credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
	return gspread.authorize(credentials)
def update_sheet(gss_client, key, item,the_day):
	wks = gss_client.open_by_key(key)
	sheet = wks.sheet1
	sheet.insert_row([item,the_day], 2)
def find_user_period(gss_client, key, userid):
	wks = gss_client.open_by_key(key)
	sheet = wks.sheet1
	try:
		cell = sheet.find(userid)
		r = cell.row
		c = cell.col
		period_day = sheet.cell(r,c+1).value
		print('hihihihihi')
		print(period_day)
		return period_day
	except:
		return 0