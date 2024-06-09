import ybc_app as a
import ybc_app_ui as u
import os
import time as t


u.Text('RunTiMu',pos=[190,300],fontsize=45)
f = open('version/setup.txt','w')
f.write('False')
f.close()
s = u.Button(text='Start',pos=[200,625])
def start():
    a.show_page('page2')
s.on_click = start
