#!/bin/bash

sudo cp elita /bin
sudo cp elita.py /bin

sudo chmod +x /bin/elita
sudo chmod +x /bin/elita.py

sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python-is-python3 -y
pip install requests
pip install pygments
