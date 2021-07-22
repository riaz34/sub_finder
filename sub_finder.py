#!//usr/bin/python

import requests

domain = input("Enter the Domain name: ")

file = open("subdomains.txt")

content = file.read()

subdomains = content.splitlines()

for sub in subdomains:
    
    url = f"http://{sub}.{domain}"
    try:

        requests.get(url)
        print("[*] Discovered subdomain:", url)
    except requests.ConnectionError:

        pass
