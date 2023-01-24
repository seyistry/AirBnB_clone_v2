#!/usr/bin/env bash
# Prepare your web servers

sudo apt-get update -y
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R $USER:$USER /data
sudo echo "<h1>Hello ALX!</h1>" > /data/web_static/releases/test/index.html

addLink="\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R $USER:$USER /data/web_static/current

sudo sed -i "25i\ $addLink" /etc/nginx/sites-available/default

sudo service nginx restart
sudo service nginx reload