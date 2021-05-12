#coding:utf-8
# --- SECTION IMPORT ---
# -- IMPORT TECH --
import cgi
import cgitb
# -- IMPORT PERS --
import includes.webtools as webtools
import includes.commdb as commdb
import time
# -- IMPORT SYS  --
import sys
import codecs
import os

# --- SECTION MAIN ---
# -- ENCODAGE FR --
sys.stdout = codecs.getwriter("utf:-8")(sys.stdout.detach())
os.system('')
print("Content-type: text/html; charset=utf-8\n")

# -- MAIN PROG -- 
cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('does'):
    if form.getvalue('does') == 'message':
        if form.getvalue('forum') and form.getvalue('pseudo') and form.getvalue('message'):
            commdb.putmessage('db/base.db', form.getvalue('forum'), (time.time(), form.getvalue('pseudo'), form.getvalue('message')))
    elif form.getvalue('does') == 'forum':
        if form.getvalue('forum'):
            print(commdb.startforum('db/base.db', form.getvalue('forum')))

    print(f"""
    <script>document.location.href="forums.py?forum={form.getvalue('forum')}"</script>
    """)

print(f"""
<script>document.location.href="forums.py"</script>
""")