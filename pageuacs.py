import ybc_app as a
import ybc_app_ui as u


f = open('data/uac_p.txt','r')
p = f.read()
f.close()
f = open('data/uac_pa.txt','r')
pa = f.read()
f.close()
f = open('data/uac_npa.txt','r')
npa = f.read()
f.close()
u.Text(text='User Account Control',pos=[100,50])
u.Text(text='Do you want to allow this procedure to \nmake changes to your devices?',pos=[250,150])
u.Text(text='Procedure:' + p,pos=[200,450])
y = u.Button(text='Yes',pos=[200,500])
n = u.Button(text='No',pos=[200,600])
def yb():
    global pa
    a.show_page(pa)
y.on_click = yb
def nb():
    global npa
    a.show_page(npa)
n.on_click = nb
