import tldextract
import requests

url = input("Enter the input: ")
ext = tldextract.extract(url)
tld = ext.suffix
try:
    if tld in ('onion','i2p','bit'):
        print("THis is in darkweb")
    else:
        print("This is not in darkweb")
except:
    print("Error")