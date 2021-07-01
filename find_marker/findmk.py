import cv2
import os
import math
import sqlite3
import subprocess
from PIL import Image
import numpy as np
from pytesseract import *
import matplotlib.pyplot as plt 

conn = sqlite3.connect("test.db", isolation_level=None, check_same_thread=False)

c = conn.cursor()

def findmk(path):
    addr = ''
    print(path)
    img_original = plt.imread(path, cv2.IMREAD_COLOR)
    print(type(img_original))
    print(img_original)

    if (type(img_original) is np.ndarray):
        img_resize = cv2.resize(img_original, dsize=(328, 207), interpolation=cv2.INTER_AREA)
        img_dia = img_resize[:180, :190]
        gray = cv2.cvtColor(img_dia, cv2.COLOR_BGR2GRAY)

        ret, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        addr = ""

        for cont in contours:
            approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
            vtc = len(approx)
            
            c.execute('SELECT * FROM shapeTable WHERE code='+str(vtc))
            rw = c.fetchone()
            print('addr *^^* ', addr)
            print('rw *^^* ', rw)
            if rw != None:
                addr += rw[1]
                print('addr *^^* ', addr)

        img_text = img_resize[:, 150:]
        text = pytesseract.image_to_string(img_text,lang='eng')

        c.execute("SELECT * FROM ocrTable WHERE code='{}'".format(text.strip()))
        addr = addr + " " + c.fetchall()[0][1]
        print('addr *^^* ', addr)
        
        return addr

    else :
        print('error')

