# coding = utf-8
from selenium import webdriver
import time
import json
import numpy as np
import pytesseract
import datetime
import os
from PIL import Image, ImageEnhance
from logging import Logger

def code_verify(file):
    im = Image.open(file)
    im = im.convert('')

    reponse = pytesseract.image_to_string(im)
    res = reponse
    print(res)


code_verify(r'MachineLearning/OCR/code.jpeg')
