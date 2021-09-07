def home():
	formulario = "<code><form action='../pyapp/' method='get'>\
	<input type='text' name='q' autofocus/>\
	<input type='submit' value='run'/></form></code>"
	return formulario
def search():
	formulario = "<code><form action='../pyapp/' method='get'>\
	<input type='text' name='sa' value='author' autofocus/><br />\
	<input type='text' name='st' value='title' >\
	<input type='submit' value='search'/></form></code>"
	return formulario
def write():
	formulario = "<code><form action='../pyapp/' method='get'>\
	<input type='text' name='wa' value='author' autofocus/><br />\
	<input type='text' name='wt' value='title'>\
	<label>URI: </label><input type='text' name='wu'>\
	<input type='submit' value='write'/></form></code><br />"
	return formulario
def style():
	estilo = "<body>"
	return estilo