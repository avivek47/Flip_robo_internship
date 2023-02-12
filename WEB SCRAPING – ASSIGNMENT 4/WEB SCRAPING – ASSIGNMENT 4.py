#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING – ASSIGNMENT 4

# In[2]:


import pandas as pd
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

import warnings
warnings.filterwarnings('ignore')


# **1. Scrape the details of most viewed videos on YouTube from Wikipedia.**
# 
# **Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos**
# 
# **You need to find following details:
# 
# **A) Rank**
# 
# **B) Name**
# 
# **C) Artist**
# 
# **D) Upload date**
# 
# **E) Views**

# In[2]:


# Request URl
url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
page = requests.get(url)

# to show the response output from the webpage
print("Legality Response number from our URL is:", page) # to show the response output from the webpage
soup = BeautifulSoup(page.content)

time.sleep(2)


# In[3]:


# Activating the chrome browser
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
time.sleep(2)

driver.get(url)
#Maximize the web Browser size
driver.maximize_window()

driver.find_element(By.XPATH,"//b").click()

records = []
for row in driver.find_elements(By.XPATH,"(//table[@class='wikitable sortable jquery-tablesorter'])[1]//tr")[1:-1]:
    temp = ''
    for element in row.find_elements(By.XPATH,".//td"):        
        temp += element.text + '|'
    records.append(temp.split('|')[:-2])

df = pd.DataFrame(records, columns=['Rank', 'Video_Name', 'Artist_Name', 'Views_in_Billions', 'Upload_Date'])

arranged_cols = ['Rank', 'Video_Name', 'Artist_Name', 'Upload_Date', 'Views_in_Billions']

df.Video_Name = df.Video_Name.apply(lambda x:x[:-4].strip('"'))
df = df[arranged_cols]
df


# **Q2 Scrape the details team India’s international fixtures from bcci.tv.**
# **Url = https://www.bcci.tv/.**
#     
# **You need to find following details:**
# 
# **A) Match title (I.e. 1st ODI)**
# 
# **B) Series**
# 
# **C) Place**
# 
# **D) Date**
# 
# **E) Time**
# 
# **Note: - From bcci.tv home page you have reach to the international fixture page through code.**

# In[5]:


#connect to web driver
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver
url='https://www.bcci.tv/international/fixtures'
driver.get(url)


# In[6]:


# Click on international match upcoming.
inter = driver.find_element(By.XPATH,'/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a')
inter.click()


# In[8]:


Name = []
Date = [] 
Place =[]
Series = []
Time = []

# scraping Series Name
for i in driver.find_elements(By.XPATH,'//span[@class="ng-binding"]'):
    Name.append(i.text)
    
# scraping Date    
for i in driver.find_elements(By.XPATH,'//h5[@class="ng-binding"]'):
    Date.append(i.text)
    
# scraping Place
for i in driver.find_elements(By.XPATH,'//span[@class="ng-binding ng-scope"]'):
    Place.append(i.text)
    
# scraping Series
for i in driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]'):
    Series.append(i.text)
    
# scraping Time
for i in driver.find_elements(By.XPATH,'//h5[@class="text-right ng-binding"]'):
    Time.append(i.text)


# In[11]:


#length of data
len(Series),len(Name),len(Place),len(Date),len(Time)


# In[10]:


Bcci= pd.DataFrame({'Match title':Series, 'Series':Name, 'Place':Place, 'Date':Date, 'Time':Time})
Bcci


# **Q3.Scrape the details of State-wise GDP of India from statisticstime.com.**
# 
# **Url = http://statisticstimes.com/**
# 
# **You have to find following details:**
#     
# **A) Rank**
# 
# **B) State**
# 
# **C) GSDP(18-19)- at current prices**
# 
# **D) GSDP(19-20)- at current prices**
# 
# **E) Share(18-19)**
# 
# **F) GDP($ billion)**
# 
# **Note: - From statisticstimes home page you have to reach to economy page through code.**
#     

# In[18]:


#connect to web driver
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver
url='http://statisticstimes.com/'
driver.get(url)


# In[19]:


economyTag=driver.find_elements(By.XPATH,"//button[@class='dropbtn']")
economyTag[1].click()


# In[20]:


try:
    IndiaTag=driver.find_elements(By.XPATH,"//div[@class='dropdown-content']/a")
    driver.get(IndiaTag[4].get_attribute('href'))
except:
    print("Error")


# In[21]:


