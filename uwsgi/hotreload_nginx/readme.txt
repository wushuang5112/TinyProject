# uwsgi小应用，利用uwsgi来实现web开发程
# 麻雀虽小

cd /source/path/
uwsgi --ini mysite.ini
uwsgi --reload uwsgi.pid
uwsgi --stop uwsgi.pid

带源码热启动


