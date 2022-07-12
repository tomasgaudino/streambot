#!/usr/bin/bash

# 1) Update Ubuntu's database of software
sudo apt-get update  > /dev/null
echo "Software updated ✅"

# 2) Install tmux
sudo apt-get install -y tmux  > /dev/null
echo "tmux installed ✅"

# 3) Install Docker
sudo apt install -y docker.io  > /dev/null
echo "Docker installed ✅"

# 4) Start and Automate Docker
sudo systemctl start docker && sudo systemctl enable docker  > /dev/null
echo "Docker started and enabled ✅"

# 5) Change permissions for docker (optional)
# Allow docker commands without requiring sudo prefix
sudo usermod -a -G docker $USER  > /dev/null
echo "Docker permissions changed ✅"

# 1) Create folder for your new instance
mkdir hummingbot_files  > /dev/null

# 2) Create folders for logs, config files and database file
mkdir hummingbot_conf > /dev/null
mkdir hummingbot_files/hummingbot_logs  > /dev/null
mkdir hummingbot_files/hummingbot_data  > /dev/null
mkdir hummingbot_files/hummingbot_scripts  > /dev/null
echo "Folders created ✅"

# 3) Launch a new instance of hummingbot
sudo docker run -d -it \
--network host \
--name hummingbot-instance \
--mount "type=bind,source=$(pwd)/hummingbot_conf,destination=/conf/" \
--mount "type=bind,source=$(pwd)/hummingbot_files/hummingbot_logs,destination=/logs/" \
--mount "type=bind,source=$(pwd)/hummingbot_files/hummingbot_data,destination=/data/" \
--mount "type=bind,source=$(pwd)/hummingbot_files/hummingbot_scripts,destination=/scripts/" \
coinalpha/hummingbot:latest

sudo docker ps
echo "Hummingbot running ✅"