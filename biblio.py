def readall():
	import sqlite3
	import sys
	
	db = sqlite3.connect('library.sqlite')
	cursor = db.cursor()
	cursor.execute('''SELECT * FROM books''')
	formated = ""
	for row in cursor:
		formated = formated + '{0}.- <b>{1} - <i>{2}</i></b><br /> <code><a href="{3}">{3}</a></code><br />'.format(row[0], row[1], row[2], row[3])
	db.close()
	return formated
def search(sa, st):
	import sqlite3
	import sys
	db = sqlite3.connect('library.sqlite')
	cursor = db.cursor()
	samod = '%' + sa + '%'
	stmod = '%' + st + '%'
	cursor.execute('''SELECT * FROM books WHERE author LIKE ? AND title LIKE ?''', (samod, stmod))
	formated = ""
	for row in cursor:
		formated = formated + '{0}.- <b>{1} - <i>{2}</i></b><br /> <code><a href="{3}">{3}</a></code><br />'.format(row[0], row[1], row[2], row[3])
	db.close()
	return formated
def write(wa, wt, wu):
	import sqlite3
	import sys
	db = sqlite3.connect('library.sqlite')
	cursor = db.cursor()
	cursor.execute('''INSERT INTO books (id, author, title, uri) VALUES (NULL, ?, ?, ?)''', (wa, wt, wu))
	db.commit()
	message = 'added:<br /><b>{0} - <i>{1}</i></b><br /> <code><a href="{2}">{2}</a></code><br />'.format(wa, wt, wu)
	db.close()
	return message