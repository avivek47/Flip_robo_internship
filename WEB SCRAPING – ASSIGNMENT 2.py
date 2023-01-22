#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Let's first install selenium Library
get_ipython().system('pip install selenium')


# **Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape 
# the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:**
#     
# **1. First get the webpage https://www.naukri.com/**
# 
# **2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.**
# 
# **3. Then click the search button.**
# 
# **4. Then scrape the data for the first 10 jobs results you get.**
# 
# **5. Finally create a dataframe of the scraped data.**

# In[23]:


# Let's import all required Libraries
import selenium                              
from selenium import webdriver               
import pandas as pd                          
from selenium.webdriver.common.by import By  
import warnings                            
warnings.filterwarnings("ignore")       
import time 


# In[24]:


# Let's frist connect to web driver
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")


# In[25]:


# Let's maximize the automated chrome window
driver.maximize_window()


# In[26]:


#opening up naukri.com website on automated chrome window
url = 'https://www.naukri.com/'
driver.get(url)


# In[27]:


# finding web element for search job bar
search_job = driver.find_element(By.CLASS_NAME,"suggestor-input")
search_job.send_keys("Data Analyst")


# In[28]:


#fnding web elements for search locn bar using absolute xpath
search_locn = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")
search_locn.send_keys("Bangalore")


# In[29]:


# Clicking using absolute xpath function
search_locn = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search_locn.click() 


# In[30]:


# Let's extract all web elements having job titles
job_titles = []
title_tags = driver.find_elements(By.XPATH,"//a[@class='title ellipsis']")
for i in title_tags:
    job_titles.append(i.text)
len(job_titles)


# In[31]:


job_titles[0:10]


# In[32]:


# Let's extract all web elements having company names
company_names = []
company_tags = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags:
    company_names.append(i.text)
len(company_names)


# In[33]:


# Lets extract all web elements having experience using parent tag
experience =[]
exp_tags = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags:
    experience.append(i.text)
len(experience)


# In[34]:


location = []
locn_tags = driver.find_elements(By.XPATH,'//li[@class="fleft br2 placeHolderLi location"]')
for i in locn_tags:
    location.append(i.text)
len(location)


# In[35]:


len(location), len(experience), len(company_names),len(job_titles)


# In[36]:


jobs= pd.DataFrame()
jobs['location'] = location
jobs['experience'] = experience
jobs['company_names'] = company_names
jobs['job_titles'] = job_titles
jobs[0:10]


# **Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:**
#     
# **1. First get the webpage https://www.naukri.com/**
#     
# **2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.**
# 
# **3. Then click the search button.**
# 
# **4. Then scrape the data for the first 10 jobs results you get.**
# 
# **5. Finally create a dataframe of the scraped data.**

# In[3]:


# Let's frist connect to web driver
driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")


# In[4]:


# Let's maximize the automated chrome window
driver.maximize_window()


# In[5]:


#opening up naukri.com website on automated chrome window
url = 'https://www.naukri.com/'
driver.get(url)


# In[6]:


# finding web element for search job bar
search_job = driver.find_element(By.CLASS_NAME,"suggestor-input")
search_job.send_keys("Data scientist")


# In[8]:


#fnding web elements for search locn bar using absolute xpath
search_locn = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")
search_locn.send_keys("Bangalore")


# In[9]:


# Clicking using absolute xpath function
search_locn = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search_locn.click()  


# In[10]:


# Let's extract all web elements having job titles
job_titles = []
title_tags = driver.find_elements(By.XPATH,"//a[@class='title ellipsis']")
for i in title_tags:
    job_titles.append(i.text)
len(job_titles)


# In[12]:


job_titles[0:10]


# In[16]:


# Let's extract all web elements having company names
company_names = []
company_tags = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags:
    company_names.append(i.text)
len(company_names)


# In[17]:


# Lets extract all web elements having experience using parent tag
experience =[]
exp_tags = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags:
    experience.append(i.text)
len(experience)


# In[18]:


location = []
locn_tags = driver.find_elements(By.XPATH,'//li[@class="fleft br2 placeHolderLi location"]')
for i in locn_tags:
    location.append(i.text)
len(location)


# In[19]:


len(location), len(experience), len(company_names),len(job_titles)


# In[21]:


jobs= pd.DataFrame()
jobs['location'] = location
jobs['experience'] = experience
jobs['company_names'] = company_names
jobs['job_titles'] = job_titles
jobs[]


