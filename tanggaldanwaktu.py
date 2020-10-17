import time;  # Digunakan untuk meng-import modul time

ticks = time.time()
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks)

import time;

localtime = time.localtime(time.time())
print ("Waktu lokal saat ini :", localtime)
"""
import calendar

cal = calendar.month(2008, 1)
print ("Dibawah ini adalah kalender:")
print (cal)
"""