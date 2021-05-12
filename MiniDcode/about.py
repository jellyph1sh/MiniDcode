#coding:utf-8
# --- SECTION IMPORT ---
# -- IMPORT TECH --
import cgi
# -- IMPORT PERS --
import includes.webtools as webtools
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
webtools.include('templates/fixe/header.html', 'À propos')
webtools.include('templates/fixe/navigation.html', 'À propos')

# -- MAIN PROG -- 
webtools.include('templates/content/about.html')

# -- FOOTER TEMPLATES --
webtools.include('templates/fixe/footer.html')