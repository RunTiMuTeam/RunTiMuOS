import ybc_app as a
import ybc_app_ui as u
import os
import time as t


f = open('data/nm.txt','r')
nm = eval(f.read())
f.close()
f = open('data/language.txt','r')
language = f.read()
f.close()
l_v = 'Version'
if language == 'zh-CN':
    l_v = '版本'
u.Text(text=l_v,pos=[100,100])
u.Text(text='7.1Beta1',pos=[300,100])
if nm:
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
if nm:
    for i in inf:
        csz += 50
        u.Text(text=i,pos=[100,csz])
        u.Text(text=inf[i],pos=[300,csz])
else:
    u.Text(text='Mode',pos=[100,csz + 50])
    u.Text(text='Safe Mode',pos=[300,csz + 50])
r = u.Button(text='Back',pos=[50,50])
def return1():
    a.show_page('page3')
r.on_click = return1