#!/usr/bin/env bash

yellow='\e[0;33m'
red='\e[0;31m'
NC='\e[0m' # No Color

#When we login, we always want to get dumped into the /vagrant directory... add this to .bashrc
echo cd /vagrant >> /home/vagrant/.bashrc

echo -e "${yellow}Setting up Apt Sources${NC}"

sudo apt-get update
# Required for apt-add-repository
sudo apt-get install -y python-software-properties build-essential

#Right now using NodeJS instead of IO.JS because ember-cli causes a GC error when installed globally ?!?!?
#Node 0.12
curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
sudo apt-get install -y nodejs
#IO JS 1.x
#curl -sL https://deb.nodesource.com/setup_iojs_1.x | sudo bash -
#sudo apt-get install -y iojs

echo -e "${yellow}Installing system pre-reqs${NC}"

#Add github.com to known hosts, so we can hit it from sudo if needed
touch ~/.ssh/known_hosts
ssh-keyscan -t rsa,dsa github.com 2>&1 | sort -u - ~/.ssh/known_hosts > ~/.ssh/tmp_hosts
cat ~/.ssh/tmp_hosts >> ~/.ssh/known_hosts

sudo apt-get install -y git

echo -e "${yellow}Installing MySQL${NC}"
sudo debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password password vagrant'
sudo debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password_again password vagrant'
sudo apt-get install -y mysql-client-core-5.6 mysql-server-5.6

echo -e "${yellow}Installing User-level Deps${NC}"

#We try to install as many things as user-level deps as possible, because security
su -c "/vagrant/vagrant/bootstrap-user-context.sh" vagrant

#App-specific setup and installation goes here
su -c "/vagrant/vagrant/bootstrap-app.sh" vagrant

echo "${yellow}Farnsworth VM now setup.${NC}"
echo ""
echo "${red}FIRST:${NC} Create an admin by logging via 'vagrant ssh' and running './manage.py createsuperuser'"
echo ""
echo "You can run the python server with this command: "
echo "  vagrant ssh -- -t 'cd /vagrant; source ~/.profile; ./manage.py runserver 0.0.0.0:8000'"
echo ""
echo "You can generate the ember distribution with this command: "
echo " cd ember; npm install; npm build"
echo ""
echo "To use ember server for local ember dev, use this command: "
echo " cd ember; npm install; npm start"
