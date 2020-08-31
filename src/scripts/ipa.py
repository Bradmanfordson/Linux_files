#!/usr/bin/python3

import netifaces

string = str()
for interface in netifaces.interfaces():
    addrs = netifaces.ifaddresses(interface)
    try:
        for item in addrs[netifaces.AF_INET]:
            string += f"{interface}: {item.get('addr')}\n"
    except Exception as e:
        pass

print(string)