# **Q3: In this question you have to scrape data using the filters available on the webpage as shown below:**
# 
# **You have to use the location and salary filter.**
# 
# **You have to scrape data for “Data Scientist” designation for first 10 job results.**
# 
# **You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs**
# 
# **The task will be done as shown in the below steps:**
# 
# **1. first get the webpage https://www.naukri.com/**
# 
# **2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.**
# 
# **3. Then click the search button.**
# 
# **4. Then apply the location filter and salary filter by checking the respective boxes**
# 
# **5. Then scrape the data for the first 10 jobs results you get.**
# 
# **6. Finally create a dataframe of the scraped data.'''**

# In[51]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url = 'https://www.naukri.com/'
driver.get(url)


# In[52]:


search_job = driver.find_element(By.CLASS_NAME,"suggestor-input")
search_job.send_keys("Data scientist")


# In[53]:


search_locn = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")
search_locn.send_keys("Delhi/NCR")


# In[54]:


search_locn = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search_locn.click() 


# In[55]:


# Let's extract all web elements having job titles
job_titles = []
title_tags = driver.find_elements(By.XPATH,"//a[@class='title ellipsis']")
for i in title_tags:
    job_titles.append(i.text)
len(job_titles)


# In[56]:


job_titles[0:10]


# In[57]:


company_names = []
company_tags = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags:
    company_names.append(i.text)
len(company_names)


# In[58]:


experience =[]
exp_tags = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in exp_tags:
    experience.append(i.text)
len(experience)


# In[59]:


location = []
locn_tags = driver.find_elements(By.XPATH,'//li[@class="fleft br2 placeHolderLi location"]')
for i in locn_tags:
    location.append(i.text)
len(location)


# In[60]:


Salary = []
Sal_tags = driver.find_elements(By.XPATH,'//li[@class="fleft br2 placeHolderLi salary"]')
for i in Sal_tags:
    Salary.append(i.text)
len(Salary)


# In[61]:


len(location), len(experience), len(company_names),len(job_titles),len(Salary)


# In[62]:


jobs= pd.DataFrame()
jobs['job_titles'] = job_titles
jobs['company_names'] = company_names
jobs['location'] = location
jobs['experience'] = experience
jobs['Salary']= Salary
jobs[0:10]


# **Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:**
# 
# **1. Brand**
# 
# **2. Product Description**
# 
# **3. Price**
# 
# **To scrape the data you have to go through following steps:**
# **1. Go to Flipkart webpage by url : https://www.flipkart.com/**
# 
# **2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and click the search icon.**
# 
# **3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the required data as usual.**
# 
# **4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then click on it.**
# 
# **5. Now scrape data from this page as usual**
# 
# **6. Repeat this until you get data for 100 sunglasses.**

# In[127]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.flipkart.com/'
driver.get(url)


# In[128]:


close = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
close.click()


# In[129]:


search = driver.find_element(By.CLASS_NAME,"_3704LK")
search.send_keys("sunglasses")
search.submit()


# In[130]:


brand = []
for i in driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]'):
    brand.append(i.text)
len(brand)


# In[131]:


descrp = []
for i in driver.find_elements(By.CLASS_NAME,'IRpwTa'):
    descrp.append(i.text)
len(descrp) 


# In[132]:


price = []
for i in driver.find_elements(By.CLASS_NAME,'_30jeq3'):
    price.append(i.text)
len(price)


# In[133]:


offer = []
for i in driver.find_elements(By.CLASS_NAME,'_3Ay6Sb'):
    offer.append(i.text)
len(offer)


# In[134]:


len(brand),len(descrp),len(price),len(offer)


# In[135]:


nex = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
nex.click()


# In[136]:


for i in driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]'):
    brand.append(i.text)
len(brand)


# In[137]:


for i in driver.find_elements(By.CLASS_NAME,'IRpwTa'):
    descrp.append(i.text)
len(descrp)


# In[138]:


for i in driver.find_elements(By.CLASS_NAME,'_3Ay6Sb'):
    offer.append(i.text)
len(offer)


# In[139]:


len(brand),len(descrp),len(price),len(offer)


# In[140]:


next2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]')
next2.click()


# In[141]:


for i in driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]'):
    brand.append(i.text)
len(brand)


# In[142]:


for i in driver.find_elements(By.CLASS_NAME,'IRpwTa'):
    descrp.append(i.text)
len(descrp)


# In[143]:


for i in driver.find_elements(By.CLASS_NAME,'_30jeq3'):
    price.append(i.text)
len(price)


# In[144]:


