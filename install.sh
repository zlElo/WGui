#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "To install the program, you need to run the installation script with sudo!"
  exit
fi

mkdir -p /opt/zlelo/wireguard-guy/

echo "[✓] Mkdir successfull"

cp -r ./dist/* /opt/zlelo/wireguard-guy/

echo "[✓] Copyed successfully the important files to opt"

ln -s /opt/zlelo/wireguard-guy/wireguard-guy_v1.11 /usr/local/bin/wireguard-guy

echo ""
echo "[✓] Installation successfully!"
echo "You can run the program with the command: wireguard-guy"
echo "For more help visit the Wiki"
