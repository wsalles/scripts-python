#!/usr/bin/env python3.4
import os, sys, json

print("Testando OS")
os.system("""ls
PROFILES=(10 20 30)
for x in ${PROFILES[@]}
do
 echo $x
done
df -h
pwd
""")

with open('rsync_4k_HDR.json', 'w') as jsonfile:
        data = {
        'process': 'rsync',
        'status': 'True',
        'source': '/mnt/DISTRIBUICAO/2398/HDR/Audio_5_1',
        'destination': '/mnt/elemental-new/Fluxo_4k/input/HDR_2398'
        }
        json.dump(data, jsonfile)

exit()