driver.get(driver.find_elements(By.XPATH,"//a[@class='ec']")[13].get_attribute('href'))


# In[30]:


Rank=[]
state=[]
GSDP=[]
GSDP18_19=[]
try:
    rankTag=driver.find_elements(By.XPATH,"//td[@class='data1']")
    Rank.extend([i.text for i in rankTag[:33]])
    state.extend([i.text for i in driver.find_elements(By.XPATH,"//td[@class='name']")][:33])
    GSDP18_19.extend([i.text for i in driver.find_elements(By.XPATH,"//td[@class='data sorting_1']")][:33])
    GSDP.extend([i.text for i in driver.find_elements(By.XPATH,"//td[@class='data']")][:165])
except:
    Rank.append("-")
    state.append("-")
    GSDP.append("-")
    GSDP18_19.append("-")


# In[34]:


GSDP19_20=GSDP[::5]
GSDP19_20
Share=GSDP[1::5]
GDP=GSDP[2::5]
GSDPat11_12_1920=GSDP[3::5]
GSDPat11_12_1819=GSDP[4::5]


# In[35]:


len(Rank),len(state),len(GSDP19_20),len(GSDP18_19),len(Share),len(GDP),len(GSDPat11_12_1920),len(GSDPat11_12_1819)


# In[36]:


df=pd.DataFrame()
df['Rank']=Rank
df['State']=state
df['GSDP (Cr INR at Current prices) 19-20']=GSDP19_20
df['GSDP (Cr INR at Current prices) 18-19']=GSDP18_19
df['shares']=Share
df['GDP ($billion)']=GDP
df['GSDP (Cr INR at 2011-12 prices) 19-20']=GSDPat11_12_1920
df['GSDP (Cr INR at 2011-12 prices) 18-19']=GSDPat11_12_1819


# In[37]:


df


# **4.Scrape the details of trending repositories on Github.com.**
# 
# **Url = https://github.com/**
# 
# **You have to find the following details:**
# 
# **A) Repository title**
# 
# **B) Repository description**
# 
# **C) Contributors count**
# 
# **D) Language used**

# In[92]:


#connect to web driver
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver
url='https://github.com/trending'
driver.get(url)
time.sleep(1)

#Initializing empty lists
url=[]
contributor=[]
language=[]
title=[]
description=[]

#scraping repositories urls data
urls=driver.find_elements(By.XPATH,"//h1[@class='h3 lh-condensed']/a")
url = [i.get_attribute('href') for i in urls]
    
#scraping repositories title data
titles=driver.find_elements(By.XPATH,"//h1[@class='h3 lh-condensed']")
title = [i.text for i in titles]
    
#scraping repositories description data
descriptions=driver.find_elements(By.XPATH,"//article[@class='Box-row']/p")
description = [i.text for i in descriptions]

for i in url:
    driver.get(i)
    time.sleep(1)
    #scraping contributors count data
    try:
        count=driver.find_element(By.XPATH,"//h2[@class='h4 mb-3']/a[contains(text(),'Contributors')]/span")
        contributor.append(count.text)
    #Handle NoSuchElementException
    except NoSuchElementException:
        contributor.append('Not available')
    
    #scraping languages data
    lan = []
    languages=driver.find_elements(By.XPATH,"//li[@class='d-inline']//a//span[1]")
    if languages:    
        lan = [i.text for i in languages]
    else:
        lan.append('Not available')
    language.append(lan) 


# In[93]:


len(title),len(description),len(contributor),len(language)


# In[94]:


#creating data frame
df=pd.DataFrame({'Title':title[0:24],'Description':description[0:24],'Contributors count':contributor[0:24],'Language used':language[0:24]})
#Displaying data frame
df


# **5. Scrape the details of top 100 songs on billiboard.com.**
# 
# **Url = https:/www.billboard.com/**
# 
# **You have to find the following details:**
# 
# **A) Song name**
# 
# **B) Artist name**
# 
# **C) Last week rank**
# 
# **D) Peak rank**
# 
# **E) Weeks on board**
# 
# **Note: - From the home page you have to click on the charts option then hot 100-page link through code.**

# In[115]:


# Calling the browser
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver

# Getting into the website
url = "https:/www.billboard.com/"
driver.get(url)
time.sleep(3)


# In[116]:


