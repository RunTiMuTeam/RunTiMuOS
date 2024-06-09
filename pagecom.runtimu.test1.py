import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Quit',pos=[50,50])
u.Text(text="Hello World!",pos=[200,300])
def quit1():
    a.show_page('page18')
q.on_click = quit1