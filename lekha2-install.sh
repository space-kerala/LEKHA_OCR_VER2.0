#installing python and pip3 for installing packages
sudo apt-get install -y python3.5
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip

#install smc fonts to read the output properly
sudo apt-get install -y fonts-smc

#installing opencv if its not installed using compilation
sudo pkg-config --modversion opencv | grep '3' &> /dev/null
if [ $? != 0 ]; then
  sudo pip3 install opencv-python
fi

#removing lekha ocr if its already installed
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr-2.0-py3.5.egg-info/
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr-2.0.egg-info/

#installing Lekha ocr version 2.0
sudo pip3 install .
sudo cp -f lekha_ocr_ver2.desktop /usr/share/applications/
sudo chmod 666 /usr/local/lib/python3.5/dist-packages/lekha_ocr/conf.json 

#Run this below 4 lines and run  if your gtk version is less than 3.20 
#sudo add-apt-repository ppa:gnome3-team/gnome3-staging
#sudo add-apt-repository ppa:gnome3-team/gnome3
#sudo apt update
#sudo apt dist-upgrade