for i in driver.find_elements(By.CLASS_NAME,'_3Ay6Sb'):
    offer.append(i.text)
len(offer)


# In[145]:


len(brand),len(descrp),len(price),len(offer)


# In[151]:


next3 = driver.find_element(By.XPATH,'(//a[@class="_1LKTO3"])[2]')
next3.click()


# In[152]:


for i in driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]'):
    brand.append(i.text)
len(brand)


# In[153]:


for i in driver.find_elements(By.CLASS_NAME,'IRpwTa'):
    descrp.append(i.text)
len(descrp)


# In[154]:


for i in driver.find_elements(By.CLASS_NAME,'_30jeq3'):
    price.append(i.text)
len(price)


# In[155]:


for i in driver.find_elements(By.CLASS_NAME,'_3Ay6Sb'):
    offer.append(i.text)
len(offer)


# In[156]:


len(brand),len(descrp),len(price),len(offer)


# In[159]:


flipkart = pd.DataFrame({'Brand Name':brand[0:100], "Decription":descrp[0:100], 'Price':price[0:100], 'Offer':offer[0:100]})
flipkart


# **Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. This task will be done in following steps:**
#         
# **1. First get the webpage https://www.flipkart.com/**
# 
# **2. Enter “iphone 11” in “Search” field .**
# 
# **3. Then click the search button.**
# 
# **As shown in the above page you have to scrape the tick marked attributes.These are:**
# 
# **1. Rating**
# 
# **2. Review summary**
# 
# **3. Full review**
# 
# **4. You have to scrape this data for first 100 reviews.**

# In[160]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.flipkart.com/'
driver.get(url)


# In[161]:


close = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
close.click()


# In[164]:


search = driver.find_element(By.CLASS_NAME,"_3704LK")
search.send_keys('iphone 11')
search.submit()


# In[170]:


iphone_sel = driver.find_element(By.CLASS_NAME,"_4rR01T")
iphone_sel.click()


# In[171]:


star = []
comm = []
bri = []
for page in range(0,10):
    for i in driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]'):
        star.append(i.text)
        
    for i in driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]'):
        comm.append(i.text)
    
    for i in driver.find_elements(By.XPATH,'//div[@class = "t-ZTKy"]'):
        bri.append(i.text)


# In[172]:


len(star),len(comm),len(bri)


# In[173]:


phone = pd.DataFrame({'Star':star, 'Comments':comm, 'Brief':bri})
phone


# **Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 4 attributes of each sneaker:**
#     
# **1. Brand**
# 
# **2. Product Description**
# 
# **3. Price**
# 
# **As shown in the below image, you have to scrape the above attributes.**

# In[183]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.flipkart.com/'
driver.get(url)


# In[184]:


close = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
close.click()


# In[185]:


search = driver.find_element(By.CLASS_NAME,"_3704LK")
search.send_keys('sneakers')
search.submit()


# In[187]:


name,des,pir,off = [],[],[],[]
for page in range(0,3):
    for i in driver.find_elements(By.CLASS_NAME,'_2WkVRV'):
        name.append(i.text)
    
    for i in driver.find_elements(By.CLASS_NAME,'IRpwTa'):
        des.append(i.text)
        
    for i in driver.find_elements(By.XPATH,'//div[@class = "_30jeq3"]'):
        pir.append(i.text)
    
    for i in driver.find_elements(By.CLASS_NAME,'_3Ay6Sb'):
        off.append(i.text)


# In[189]:


len(name),len(des),len(pir),len(off)


# In[190]:


sneaker = pd.DataFrame({'Brand':name[0:100], 'Product Description':des[0:100], 'Price':pir[0:100], 'Offer':off[0:100]})
sneaker


# In[191]:


sneaker['Price and Offer'] = sneaker['Price'] +' and ' + sneaker['Offer']
sneaker.drop(columns = ['Price','Offer'],inplace=True)
sneaker


# **Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:**
# 
# **After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:**
# 
# **1. Title**
# 
# **2. Ratings**
# 
# **3. Price**

# In[192]:


driver.close()


# In[215]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.amazon.in/'
driver.get(url)


# In[216]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('laptop')
search.submit()


# In[217]:


title = []
for i in driver.find_elements(By.XPATH,'//a[@class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]'):
    title.append(i.text)
len(title)


# In[222]:


rate = []
for i in driver.find_elements(By.XPATH,'//span[@class = "a-price-whole"]'):
    ratings.append(i.text)
len(ratings)


# In[223]:


price = []
for i in driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]'):
    price.append(i.text)
