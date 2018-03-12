# Lekha Ocr version 2.0


## Description

Lekha Ocr version 2.0 Converts your malayalam documents and images to editable malayalam text.It's designed to be easy,fast and simple to use.it has add-on features like scanning,croping,rotating and skew correction of images which help you to do things easy. 

In other words, let the machine do most of the malayalam typing work for you.


## Screenshots

### Main Window

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_mainwindow.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_mainwindow.png" width="534" height="300" />
</a>

### Main Window after convertion
<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_output.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_output.png" width="534" height="300" />
</a>


### Settings Window

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_settings.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_settings.png" width="280" height="300" />
</a>


### Layout Analyzed Image

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_layout.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_layout.png" width="534" height="300" />
</a>

### Crop

<a href="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_crop.png">
  <img src="https://github.com/space-kerala/LEKHA_OCR_VER2.0/blob/master/screenshots/screenshot_crop.png" width="353" height="300" />
</a>




## Main features

* Scan
* Import image from disk
* Image layout analysis and feature to correct the result : draw new box by selecting and then press enter to confirm  ,delete the incorrect layout analysed box by clicking on respective box.
* Malayalam ocr (lekha_ocrv2)
* [Image Skew correction](https://github.com/kakul/Alyn)
* Rotate image
* Crop image : crop out unwanted parts of imported/scanned image using crop functionality.
* Set Workspace Directory
* Save Output malayalam text to text file.




## Installation : Debian/Ubuntu

* git clone https://gitlab.com/space-kerala/LEKHA_OCR_VER2.0.git
  (or Download zip and extract)
* Navigate to the cloned or extracted directory
* sudo apt-get update
* sudo bash lekha2-install.sh
* installation done  
* Open the application by searching lekha ocr ver 2 in the dash
* Set workspace directory under edit-> preference before any scan operation.

## To Uninstall
* sudo bash uninstall.sh 

## Details

It mainly uses:

* [Pyinsane2](https://pypi.python.org/pypi/pyinsane2): To scan the pages
* [OPENCV](https://github.com/opencv/opencv): for image manipulation and calculations
* [Lekha_ocrv2](https://github.com/space-kerala/LEKHA_OCR_VER2.0/tree/master/lekha_ocr)(OCR)
* [GTK+](http://www.gtk.org/): For the user interface
* [PYGOBJECT](https://pygobject.readthedocs.io/): python binding for Gtk+
* [Matplotlib](https://matplotlib.org/): Selection and for layout analyzed output correction features
* [Pillow](https://pypi.python.org/pypi/Pillow/)


## Creators
  Team under Arun M    
* [Sachin Gracious](https://github.com/sachingracious)
* [Sajaras k](https://github.com/sajaras)
* [Yadhukrishnan K](https://github.com/yadu17)

## Contributors
* Arun M helped in project management and technical assistance.
* Ambily Sreekumar,contributed in building data set for training.
* [Jithin thankachan](https://github.com/jithin-space):contributed in training tool and helped in documentation.
* [Arun Joseph](https://github.com/arunjoseph0):contributed most of the engine initial  developments of [Lekha ocr 1.0](https://gitlab.com/space-kerala/lekha-OCR)
* Balagopal Unnikrishnan : Contributed in preparing XML label for training and helped in documentation of[Lekha ocr 1.0](https://gitlab.com/space-kerala/lekha-OCR)
* Rijoy V : Contributed in initial research of [Lekha OCR ver 1.0](https://gitlab.com/space-kerala/lekha-OCR)

## Supporters
   
This project is developed by [SPACE-KERALA](https://github.com/space-kerala) in association with [ICFOSS](https://icfoss.in)


## Licence

GPLv3 only. See License.md


## Development

All the information can be found on (https://github.com/space-kerala)