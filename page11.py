import ybc_app_ui as u
import ybc_app as a


c = u.Button(text='Cancel',pos=[300,50])
def cancel():
    a.show_page('page10')
c.on_click = cancel
ddh = u.Textarea(placeholder='Please enter your esim ticket number.',pos=[200,300])
s = u.Button(text='Submit',pos=[200,400])
def submit():
    global ddh
    a.set('esim',ddh.text)
    a.show_page('page12')
s.on_click = submit
