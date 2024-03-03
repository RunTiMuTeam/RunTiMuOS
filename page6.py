import ybc_app as a
import ybc_app_ui as u


u.Text('RunTiMu',pos=[190,300])
f = open('data/sr.txt','r')
sr = f.read()
f.close()
if sr == 'r':
    u.Text('Restarting...',pos=[200,375])
    u.Text('Exiting Desktop...',pos=[200,400])
    u.Text('Exiting Service...',pos=[200,425])
    u.Text('Disabling Application...',pos=[200,450])
    u.Text('Done.',pos=[200,475])
    a.show_page('page0')
else:
    u.Text('Restarting...',pos=[200,375])
    u.Text('Exiting Desktop...',pos=[200,400])
    u.Text('Exiting Service...',pos=[200,425])
    u.Text('Disabling Application...',pos=[200,450])
    u.Text('Done.',pos=[200,475])
    u.Text('You can safely close the window.',pos=[200,500])