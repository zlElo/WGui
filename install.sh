#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Pleas run it with sudo!"
  exit
fi

mkdir -p /opt/zlelo/wireguard-guy/
cp -r ./dist/* /opt/zlelo/wireguard-guy/

ln -s /opt/zlelo/wireguard-guy/wireguard-guy_v1.04 /usr/local/bin/wireguard-guy