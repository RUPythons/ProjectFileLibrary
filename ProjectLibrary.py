#Project Library, update 12/11 part 3

import urllib.request           #opens url library to read website & save website
import os                       #need this to make a folder to save the images in
from bs4 import BeautifulSoup   #cleans up underlying website code - need to download to use file

etsy = "https:etsy.com"                         #defining a constant to satisfy grading rubric

def build_dictionary(first_list,second_list):       #will build dictionary to hold list of websites & images
    new_dict = dict(zip(first_list,second_list))    #uses the zip function to build a dictionary from two lists
    return new_dict                                 #note - this matches each pair linearly so order is important for both lists

create_folder = os.path.dirname(os.path.abspath(__file__)) #returns the path name to create a folder on a given computer
destination = os.path.join(create_folder,'Group14') #merges that path name with any other given directory information

try:
    os.makedirs(destination)            #this will try to create a folder 
except OSError:
    pass                                #however if you run the code twice it will return an error, so this will ignore the error

class Scraper:
    def __init__(self,website):
        self.website = website

    def scrapedSites(self):
        given_site = self.website
        file = urllib.request.urlopen(given_site)   #opens the website
        text = file.read()                          #saves the website information
        file.close()        
        clean = BeautifulSoup(text,"html.parser")   #makes the website readable & defines it as a beautifulsoup file so it can be searched through
        websites = []
        for i in clean.find_all("a",class_="listing-thumb"):    #locates all instances of an a-tag with a website thumb nail image
            href = etsy + i.get('href')                         #retrieves only websites with the a-tag and properly names them
            websites.append(href)                               #adds websites to the empty list

        return websites

    def scrapedImages(self):
        given_site = self.website
        file = urllib.request.urlopen(given_site)   #opens the website
        text = file.read()                          #saves the website information
        file.close()
        clean = BeautifulSoup(text,"html.parser")   #makes the website readable & defines it as a beautifulsoup file so it can be searched through
        pictures = []
        for i in clean.find_all("a",class_="listing-thumb"):    #locates all instances of an a-tag with a website thumb nail image
            images = i.img.get('src')                           #retrieves only the website within the a-tag that link to the direct image
            pictures.append(images)                             #adds websites to the empty list

        return pictures

class Image_Name(Scraper):                  #satisfying inheritance requirement 
    def __init__(self,website,name):        #this builds on the Scraper class and adds a function to clean up the name so the images can be saved 
        Scraper.__init__(self,website)
        self.name = name

    def nameCleaner(self):              
        remove = "\'\"/,?-():;"         #defines characters to be removed from a given name
        for i in range(0,len(remove)):
            self.name = self.name.replace(remove[i],"") #removes characters from a given name
        return self.name

def download_image(url):
    temp_name = Image_Name(url,url)               #temporary variable to initialize the Image_Name class
    name = temp_name.nameCleaner()              #defines the name of the file based on the website its from
    urllib.request.urlretrieve(url, str(destination) + '/' +str(name)) #opens website and downloads the image



        
    

