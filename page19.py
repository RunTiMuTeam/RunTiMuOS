import ybc_app as a
import ybc_app_ui as u
import urllib.request as rq
import os


q = u.Button(text='Quit',pos=[50,50])
returnz = u.Textarea(placeholder='Please type the software name.',pos=[200,200])
i = u.Button(text='Install',pos=[200,500])
def install():
    global returnz,i
    c = returnz.text
    i.text = 'Checking'
    rq.urlretrieve('http://api.runtimu.com/apps/' + c + '/' + c + '.txt','cache/download/apps/' + c + '.txt')
    tf = os.listdir('cache/download/apps')
    if c + '.txt' not in tf:
        i.text = 'This app not found.'
    else:
        i.text = 'Downloading'
        f = open('cache/download/apps/' + c + '.txt','r')
        l = eval(f.read())
        f.close()
        for i2 in l:
            rq.urlretrieve('http://api.runtimu.com/apps/download/' + i2,i2)
        f = open('data/apps.txt','r')
        l2 = eval(f.read())
        f.close()
        rq.urlretrieve('http://api.runtimu.com/apps/open/' + c + '.txt','cache/download/open/' + c + '.txt')
        f = open('cache/download/open/' + c + '.txt','r')
        n2 = f.read()
        f.close()
        f = open('data/apps.txt','w')
        l2[c] = n2
        f.write(str(l2))
        f.close()
        i.text = 'Installed'
i.on_click = install
def quit1():
    a.show_page('page18')
q.on_click = quit1