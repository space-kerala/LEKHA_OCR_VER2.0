#installing python and pip3 for installing packages
sudo apt-get install -y python3.5
sudo apt-get install -y python3-tk
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip

#install smc fonts to read the output properly
sudo apt-get install -y fonts-smc

#installing opencv if its not installed using compilation
sudo pkg-config --modversion opencv | grep '3' &> /dev/null
if [ $? != 0 ]; then
  sudo pip3 install opencv-python
fi

#checking gtk version >=3.20 if less than 3.20 then upgrade to 3.20
if [[ $(sudo apt-cache policy  libgtk-3-0 | head -n 2 | tail -n 1 |grep '3.18') ]]; then
    echo "application requires gtk version >=3.20.upgrading from gtk 3.18 to latest version"
    sudo add-apt-repository ppa:gnome3-team/gnome3-staging
    sudo add-apt-repository ppa:gnome3-team/gnome3
    sudo apt update
    sudo apt dist-upgrade
else
    echo "gtk version is already >=3.20"
fi

#removing lekha ocr if its already installed
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr-2.0-py3.5.egg-info/
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr-2.0.egg-info/

#installing Lekha ocr version 2.0
sudo pip3 install .
sudo cp -f lekha_ocr_ver2.desktop /usr/share/applications/
sudo chmod 666 /usr/local/lib/python3.5/dist-packages/lekha_ocr/conf.json 





