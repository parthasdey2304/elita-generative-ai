#!/bin/bash
echo -e "\e[32m[INFO] Getting things ready for you!\e[0m"

sleep 1

echo -e "\e[32m[INFO] Setting up the scripts...\e[0m"
sudo cp elita /bin
sudo cp elita.py /bin
sudo chmod +x /bin/elita
sudo chmod +x /bin/elita.py

sleep 1

echo -e "\e[32m[INFO] Installing Dependencies...\e[0m"
pip install requests
pip install pygments

echo -e "\e[32mNow you are good to go! Type \e[33m elita 'good morning'\e[32m and see Elita generate content for you!"
