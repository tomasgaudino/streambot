#!/usr/bin/bash

echo "Command: " $0
echo "Current path: "$1
echo "Container id: " $2
echo "Strategy name: "$3
echo "Strategy file: " $4
echo "Password: " $5
echo "Status: " $6

if [[ $6 == "running" ]]
then
  sudo docker stop $2
fi
sudo docker rm $2
sudo docker run -d -it \
  --name $2 \
  --network "host" \
  --mount "type=bind,source="$1"/hummingbot_conf,destination=/conf/" \
  --mount "type=bind,source="$1"/"$2"_files/hummingbot_logs,destination=/logs/" \
  --mount "type=bind,source="$1"/"$2"_files/hummingbot_data,destination=/data/" \
  --mount "type=bind,source="$1"/"$2"_files/hummingbot_scripts,destination=/scripts/" \
  -e $3 -e $4 -e $5\
  coinalpha/hummingbot:latest