#!/usr/bin/bash

# If Hummingbot has troubles with Docker, try running as root this:
#   rm /var/run/docker.pid
#   ps axf | grep docker | grep -v grep | awk '{print "kill -9 " $1}' | sudo sh
#   dockerd -d

# -r Restart with new strategy
# -s Start and run with new strategy

while getopts 'd:f:p:s:' OPTION; do
  case "$OPTION" in
    d)
      export STRATEGY=$OPTARG
      ;;
    f)
      export CONFIG_FILE_NAME=$OPTARG
      ;;
    p)
      export CONFIG_PASSWORD=admin
      ;;
    s)      
      if [[ "$OPTARG"="hummingbot" ]]
      then
        docker stop "hummingbot-instance"
        docker rm "hummingbot-instance"
        docker run -it --restart=always \
          --name $OPTARG"-instance" \
          --network host \
          --mount "type=bind,source=$(pwd)/hummingbot_conf,destination=/conf/" \
          --mount "type=bind,source=$(pwd)/"$OPTARG"_files/hummingbot_logs,destination=/logs/" \
          --mount "type=bind,source=$(pwd)/"$OPTARG"_files/hummingbot_data,destination=/data/" \
          --mount "type=bind,source=$(pwd)/"$OPTARG"_files/hummingbot_scripts,destination=/scripts/" \
          -e STRATEGY -e CONFIG_FILE_NAME -e CONFIG_PASSWORD\
          coinalpha/hummingbot:latest
      else
        docker stop $OPTARG
        docker rm $OPTARG
        docker run -it --restart=always \
          --name $OPTARG \
          --network host \
          --mount "type=bind,source=$(pwd)/hummingbot_conf,destination=/conf/" \
          --mount "type=bind,source=$(pwd)/"$OPTARG"_files/hummingbot_logs,destination=/logs/" \
          --mount "type=bind,source=$(pwd)/"$OPTARG"_files/hummingbot_data,destination=/data/" \
          --mount "type=bind,source=$(pwd)/"$OPTARG"_files/hummingbot_scripts,destination=/scripts/" \
          -e $STRATEGY -e $CONFIG_FILE_NAME -e $CONFIG_PASSWORD\
          coinalpha/hummingbot:latest
      fi
      unset STRATEGY CONFIG_FILE_NAME CONFIG_PASSWORD
      ;;
    esac
done
shift "$(($OPTIND -1))"