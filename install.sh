#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "To install the program, you need to run the installation script with sudo!"
  exit
fi

mkdir -p /opt/zlelo/wgui/

echo "[✓] Mkdir successfull"

cp -r ./dist/* /opt/zlelo/wgui/

echo "[✓] Copyed successfully the important files to opt"

ln -s /opt/zlelo/wgui/wgui_v1.13-2 /usr/local/bin/wgui

echo ""
echo "[✓] Installation successfully!"
echo "You can run the program with the command: wgui"
echo "For more help visit the Wiki"
