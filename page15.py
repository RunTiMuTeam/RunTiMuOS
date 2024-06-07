import ybc_app as a
import ybc_app_ui as u


f = open('data/newesim.txt','r')
tf = eval(f.read())
f.close()
q = u.Button(text='Quit',pos=[50,50])
def quit1():
    a.show_page('page2')
q.on_click = quit1
if tf:
    u.Button(text='Bind phone number to your eSIM',pos=[200,200])