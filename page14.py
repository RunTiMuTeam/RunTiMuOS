import ybc_app as a
import ybc_app_ui as u


f = open('data/language.txt','r')
language = f.read()
f.close()
l_q = 'Quit'
l_t1 = "You didn't added eSIM!"
l_ph1 = "Please enter you need remove eSIM's phone number!\nIf remove done,RunTiMuOS shut down,after that you should start RunTiMuOS."
l_rm = 'Remove'
l_rm2 = 'Remove Done.'
l_t2 = "This phone number not in your device!"
if language == 'zh-CN':
    l_q = '退出'
    l_t1 = '你没有添加过eSIM'
    l_ph1 = '请输入你需要删除的eSIM的手机号码\n如果删除完成，RunTiMuOS将会关机，然后你需要去启动RunTiMuOS'
    l_rm = '删除'
    l_rm2 = '删除完成'
    l_t2 = '这个手机号码不在你的设备里'
f = open('phone/esim.txt','r')
esim_dictory = eval(f.read())
f.close()
esim_list = []
q = u.Button(text=l_q,pos=[300,50])
def quit1():
    a.show_page('page10')
q.on_click = quit1
if esim_dictory == {}:
    u.Text(text=l_t1,pos=[200,600])
else:
    for i in esim_dictory:
        esim_list.append(i)
    es = u.Textarea(placeholder=l_t2,pos=[200,200])
    rm = u.Button(text=l_rm,pos=[200,400])
    def remove1():
        global es,esim_list,esim_dictory
        if es.text in esim_list:
            esim_dictory.pop(es.text)
            f = open('phone/esim.txt','w')
            f.write(str(esim_dictory))
            f.close()
            rm.text = l_rm2
            f = open('data/sr.txt','w')
            f.write('s')
            f.close()
            a.show_page('page6')
        else:
            u.Text(text=l_t2,pos=[200,500])
    rm.on_click = remove1
