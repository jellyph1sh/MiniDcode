#coding:utf-8
# --- SECTION IMPORT ---
# -- IMPORT TECH --
import cgi
import cgitb
# -- IMPORT PERS --
import includes.webtools as webtools
import includes.dcoding as dcoding
# -- IMPORT SYS  --
import sys
import codecs
import os

# --- SECTION MAIN ---
# -- ENCODAGE FR --
sys.stdout = codecs.getwriter("utf:-8")(sys.stdout.detach())
os.system('')
print("Content-type: text/html; charset=utf-8\n")

# -- HEADER TEMPLATES --
webtools.include('templates/fixe/header.html', 'Convertisseur')
webtools.include('templates/fixe/navigation.html', 'Convertisseur')

# -- MAIN PROG --
cgitb.enable()
form = cgi.FieldStorage()
alert, out, code, bsa, bsb = '', '', '', 'bsdec', 'bsasc'

if form.getvalue('valid') and form.getvalue('code') and form.getvalue('bsa') and form.getvalue('bsb'):
	code, bsa, bsb = form.getvalue('code'), form.getvalue('bsa'), form.getvalue('bsb')
	alert, out = dcoding.generalDcoding(code, bsa, bsb)
elif form.getvalue('valid'):
	if form.getvalue('bsa') and form.getvalue('bsb'):
		bsa, bsb = form.getvalue('bsa'), form.getvalue('bsb')
	alert = 'Entrez un nombre à convertir'

webtools.include('templates/content/converter.html', 'converter.py', code, out, alert)

# -- DYN SCRIPT --
webtools.scripts_include('scripts/conserve_selector.js', bsa, bsb)
webtools.scripts_include('scripts/reverse_button.js')

# -- FOOTER TEMPLATES --
webtools.include('templates/fixe/footer.html')