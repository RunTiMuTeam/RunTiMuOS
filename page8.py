import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Quit',pos=[300,50])
b = u.Button(text='Disable User Account Control(Not Recommended)',pos=[200,300])
m = u.Button(text='Enable User Account Control',pos=[200,400])
def bz():
    f = open('data/uac.txt','w')
    f.write('False')
    f.close()
b.on_click = bz
def mz():
    f = open('data/uac.txt','w')
    f.write('True')
    f.close()
m.on_click = mz
def quit1():
    a.show_page('page3')
q.on_click = quit1
