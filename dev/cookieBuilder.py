import sys

cookie = sys.argv[1]
cookieString = "series.ly	TRUE	/	FALSE	1419020604	PHPSESSID	" + cookie
f = open('cookie.txt', 'w')
f.write(cookieString)
f.close()