import ybc_app as a
import ybc_app_ui as u
import os
import time as t


s = u.Button(text='Shut Down',pos=[200,200])
r = u.Button(text='Restart',pos=[200,300])
b = u.Button(text='Back To Menu',pos=[200,400])
def shutdown():
    a.show_page('page6')
    f = open('data/sr.txt','w')
    f.write('s')
    f.close()
s.on_click = shutdown
def restart():
    a.show_page('page6')
    f = open('data/sr.txt','w')
    f.write('r')
    f.close()
r.on_click = restart
def back():
    a.show_page('page2')
b.on_click = back