#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get install -y python-pip
sudo apt-get install libffi-dev -y
sudo pip install django
sudo apt-get install python-dev -y
sudo apt-get install libmysqlclient-dev -y
sudo pip install -r /projects/req.txt
sudo apt-get install apache2 -y 