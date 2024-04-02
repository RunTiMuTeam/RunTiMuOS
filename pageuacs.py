import ybc_app as a
import ybc_app_ui as u


u.Text(text='User Account Control',pos=[100,50])
u.Text(text='Do you want to allow this procedure to \nmake changes to your devices?',pos=[250,150])
u.Text(text='Procedure:Settings',pos=[200,450])
y = u.Button(text='Yes',pos=[200,500])
n = u.Button(text='No',pos=[200,600])
def yb():
    a.show_page('page3')
y.on_click = yb
def nb():
    a.show_page('page2')
n.on_click = nb