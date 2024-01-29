# SSL_check
Python script to check all your website  ssl expiry and send and email 

Use pycharm or add the file directly to your server.



cd /srv/
mkdir ssl
chmo 755 ssl 

crontab -e 

add the time for the  ssl to run  include file location and python 

example 

python /srv/ssl/ssl.py 
