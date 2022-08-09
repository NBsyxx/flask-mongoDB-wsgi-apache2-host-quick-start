# flask-mongoDB-wsgi-apache2-host-quick-start
quick code&amp;configuration for setup virtualhosts

## Configurations 

FlaskApp.conf under etc/apache2/sites-available
FlaskApp.wsgi under var/www/FlaskApp/
makes it look like

         -FlaskApp.wsgi
FlaskApp-|
         -FlaskApp/__init__.py


## Hostings
1. log onto the server SSH

2: Download and Install Apache
- sudo apt update
- sudo apt install apache2
- apache2 -version

3: Configure Firewall
- sudo ufw app list
- sudo ufw allow 'Apache'

4: Configure apache
- sudo systemctl status apache 2  

5: Install and enable mod_wsgi 
-       sudo apt-get install libapache2-mod-wsgi-py3
-       for python2.X  use sudo apt-get install libapache2-mod-wsgi python-dev #

6: pip3
-       sudo apt-get install python3-pip 

7: Virtual Env
-       sudo pip3 install virtualenv
-       sudo virtualenv name_of_your_venv
-       source name_of_your_venv/bin/activate # activate 

8: Install flask & pymongo
-        sudo pip3 install Flask 
-        sudo pip3 install pymongo
-        sudo pip3 install -r /path/to/requirements.txt # other requirements

9: Restart apache
-      sudo service apache2 restart 

Ready! 




