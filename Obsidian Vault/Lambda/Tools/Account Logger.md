# Account Logger
The account logger tool saves data like the follower counts, numbers of posts, accounts followed and biographies of target accounts into a database stored locally on the user's PC.

#### How to Use
- Open the **Account Logger** tab in the Lambda App
- Select `Add Account` from the sidebar and enter the account url
- Lambda should process the link and start logging the account

#### Accessing the Data
You can use a SQLite Browser to open the data stored by Lambda. The only readable data will be things like biographies and follower/following numbers. If you want to view content posted by the target please refer to the [[Content Gallery]]

#### Common Errors and Fixes
- "Account Name Not Found" / #0001
	- Fixable by making sure the link is a valid link in the format or by making sure the account actually exists. If the issue persists, try using a VPN.
- "Too Many Requests" / #0002
	- Fix this error by having **Only One** instance of Lambda open at a time. Using multiple instances can cause files to be corrupted and result in rate limiting by Instagram.
- "Error Writing To Database: Not Enough Space" / #0003
	- You can fix this by moving your account database to a different location. To do this open the `Settings` menu and select the `File/Folder` tab. You can then change the **Database Location** directory to somewhere else.
- "Thread Error: Account No Longer Exists" / #0004
	- This (usually) means the account you have been tracking has been removed from Instagram completely. If the account is still accessable from the browser try to use a VPN while using Lambda to avoid rate limiting.