len(price)


# In[224]:


len(title),len(ratings),len(price)


# In[226]:


laptop = pd.DataFrame({'Title': title[0:10], 'Price': ratings[0:10], 'Ratings' : price[0:10]})
laptop


# **Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:**
# 
# **1. First get the webpage https://www.azquotes.com/**
# 
# **2. Click on Top Quotes**
# 
# **3. Than scrap a) Quote b) Author c) Type Of Quotes**
# 

# In[264]:


driver.close()


# In[272]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.azquotes.com/'
driver.get(url)


# In[273]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
search.click()


# In[274]:


Quote = []
for i in driver.find_elements(By.XPATH,"//div[@class='wrap-block']"):
    Quote.append(i.text)
len(Quote)


# In[275]:


Author = []
for i in driver.find_elements(By.XPATH,"//div[@class='wrap-block']"):
    Author.append(i.text)
len(Author)


# In[276]:


type_of_quote =[]
for i in driver.find_elements(By.XPATH,"//div[@class='wrap-block']"):
    type_of_quote.append(i.text)
len(type_of_quote)


# In[277]:


len(Quote),len(Author),len(type_of_quote)


# In[278]:


AZ_Quotes = pd.DataFrame({'Quote':Quote,'Author':Author,'Type of quotes':type_of_quote})
AZ_Quotes


# **Q9:Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.**
#     
# **This task will be done in following steps:**
# 
# **1. First get the webpage https://www.jagranjosh.com/**
#     
# **2. Then You have to click on the GK option**
# 
# **3. Then click on the List of all Prime Ministers of India**
# 
# **4. Then scrap the mentioned data and make the DataFrame.**

# In[279]:


driver.close()


# In[280]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.jagranjosh.com/.'
driver.get(url)


# In[283]:


gk_option = driver.find_element(By.XPATH,'//a[normalize-space()="GK"]')
gk_option.click()


# In[284]:


list_of_pm = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[10]/div[1]/div[1]/ul[1]/li[2]/a[1]")
list_of_pm.click()


# In[285]:


Name = []
for i in driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[2]/p'):
    Name.append(i.text)
len(Name)


# In[286]:


Born_dead = []
for i in driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[3]/p'):
    Born_dead.append(i.text)
len(Born_dead)


# In[287]:


Term_Of_Office =[]
for i in driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[4]/p'):
    Term_Of_Office.append(i.text)
len(Term_Of_Office)


# In[288]:


Remarks = []
for i in driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[5]/p'):
    Remarks.append(i.text)
len(Remarks)


# In[289]:


len(Name),len(Born_dead),len(Term_Of_Office),len(Remarks)


# In[294]:


df = pd.DataFrame({'NAME':Name[0:18],'BORN-DEAD':Born_dead[0:18],'TERM-OF-OFFICE':Term_Of_Office[0:18],'REMARKS':Remarks[0:18]})
df


# **Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/**
# 
# **This task will be done in following steps:**
# 
# **1. First get the webpage https://www.motor1.com/**
# 
# **2. Then You have to click on the List option from Dropdown menu on left side.**
# 
# **3. Then click on 50 most expensive cars in the world.**
# 
# **4. Then scrap the mentioned data and make the dataframe.**

# In[ ]:


driver.close()


# In[296]:


driver = webdriver.Chrome(r"C:\Users\Lewnovo\chromedriver.exe")
driver.maximize_window()
url ='https://www.motor1.com/'
driver.get(url)


# In[301]:


menu = driver.find_element(By.CLASS_NAME,'box-item-left')
menu.click()


# In[302]:


Feature_tap = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[5]/button')
Feature_tap.click()


# In[303]:


List = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[6]/ul/li[1]/a')
List.click()


# In[306]:


bstruck = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[1]/div[1]/div/div/div[2]/div/div[1]/h3/a')
bstruck.click()


# In[327]:


car_name,car_desc,car_price=[],[],[]
car_price=[]
carn= driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in carn:
    car_name.append(i.text)
    
card=driver.find_elements(By.TAG_NAME,"p")
for i in card:
    car_desc.append(i.text.replace("Price",""))
    
carp=driver.find_elements(By.TAG_NAME,"strong")
for i in carp:
    car_price.append(i.text)


# In[324]:


len(car_name),len(car_desc),len(car_price)


# In[328]:


df10=pd.DataFrame({"CAR NAME":car_name[0:15],"DESCRIPTION":car_desc[29:44],"CAR PRICE":car_price[18:33]})
df10


# In[ ]:




