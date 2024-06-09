import ybc_app as a
import ybc_app_ui as u


u.Text('RunTiMu',pos=[190,300],fontsize=45)
f = open('data/language.txt','r')
language = f.read()
f.close()
l_y = 'You can safely close the window.'
if language == 'zh-CN':
    l_y = '你可以安全的关闭这个窗口了'
f = open('data/sr.txt','r')
sr = f.read()
f.close()
def restart():
    a.show_page('page0')
if sr == 'r':
    restart()
else:
    '''
    u.Text('Shutting down...',pos=[200,375])
    u.Text('Exiting Desktop...',pos=[200,400])
    u.Text('Exiting Service...',pos=[200,425])
    u.Text('Disabling Application...',pos=[200,450])
    u.Text('Done.',pos=[200,475])
    '''
    quit()#u.Text(l_y,pos=[200,500])