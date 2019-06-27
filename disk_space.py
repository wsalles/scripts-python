#-*- coding: utf-8 -*-
import sys, os

def percentDisk(path):
        stat = os.statvfs(path)
        total = (stat.f_bsize * stat.f_blocks) / 1024
        avail = (stat.f_bsize * stat.f_bavail) / 1024
        used = total-avail
        percent = float(used)/float(total)*100
        p = ("%.2f" % percent)
        return p

mount_point = percentDisk("/mnt/exemplo")