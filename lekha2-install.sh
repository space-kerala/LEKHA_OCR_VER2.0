#sudo rm $HOME/.local/share/applications/lekha_ocr_ver2.desktop
sudo apt-get install -y python3.5
sudo apt-get install -y python3-matplotlib
sudo apt-get install -y python3-pip
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr
sudo rm -rf /usr/local/lib/python3.5/dist-packages/lekha_ocr-2.0-py3.5.egg-info/
sudo pkg-config --modversion opencv | grep '3' &> /dev/null
if [ $? != 0 ]; then
   echo "opencv not installed in your machine compiling and installing opencv 3.2,time consuming process please wait patiently"	
   
   ######################################
   # INSTALL OPENCV ON UBUNTU OR DEBIAN #
   ######################################

   # |         THIS SCRIPT IS TESTED CORRECTLY ON         |
   # |----------------------------------------------------|
   # | OS             | OpenCV       | Test | Last test   |
   # |----------------|--------------|------|-------------|
   # | Ubuntu 16.04.2 | OpenCV 3.2.0 | OK   | 20 May 2017 |
   # | Debian 8.8     | OpenCV 3.2.0 | OK   | 20 May 2017 |
   # | Debian 9.0     | OpenCV 3.2.0 | OK   | 25 Jun 2017 |

   # 1. KEEP UBUNTU OR DEBIAN UP TO DATE

   sudo apt-get -y update
   sudo apt-get -y upgrade
   sudo apt-get -y dist-upgrade
   sudo apt-get -y autoremove


   # 2. INSTALL THE DEPENDENCIES

   # Build tools:
   sudo apt-get install -y build-essential cmake

   # GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
   sudo apt-get install -y qt5-default libvtk6-dev

   # Media I/O:
   sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev

   # Video I/O:
   sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

   # Parallelism and linear algebra libraries:
   sudo apt-get install -y libtbb-dev libeigen3-dev

   # Python:
   sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy

   # Java:
   sudo apt-get install -y ant default-jdk

   # Documentation:
   sudo apt-get install -y doxygen


   # 3. INSTALL THE LIBRARY (YOU CAN CHANGE '3.2.0' FOR THE LAST STABLE VERSION)

   sudo apt-get install -y unzip wget
   wget https://github.com/opencv/opencv/archive/3.2.0.zip
   unzip 3.2.0.zip
   rm 3.2.0.zip
   mv opencv-3.2.0 OpenCV
   cd OpenCV
   mkdir build
   cd build
   cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON -DENABLE_PRECOMPILED_HEADERS=OFF ..
   make -j4
   sudo make install
   sudo ldconfig
   sudo rm -rf /OPENCV
   
   # 4. EXECUTE SOME OPENCV EXAMPLES AND COMPILE A DEMONSTRATION

   # To complete this step, please visit 'http://milq.github.io/install-opencv-ubuntu-debian'.

   #end of install-opencv.sh
fi

sudo pip3 install .
sudo cp -f lekha_ocr_ver2.desktop /usr/share/applications
