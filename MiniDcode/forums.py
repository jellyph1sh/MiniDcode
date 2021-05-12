#coding:utf-8
# --- SECTION IMPORT ---
# -- IMPORT TECH --
import cgi
import cgitb
# -- IMPORT PERS --
import includes.webtools as webtools
import includes.commdb as commdb
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
webtools.include('templates/fixe/header.html', 'Forum')
webtools.include('templates/fixe/navigation.html', 'Forum')

# -- MAIN PROG -- 
cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('forum'):
    forum_name = form.getvalue('forum')
    messages = commdb.getmessages('db/base.db', forum_name)
    if '[ERROR]' in messages:
        print(f'<h2>Le forum "{forum_name}" n\'existe pas !</h2>')
    else:
        print(f'<h2>FORUM : {forum_name}</h2>')
        print(f"""<form action="cmdforum.py" method="POST">
            <input type="hidden" name="does" value="message" />
            <input type="hidden" name="forum" value="{forum_name}" />
            <p><label for="pseudo">Pseudonyme : </label><input type="text" name="pseudo" value="" /></p>
            <p><label for="message">Message : </label><textarea name="message" value=""></textarea></p>
            <button type="submit">VALIDER</button>
        </form>""")
        if '[WARN]' in messages:
            print(f'<p>{messages[1]}</p>')
        else:
            render = []
            for message in messages:
                render.append(f'{message[2]} ({message[1]}) : {message[3]}')
            print('<p>'+'</p><hr><p>'.join(render[::-1])+'</p>')
    print('<a href="forums.py">Retourner aux forums</a>')
else:
    print("""<form action="cmdforum.py" method="POST">
        <input type="hidden" name="does" value="forum" />
        <p><label for="forum">Nom du forum : </label><input type="text" name="forum" value="" /></p>
        <p><label for="topic">Sujet : </label><input type="text" name="topic" value="" /></p>
        <button type="submit">VALIDER</button>
    </form>""")
    print('<h2>FORUM DISPONIBLE : </h2>')
    forums = commdb.getforums('db/base.db')
    if not '[ERROR]' in forums:
        for forum in forums:
            name, nb_mess = forum[1], forum[2]
            print(f'<p><a href="forums.py?forum={name}">{name} ({nb_mess} messages)</a></p>')
    else:
        print('<p>Aucun forums disponnible pour le moment...</p>')

# -- FOOTER TEMPLATES --
webtools.include('templates/fixe/footer.html')