import ybc_app_ui as u
import ybc_app as a


ns = u.Text(text="Your device doesn't support SIM.",pos=[200,100])
esim = u.Button(text='Set up eSIM',pos=[200,200])
rm = u.Button(text='Remove eSIM',pos=[200,300])
r = u.Button(text='Back',pos=[50,50])
start = 400
f = open('phone/esim.txt','r')
dictory = eval(f.read())
f.close()
if dictory != {}:
    for i in dictory:
        u.Text(text=dictory[i] + '\n' + i,pos=[200,start])
        start += 50
def return1():
    a.show_page('page3')
r.on_click = return1
def setupesim():
    a.show_page('page11')
esim.on_click = setupesim
def remove1():
    a.show_page('page14')
rm.on_click = remove1
