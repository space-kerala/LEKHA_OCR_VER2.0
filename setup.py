""" Setup script for installing Alyn """

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
    install_requires=['ipython','pygobject','Pillow','matplotlib','scikit-image','pyinsane2','pandas','scikit-learn'],
    include_package_data=True,
    zip_safe=False,
   


   )