#clicking the charts button
options=driver.find_element(By.XPATH,"//button[@class='o-icon-button lrv-a-unstyle-button lrv-a-unstyle-link lrv-u-cursor-pointer lrv-u-flex js-MegaMenu-Trigger lrv-u-color-grey:hover lrv-a-hover-effect']")
options.click()
charts= driver.find_element(By.XPATH,"//a[@class='c-link  lrv-a-unstyle-link a-font-primary-bold lrv-u-font-size-28@desktop-xl lrv-u-font-size-18 lrv-u-color-grey:hover u-padding-a-1@desktop-max lrv-u-padding-b-050']")
charts.click()
#clicking the hot 100
charts= driver.find_element(By.XPATH,"//a[@class='c-label__link lrv-u-color-brand-primary u-color-black@mobile-max a-font-primary-bold lrv-u-font-size-32 u-whitespace-nowrap@tablet']")
charts.click()
time.sleep(1)


# In[118]:


#Initializing empty lists
song = []
artist = []
lrank = []
prank = []
wboard = []

#scraping name data
songs=driver.find_elements(By.XPATH,"//ul[@class='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max']/li/h3")
song = [i.text for i in songs]

#scraping name data
artists=driver.find_elements(By.XPATH,"//span[@class='c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only']")
artist = [i.text for i in artists]
#First artist
i = driver.find_element(By.XPATH,"//span[@class='c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet']")
artist.insert(0,i.text)

#scraping last week rank data
lranks=driver.find_elements(By.XPATH,"//ul[@class='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max']/li[4]/span")
lrank = [i.text for i in lranks]

#scraping peak rank data
pranks=driver.find_elements(By.XPATH,"//ul[@class='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max']/li[5]/span")
prank = [i.text for i in pranks]

#scraping peak rank data
wboards=driver.find_elements(By.XPATH,"//ul[@class='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max']/li[6]/span")
wboard = [i.text for i in wboards]
wboard


# In[119]:


len(song),len(artist),len(lrank),len(prank),len(wboard)


# In[120]:


#creating data frame
bill_board=pd.DataFrame({'Title':song,'Artist':artist,'Last wee rank':lrank,'Peak rank':prank, 'Weeks on board':wboard})
#Displaying data frame
bill_board


# **Q6.Scrape the details of Highest sellingnovels.**
# Url = https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-greycompare/
# 
# **You have to find the following details:**
# 
# **A) Book name**
# 
# **B) Author name**
# 
# **C) Volumes sold**
# 
# **D) Publisher**
# 
# **E) Genre**

# In[9]:


# Calling the browser
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver

# Getting into the website
url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare/"
driver.get(url)
time.sleep(3)


# In[11]:


#Initializing emty lists
name = []
author = []
volume = []
publisher = []
genre = []

#Scraping book name data
names=driver.find_elements(By.XPATH,"//table[@class='in-article sortable']/tbody/tr/td[2]")
name = [i.text for i in names]

#Scraping author name data
authors=driver.find_elements(By.XPATH,"//table[@class='in-article sortable']/tbody/tr/td[3]")
author = [i.text for i in authors]

try:
    volumes=driver.find_elements(By.XPATH,"//table[@class='in-article sortable']/tbody/tr/td[4]")
    volume = [i.text for i in volumes]
#Handling NoSuchElementException
except NoSuchElementException:
    volume.append('Not available')
    
#Scraping publisher name data
publishers=driver.find_elements(By.XPATH,"//table[@class='in-article sortable']/tbody/tr/td[5]")
publisher = [i.text for i in publishers]

#Scraping genre data
try:
    genres=driver.find_elements(By.XPATH,"//table[@class='in-article sortable']/tbody/tr/td[6]")
    genre = [i.text for i in genres]
#Handling NoSuchElementException
except NoSuchElementException:
     genre.append('Not available')


# In[12]:


len(name),len(author),len(genre),len(volume),(publisher)


# In[13]:


#creating data frame
Hig_sellingnovals=pd.DataFrame({'Book name':name,'Author':author,'Genre':genre,'Sales volume':volume, 'Publisher':publisher})

#Displaying data frame
Hig_sellingnovals


# **7. Scrape the details most watched tv series of all time from imdb.com.**
# 
# **Url = https://www.imdb.com/list/ls095964455/**
#     
# **You have to find the following details:**
#     
# **A) Name**
# 
# **B) Year span**
# 
# **C) Genre**
# 
# **D) Run time**
# 
# **E) Ratings**
# 
# **F) Votes**

# In[3]:


# Calling the browser
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver

