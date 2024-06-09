import ybc_app as a
import ybc_app_ui as u


f = open('phone/esim.txt','r')
esim_dictory = eval(f.read())
f.close()
esim_list = []
q = u.Button(text='Quit',pos=[300,50])
def quit1():
    a.show_page('page10')
q.on_click = quit1
if esim_dictory == {}:
    u.Text(text="You didn't added eSIM!",pos=[200,600])
else:
    for i in esim_dictory:
        esim_list.append(i)
    es = u.Textarea(placeholder="Please enter you need remove eSIM's phone number!\nIf remove done,RunTiMuOS shut down,after that you should start RunTiMuOS.",pos=[200,200])
    rm = u.Button(text='Remove',pos=[200,400])
    def remove1():
        global es,esim_list,esim_dictory
        if es.text in esim_list:
            esim_dictory.pop(es.text)
            f = open('phone/esim.txt','w')
            f.write(str(esim_dictory))
            f.close()
            rm.text = 'Remove Done.'
            f = open('data/sr.txt','w')
            f.write('s')
            f.close()
            a.show_page('page6')
        else:
            u.Text(text="This phone number not in your device!",pos=[200,500])
    rm.on_click = remove1
