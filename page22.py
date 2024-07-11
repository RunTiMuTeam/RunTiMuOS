import ybc_app as a
import ybc_app_ui as u
import ybc_sms as s
import random as r


q = u.Button(text='Back',pos=[50,50])
def quit1():
    a.show_page('page21')
q.on_click = quit1
code = u.Textarea(placeholder='Please enter verification code.',pos=[200,300])
code2 = a.get('code')
pn = a.get('pn')
v = u.Button(text='Verify',pos=[200,500])
def verify():
    global code,code2,pn,v
    if code.text == code2:
        f = open('data/id.txt','w')
        f.write(pn)
        f.close()
        f = open('data/idlogin.txt','w')
        f.write('True')
        f.close()
        v.text = 'Verification code is right.'
        quit()
    else:
        v.text = 'Verification code is not right.'