#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
from datetime import date


# In[2]:


chrome_browser = webdriver.Chrome()
chrome_browser.get("https://www.mohfw.gov.in/")
time.sleep(15)


# In[3]:


exp=chrome_browser.find_element_by_xpath('//*[@id="state-data"]/div/div/div/h2/a')
exp.click()


# In[4]:


today=date.today()
today_date = str(today)
print(today_date)


# In[7]:


head_list=[]
h= chrome_browser.find_element_by_xpath('//*[@id="state-data"]/div/div/div/div/table')
th_list=h.find_elements_by_tag_name('th')

for i in th_list:
    head_list.append(i.text)
    
print(head_list)
print(len(head_list))


# In[36]:


column_names=['S. No.', 'Name of State / UT', 'Active_Cases_Total', 'Active_Cases_Change since yesterday', 'Cured/Discharged/Migrated_Cumulative', 'Cured/Discharged/Migrated_Change since yesterday', 'Deaths_Cumulative', 'Deaths_Change since yesterday']
df=pd.DataFrame(columns= column_names)
print(df)


# In[37]:


tr_list=h.find_elements_by_tag_name('tr')

for i in tr_list:
    td_list=i.find_elements_by_tag_name('td') # tag name retrieve each piece of info for a state
    row=[]
    for td in td_list:
        row.append(td.text) # creating row ie each state data
    #print(row)
    
    try:
        data = {}
        for j in range(len(df.columns)):
            data[df.columns[j]] = row[j] 
        df = df.append(data, ignore_index=True)
    except:
        continue
    
    


# In[38]:


df


# In[39]:


df=df.drop(columns=['S. No.'])


# In[40]:


df


# In[41]:


df.to_csv('Covid_Dataset_'+today_date+'.csv', index = False)


# In[ ]:




