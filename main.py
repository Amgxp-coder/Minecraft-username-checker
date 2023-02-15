import urllib3
import certifi
import json
import os
import time

found = 0
fails = 0

with open('userlist.txt') as f:
    for line in f:
        line = line.strip(' ').strip('\n')

        url = 'https://api.mojang.com/users/profiles/minecraft/'
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        try:
            r = http.request('GET', url + line)
            #print str(url + line)
        except urllib3.exceptions.SSLError as e:
          print("")

        try:
            r_data = json.loads(r.data.decode('utf-8'))
            # print r_data
        except Exception as e:
            # print(str(e))
            r_data = ""

        if r_data:
            print("Username: " + r_data['name'] + ", UUID: " + r_data['id'] + ", Paid: TRUE")
            fails += 1
            os.system(f"title Minecraft Checker By @amgxp ^| Found {found} ^| Fails {fails}")
            time.sleep(1)
            None
        else:
            print("Username: " + line + " Paid: FALSE")
            found += 1
            os.system(f"title Minecraft Checker By @amgxp ^| Found {found} ^| Fails {fails}")
            time.sleep(1)
            filename = "Found.txt"
            myfile = open(filename, 'a')
            myfile.write(line + "\n")
            myfile.close()


time.sleep("1")
