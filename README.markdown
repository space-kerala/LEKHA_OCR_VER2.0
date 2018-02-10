# Lekha Ocr version 2.0


## Description

Lekha Ocr version 2.0 Converts your malayalam documents and images to editable malayalam text.It's designed to be easy,fast and simple to use.it has add-on features like scanning,croping,rotating and skew correction of images which help you to do things easy. 

In other words, let the machine do most of the malayalam typing work for you.


## Screenshots

### Main Window

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_mainwindow.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_mainwindow.png" width="447" height="262" />
</a>

### Main Window after convertion
<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_output.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_output.png" width="447" height="262" />
</a>


### Settings Window

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_settings.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_settings.png" width="447" height="262" />
</a>


### Layout Analyzed Image

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_layout.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_layout.png" width="447" height="262" />
</a>

### Crop

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_crop.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_crop.png" width="447" height="262" />
</a>




## Main features

* Scan
* Import image from files
* Image layout analysis and feature to correct the result.
* Malayalam ocr (lekha_ocrv2)
* Image Skew correction
* Rotate image
* Crop image
* Set Workspace Directory 
* Save Output malayalam text to text file




## Installation

* git clone https://github.com/space-kerala/LEKHA_OCR_VER2.0.git
* Navigate to root distribution directory
* sudo apt-get update
* sudo bash lekha2-install.sh
* installation done  


## Details

It mainly uses:

* [Pyinsane2](https://pypi.python.org/pypi/pyinsane2): To scan the pages
* [OPENCV](https://github.com/opencv/opencv): for image manipulation and calculations
* [Lekha_ocrv2](https://github.com/space-kerala/LEKHA_OCR_VER2.0/tree/master/lekha_ocr)(OCR)
* [GTK+](http://www.gtk.org/): For the user interface
* [PYGOBJECT](https://pygobject.readthedocs.io/): python binding for Gtk+
* [Matplotlib](https://matplotlib.org/): Selection and for layout analyzed output correction features
* [Pillow](https://pypi.python.org/pypi/Pillow/)



## Licence

GPLv3 only. See License.md


## Development

All the information can be found on (https://github.com/space-kerala)