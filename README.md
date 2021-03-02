# Database_Advanced
A school project

Hi and welcome reader. This script is for Ubuntu use only

<br>
==========Step 1==========
<br>
install Ubuntu. I'm using ubuntu-20.04-2.0. I installed it on a Virtual machine (Oracle vmbox)
<br>
==========Step 2==========
<br>
install python 3 on ubuntu you can do that as followed
sudo apt update
<br>
sudo apt -y upgrade
<br>
sudo apt install -y python3-pip
<br>
==========Step 3==========
<br>
Navigate to the file folder that you've placed the python script in and right click to open a terminal.
when the terminal is opened type:
<br>
python3 Scraping_File.py3
<br>
==========Step 4==========
<br>
Installing MongoDB for storing our data
<br>
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
<br>
I also installed mongo compass for a better UI. This isn't necessary
<br>
==========Step 5==========
<br>
Now we are installing Redis this is very simple but a very long process
<br>
wget http://download.redis.io/redis-stable.tar.gz
<br>
tar xvzf redis-stable.tar.gz
<br>
cd redis-stable
<br>
make
<br>
make test
<br>
If you are heaving issues and getting errors about installing TCL do the follow. First make sure your ubuntu is up-to-date (sudo apt-get update -y) followed by (sudo apt-get upgrade -y)
<br>
Installing tcl:
<br>
sudo apt-get install -y tcl-dev
