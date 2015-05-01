#!/usr/bin/env bash

yellow='\e[0;33m'
red='\e[0;31m'
NC='\e[0m' # No Color

#Do the installs
cd /vagrant

#Add github.com to known hosts, so we can npm install from it
touch ~/.ssh/known_hosts
ssh-keyscan -t rsa,dsa github.com 2>&1 | sort -u - ~/.ssh/known_hosts > ~/.ssh/tmp_hosts
cat ~/.ssh/tmp_hosts >> ~/.ssh/known_hosts


echo -e "${yellow}Installing npm deps${NC}"
mkdir ~/npm
echo 'export PATH="$PATH:$HOME/npm/bin"' >> ~/.profile
source ~/.profile
npm config set prefix ~/npm

npm install -g bower

