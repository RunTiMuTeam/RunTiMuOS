import ybc_app as a
import ybc_app_ui as u


u.Text(text='Erase all?',pos=[200,200])
yes = u.Button(text='Yes',pos=[200,500])
no = u.Button(text='No',pos=[200,550])
def y():
    f = open('version/setup.txt','w')
    f.write('True')
    f.close()
    quit()
yes.on_click = y
def n():
    a.show_page('page3')
no.on_click = n
