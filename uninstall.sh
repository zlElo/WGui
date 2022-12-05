#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Pleas run it with sudo!"
  exit
fi

rm -rf /opt/zlelo/wireguard-guy/

rm -f /usr/local/bin/wireguard-guy