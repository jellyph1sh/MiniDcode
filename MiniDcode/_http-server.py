#coding utf-8
import http.server
import random, time

def run():
    i, a = 0, random.randint(30, 35)
    loading = '|/-\\'
    for wait in range(a):
        i += 1
        print(f'\rWaiting server starting [{loading[i]}]', end='')
        if i == 3:
            i = -1
        time.sleep(0.1)
    print('\rServer start!\t\t\t\t')

port = 80				
address = ('', port)	

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler		
handler.cgi_directories = ['/']

httpd = server(address, handler)

text = """
                                         .#############* 
                            ///.         .#,          #* 
                         *(######/       .#,          #* 
                       /###,   .(##(.    .#,          #* 
                    ,###/         *##(*  .#,          #* 
    ,,,,,,,,,,,,,.  (##/.          *##(   *************. 
    #*          #*    /###,     .(##(.                   
    #*          #*      ,(##(.*###*          ....                *               (  
    #*          #*         (###(.        ,####((##.            (  `              )\ )           (     
    #*          #*                  ,####(*     ,##.           )\))(  (       ( (()/(           )\ )  (   
    #(((((((((((#((((((((((((*      ,##          *##(         ((_)()\ )\  (   )\ /(_))  (  (   (()/( ))\ 
    #*          #*          #/       *##/          (#(        (_()((_|(_) )\ |(_|_))_   )\ )\   ((_))((_)
    #*          #*          #/         (#/      /(###(        |  \/  |(_)_(_/((_)|   \ ((_|(_)  _| (_))
    #*          #*          #/          ##(/(###/.            | |\/| || | ' \)) || |) / _/ _ \/ _` / -_)
    #*          #*          #/           ,,,,                 |_|  |_||_|_||_||_||___/\__\___/\__,_\___|
    #####################################/               
    #*          #*          #/          #/               
    #*          #*          #/          #/               
    #* /#  ,#.  #* /#  ,#.  #/ *#  .#,  #/               
    #*          #*          #/          #/               
    (((((((((((((((((((((((((((((((((((((/               
"""

print(text)
run()
print('Please try to put \'http://localhost:80/index.py\' in your browser\nDevelopment server, please do not use it in production!')
print('#-------------------------------------------------LOGS-------------------------------------------------#')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('#------------------------------------------------------------------------------------------------------#')
    print('Bye!')
except:
    print('#------------------------------------------------------------------------------------------------------#')
    print('Server was interrupt strangely, please contact the site administrators: Sorgiati Sacha - Van Den Bosch Théo')