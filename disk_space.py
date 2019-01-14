#-*- coding: utf-8 -*-
import sys, os

stat = os.statvfs("MOUNT")
total = (stat.f_bsize * stat.f_blocks) / 1024
avail = (stat.f_bsize * stat.f_bavail) / 1024
used = total-avail
percent = float(used)/float(total)*100