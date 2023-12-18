#!/bin/bash
echo -e "\e32m[INFO] Getting things ready for you!"

sleep 1

echo "[INFO] Setting up the scripts..."
sudo cp elita /bin
sudo cp elita.py /bin
sudo chmod +x /bin/elita
sudo chmod +x /bin/elita.py

echo "[INFO] Installing Dependencies..."
pip install requests
pip install pygments

echo -e "Now you are good to go! Type \e[31m elita 'good morning'\e[32m and see Elita generate content for you!"
