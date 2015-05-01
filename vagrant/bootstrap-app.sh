#!/usr/bin/env bash

yellow='\e[0;33m'
red='\e[0;31m'
NC='\e[0m' # No Color

#Setup the Database

cd /vagrant

echo 'export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/usr/local/mysql/lib"' >> ~/.profile

echo "create user 'shuffle'@'localhost' identified by 'shuffle';" | mysql -uroot -pvagrant
echo "create database shuffle DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;" | mysql -uroot -pvagrant
echo "grant all privileges on *.* to 'shuffle'@'localhost' with grant option;" | mysql -uroot -pvagrant

echo "flush privileges" | mysql -uroot -pvagrant

if [ -f /vagrant/vagrant/data/initial.sql ];
then
    #import data, if available
    mysql -uroot -pvagrant shuffle < /vagrant/data/initial.sql
fi

sudo apt-get install -y libjpeg-dev ghostscript pdftk python-pip python-dev libmysqlclient-dev libxml2-dev libxslt1-dev
sudo pip install -U distribute
sudo pip install virtualenv virtualenvwrapper
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.profile
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv shuffle
echo 'workon shuffle' >> ~/.profile
workon shuffle
echo 'source "${VIRTUAL_ENV}/src/django/extras/django_bash_completion"' >> {VIRTUAL_ENV}/bin/postactivate


pip install -r requirements.txt
npm install
bower install
./manage.py migrate
#./manage.py createsuperuser

