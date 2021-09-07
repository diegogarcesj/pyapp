from sys import path
path.append('/usr/local/www/nginx/pyapp/')

from cgi import parse_qs, escape
import default,biblio

def application(environ, start_response):
	query = environ['REQUEST_URI']
	querystr = environ['QUERY_STRING']
	d = parse_qs(querystr)
	q = escape(d.get('q', [''])[0])
	sa = escape(d.get('sa', [''])[0])
	st = escape(d.get('st', [''])[0])
	wa = escape(d.get('wa', [''])[0])
	wt = escape(d.get('wt', [''])[0])
	wu = escape(d.get('wu', [''])[0])
	if q.startswith('help'):
		output = default.home() + "<p>Welcome to nmarks-lml-LinkMetaLibrary</p><p>Help: all, search, write...</p>"
	elif q.startswith('all'):
		output = default.home() + biblio.readall() 
	elif q.startswith('search'):
		output = default.home() + default.search()
	elif q.startswith('write'):
		output = default.home() + default.write()
	elif (len(sa) > 0) | (len(st) > 0):
		output = default.home() + default.search() + biblio.search(sa,st)
	elif (len(wa) > 0) & (len(wt) > 0 & (len(wu) > 0)):
		output = default.home() + default.write() + biblio.write(wa, wt, wu)
	else:
		output = default.style() + default.home() + default.search() + biblio.readall()

	start_response('200 OK', [('Content-Type','text/html; charset: utf-8')])
	return output 
