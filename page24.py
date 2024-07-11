import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Back',pos=[50,50])
def quit1():
    a.show_page('pageuacs')
q.on_click = quit1
u.Text(text="Error:Scan face couldn't\n help you open app!",pos=[200,300])