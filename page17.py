import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Quit',pos=[50,50])
u.Text(text="User(now):Administrator\nROOT:No",pos=[200,300])
def quit1():
    a.show_page('page3')
q.on_click = quit1