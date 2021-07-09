import os
import math
import cv2 
import subprocess
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
from pytesseract import *
import sqlite3

conn = sqlite3.connect("test.db", isolation_level=None, check_same_thread=False)

c = conn.cursor()

c.execute("SELECT * FROM ocrTable WHERE code = 'ABCD'")
print(c.fetchall())