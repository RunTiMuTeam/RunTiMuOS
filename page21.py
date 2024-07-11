import ybc_app as a
import ybc_app_ui as u
import ybc_sms as s
import random as r


q = u.Button(text='Quit',pos=[50,50])
def quit1():
    a.show_page('page3')
q.on_click = quit1
f = open('data/idlogin.txt','r')
state = eval(f.read())
f.close()
if state:
    f = open('data/id.txt','r')
    rid = f.read()
    f.close()
    u.Text(text=rid,pos=[200,300])
    out = u.Button(text='Logout',pos=[200,500])
    def rout():
        global out
        f = open('data/id.txt','w')
        f.write('')
        f.close()
        f = open('data/idlogin.txt','w')
        f.write('False')
        f.close()
        out.text = 'Logout Successfully'
        quit()
    out.on_click = rout
else:
    p = u.Textarea(placeholder='Please enter your phone number.',pos=[200,300])
    c = u.Button(text='Get Verification Code',pos=[200,500])
    def getcode():
        global p
        code = r.randint(111111,999999)
        s.sms(p.text,"[RunTiMu]Verification code " + str(code) + " is valid within 5 minutes.Please don't divulge to others.")
        a.set('pn',p.text)
        a.set('code',str(code))
        a.show_page('page22')
    c.on_click = getcode
