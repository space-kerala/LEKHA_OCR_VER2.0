#    Lekha Ocr version 2.0 - Convert your malayalam documents and images to editable text
#    Copyright (C) 2018 Space-kerala (Society For Promotion of Alternative Computing and Employment)

#    Lekha Ocr version 2.0 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Lekha Ocr version 2.0 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Setup script for installing Lekha Ocr version 2.0 """

from setuptools import setup

setup(
    name="lekha_ocr",
    version="2.0",
    author="",
    description="Malayalam ocr",
    author_email="",
    url='https://github.com/space-kerala/LEKHA_OCR_App.git',
    download_url='https://github.com',
    keywords=['malayalam ocr','lekha ocr', 'malayalam image to text convertor','malayalam text from image'],
    packages=['lekha_ocr'],
    classifiers=[],
    license='GPL-3.0-only',
    install_requires=['opencv-python','ipython','pygobject','Pillow','matplotlib','scikit-image','pyinsane2','pandas','scikit-learn'],
    include_package_data=True,
    zip_safe=False,
   


   )