# Getting into the website
url = "https://www.imdb.com/list/ls095964455/"
driver.get(url)
time.sleep(1)


# In[4]:


#creating emty lists
name = []
run = []
year = []
rate = []
genre = []
vote = []


# In[6]:



#Scraping tv series name data
names=driver.find_elements(By.XPATH,"//h3[@class='lister-item-header']/a")
name = [i.text for i in names]
#Scraping tv series genre data
genres=driver.find_elements(By.XPATH,"//span[@class='genre']")
genre = [i.text for i in genres] 
#Scraping tv series year of release data
years=driver.find_elements(By.XPATH,"//h3[@class='lister-item-header']/span[2]")
year = [i.text for i in years]
#Scraping tv series runtime data
runs=driver.find_elements(By.XPATH,"//span[@class='runtime']")
run = [i.text for i in runs]  

#Scraping tv series rating data
try:
    rates=driver.find_elements(By.XPATH,"//div[@class='ipl-rating-star small']/span[2]")
    rate = [i.text for i in rates]
#Handling NosuchElementException
except:
    rate.append('Not available')
    
#Scraping tv series voting data
try:
    votes=driver.find_elements(By.XPATH,"//span[@name='nv']")
    vote = [i.text for i in votes]
#Handling NosuchElementException
except:
    vote.append('Not available')


# In[7]:


len(name),len(genre),len(rate),len(year),len(run),len(vote)


# In[8]:


#creating data frame
imdb=pd.DataFrame({'Name':name,'Genre':genre, 'Ratings':rate, 'Year of release':year,'Runtime':run, 'Votes':vote})
#Displaying data frame
imdb


# **Details of Datasets from UCI machine learning repositories.**
# 
# **Url = https://archive.ics.uci.edu/**
# 
# **You have to find the following details:**
# 
# **A) Dataset name**
# 
# **B) Data type**
# 
# **C) Task**
# 
# **D) Attribute type**
# 
# **E) No of instances**
# 
# **F) No of attribute**
# 
# **G) Year**
# 
# **Note: - from the home page you have to go to the ShowAllDataset page through code.**

# In[19]:


# Calling the browser
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe") 
driver

# Getting into the website
url = "https://archive.ics.uci.edu/"
driver.get(url)
time.sleep(1)


# In[20]:


#Clicking on view all datasets link
datasets=driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td[2]/span[2]/a/font/b")
try:
    datasets.click()
except ElementNotInteractableException:
    driver.get(datasets.get_attribute('href'))


# In[21]:


#Creating empty lists for storing the data
Name=[]
Type=[]
Task=[]
Attribute=[]
No_of_Instance=[]
No_of_Attribute=[]
Year=[]


try:
    names=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[2]/p/b/a")
    for i in names:
        Name.append(i.text)
except NoSuchElementException:
    Name.append('-')
    
#Scrapping the data having data type
try:
    types=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]")
    for i in types[1:]:
        Type.append(i.text)
except NoSuchElementException:
    Type.append('-')
    
#Scrapping the data having default task
try:
    task=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[3]")
    for i in task[1:]:
        Task.append(i.text)
except NoSuchElementException:
    Task.append('-')
        
#Scrapping the data having attribute types
try:
    attribute=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[4]")
    for i in attribute[1:]:
        Attribute.append(i.text)
except NoSuchElementException:
     Attribute.append('-')
        
#Scrapping the data having no of instances
try:
    instance=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[5]")
    for i in instance[1:]:
        No_of_Instance.append(i.text)
except NoSuchElementException:
    No_of_Instance.append('-')
        
#Scrapping the data having no of attributes
try:
    attribute_no=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[6]")
    for i in attribute_no[1:]:
        No_of_Attribute.append(i.text)
except NoSuchElementException:
    No_of_Attribute.append('-')
        
#Scrapping the data having the year details
try:
    year=driver.find_elements(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[7]")
    for i in year[1:]:
        Year.append(i.text)
except NoSuchElementException:
    Year.append('-')
    


# In[23]:


len(Name),len(Type),len(Task),len(Attribute),len(No_of_Instance),len(No_of_Attribute),len(Year)


# In[24]:



#Creating the dataframe
df10=pd.DataFrame({"Name":Name,"Data types":Type,"Default Task":Task,"Attribute types":Attribute, 
                 "No of instances":No_of_Instance,"No of atrributes":No_of_Attribute,"Year":Year})
df10 


# In[ ]:




