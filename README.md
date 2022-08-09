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
1. log onto the server

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
-       sudo apt-get install libapache2-mod-wsgi python-dev

6:  Creating flask app
-       cd /var/www 
-       sudo mkdir webApp
-       cd webApp

7: Install flask
-        sudo apt-get install python-pip 
-        sudo pip install Flask 
-        sudo pip install flask_sqlalchemy

9: Restart apache
-      sudo service apache2 restart 

Ready! 




