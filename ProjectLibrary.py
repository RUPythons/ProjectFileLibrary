#Project Library - Updated 12/3

import random                   #needed to generate random numbers
import urllib.request           #opens url library to read website & save website
from bs4 import BeautifulSoup   #cleans up underlying website code - need to download to use file



def build_dictionary(first_list,second_list):       #will build dictionary to hold list of websites & images
    new_dict = dict(zip(first_list,second_list))    #uses the zip function to build a dictionary from two lists
    return new_dict                                 #note - this matches each pair linearly so order is important for both lists

def cleaner(name_str):
    remove = "\'\"!/,?-():;"
    for i in range(0,len(remove)):
        name_str = name_str.replace(remove[i],"")
    return name_str

def download_image(url):
    name = random.randrange(1, 10000)               #assigns random number to name each image
    full_name = str(name) + ".jpg"                  #defines how to name each image
    urllib.request.urlretrieve(str(url), full_name) #opens website and downloads the image

etsy = "https:etsy.com"                         #defining a constant to satisfy grading rubric

def Etsy_Website_Scraper(website):
    given_site = website                       
    file = urllib.request.urlopen(given_site)   #opens website
    text = file.read()                          #saves website information
    clean = BeautifulSoup(text,"html.parser")   #cleans website code & makes it understandable

    websites = []
    
    for i in clean.find_all("a",class_="listing-thumb"):    #locates all instances of an a-tag with a website thumb nail image
        href = etsy + i.get('href')                         #retrieves only websites with the a-tag and properly names them
        websites.append(href)                               #adds websites to the empty list

    return websites

def Etsy_Images_Scraper(website):
    given_site = website                       
    file = urllib.request.urlopen(given_site)   #opens website
    text = file.read()                          #saves website information
    clean = BeautifulSoup(text,"html.parser")   #cleans website code & makes it understandable

    pictures = []
    
    for i in clean.find_all("a",class_="listing-thumb"):
        images = i.img.get('src')                           #retrieves only the website within the a-tag that go back to the direct image
        pictures.append(images)                             #adds websites to the empty list

    return pictures



        
    

