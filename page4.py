import ybc_app as a
import ybc_app_ui as u
import os
import time as t


u.Text(text='Version',pos=[100,100])
u.Text(text='4.0',pos=[300,100])
f = open('phone/model.txt','r')
model = f.read()
f.close()
'''
u.Text(text='Model',pos=[100,150])
u.Text(text=model,pos=[300,150])
'''
f = open('phone/i.txt','r')
inf = f.read()
inf = eval(inf)
f.close()
csz = 100
for i in inf:
    csz += 50
    u.Text(text=i,pos=[100,csz])
    u.Text(text=inf[i],pos=[300,csz])
r = u.Button(text='Back',pos=[50,50])
def return1():
    a.show_page('page3')
r.on_click = return1
