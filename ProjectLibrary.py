#Project Library, update 12/13 finalized

import urllib.request           #opens url library to read website & save website
import os                       #need this to make a folder to save the images in
from bs4 import BeautifulSoup   #cleans up underlying website code - need to download to use file
import itertools

etsy = "https:etsy.com"                         #defining a constant to satisfy grading rubric

create_folder = os.path.dirname(os.path.abspath(__file__)) #returns the path name to create a folder on a given computer
destination = os.path.join(create_folder,'Group14') #merges that path name with any other given directory information

try:
    os.makedirs(destination)            #this will try to create a folder 
except OSError:
    pass                                #however if you run the code twice it will return an error, so this will ignore the error

def cleaner(url):
    name = url
    remove = "\'\"/,?-():;"             #defines characters to remove from website name
    for i in range(0,len(remove)): 
        name = name.replace(remove[i],"") #iterates through the name replacing each character with a blank space
    return name

def download_image(url):
    name = cleaner(url)              #defines the name of the file based on the website its from
    urllib.request.urlretrieve(url, str(destination) + '/' +str(name)) #opens website and downloads the image

def scrapedsites(url):
    given_site = url
    file = urllib.request.urlopen(given_site)   #opens the website
    text = file.read()                          #saves the website information
    file.close()        
    clean = BeautifulSoup(text,"html.parser")   #makes the website readable & defines it as a beautifulsoup file so it can be searched through
    websites = []
    for i in clean.find_all("a",class_="listing-thumb"):    #locates all instances of an a-tag with a website thumb nail image
        href = etsy + i.get('href')                         #retrieves only websites with the a-tag and properly names them
        websites.append(href)                               #adds websites to the empty list

    return websites

def scrapedimages(url):
    given_site = url
    file = urllib.request.urlopen(given_site)   #opens the website
    text = file.read()                          #saves the website information
    file.close()
    clean = BeautifulSoup(text,"html.parser")   #makes the website readable & defines it as a beautifulsoup file so it can be searched through
    pictures = []
    for i in clean.find_all("a",class_="listing-thumb"):    #locates all instances of an a-tag with a website thumb nail image
        images = i.img.get('src')                           #retrieves only the website within the a-tag that link to the direct image
        pictures.append(images)                             #adds websites to the empty list

    return pictures

class List_Ops:
    def __init__(self,list1):
        self.list1 = list1

    def buildlist(self):
        merged_list = list(itertools.chain(*self.list1)) #this will unpack a list of lists as one big list
        return merged_list

class MakeDictionary(List_Ops):         #This class builds on the List_Ops class to demonstrate inheritance
    def __init__(self,list1,list2): 
        List_Ops.__init__(self,list1)   
        self.list2 = list2

    def dictionarybuild(self):                      #will build dictionary to hold list of websites & images
        new_dict = dict(zip(self.list1,self.list2)) #uses the zip function to build a dictionary from two lists
        return new_dict                             #note - this matches each pair linearly so order is important for both lists






    


