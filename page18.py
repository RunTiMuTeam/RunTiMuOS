import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Quit',pos=[50,50])
i = u.Button(text='App Store',pos=[200,100])
f = open('data/apps.txt','r')
l = eval(f.read())
f.close()
o = u.Textarea(placeholder='Please enter your software name.',pos=[200,250])
bo = u.Button(text='Open',pos=[200,400])
def lbo():
    global o
    a.show_page(l[o.text][:-3])
bo.on_click = lbo
def li():
    f = open('data/uac.txt','r')
    tf = f.read()
    f.close()
    if tf:
        f = open('data/uac_p.txt','w')
        f.write('App Store')
        f.close()
        f = open('data/uac_pa.txt','w')
        f.write('page19')
        f.close()
        f = open('data/uac_npa.txt','w')
        f.write('page18')
        f.close()
        a.show_page('pageuacs')
    else:
        a.show_page('page19')
i.on_click = li
def quit1():
    a.show_page('page2')
q.on_click = quit1