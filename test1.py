#!/usr/local/bin/python3

print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''<!DOCTYPE html>
<html>
<head>

	<title>web1 - home</title>
	<meta charset="utf-8">
</head>
<body>
	<h1><a href="test1.py">WEB</a></h1>
	 <ol>
		 <li><a href="test1.py?id=HTML">HTML</a></li>
		 <li><a href="test1.py?id=CSS">CSS</a></li>
		 <li><a href="test1.py?id=JavaScript">JavaScript</a></li>
	 </ol>
</body>
</html>
'''.format(title=pageId))