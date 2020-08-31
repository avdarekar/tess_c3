#import libraries
import requests
from bs4 import BeautifulSoup as soup

#open TIC_C3.txt and read from it
starlist = open(r"/Users/adbreeze13/Desktop/UNCResearch/TESS/TIC_C3.txt", "r")
stars = starlist.readlines()
starlist.close()

#the url for the Web TESS Viewing Tool
url = 'https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py'

#open a new file named TESSc3_updated.txt
filename = "TESSc3_updated.txt"
f = open(filename, "w")

#iterate through TIC_C3.txt, search for each star in the Web TESS Viewing Tool, count the number of sectors each star will be observed in in cycle 3, and write this information to TESSc3_updated.txt
for a in stars:
    s = str(a).strip()
    f.write(s + " ")
    star = {'Entry': s}
    res = requests.post(url, data=star)
    page_html = res.text
    page_soup = soup(page_html, "html.parser")
    sector_text = page_soup.body.pre.text
    sectors_list = sector_text.split('.')
    c3 = []
    for x in sectors_list:
        if "in cycle 3" in x and "not observed" not in x:
            c3.append(x)
    f.write(str(len(c3)).strip() + "\n")
    



#close TESSc3_updated.txt
f.close()





c3_observed = []
    for i in c3:
        if "not observed" not in i:
            c3_observed.append(i)




