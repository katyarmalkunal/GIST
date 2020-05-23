
# coding: utf-8

# In[1]:


import os
os.chdir("F:\Kunal\Job_Applications\DeeperSystem")
os.getcwd()


# In[2]:


import pandas as pd

df=pd.read_json("source_file_2.json")


# In[3]:


df.head()


# In[4]:


df.info()


# In[7]:


# MANAGERS
managers=[]
for ind,row in df.iterrows():
    if len(row['managers'])!=1:
        for man in row['managers']:
            if man not in managers:
                managers.append(man)
    else:
        if row['managers'][0] not in managers:
            managers.append(row['managers'][0])
            
            
# WATCHERS            
watchers=[]
for ind,row in df.iterrows():
    if len(row['watchers'])!=1:
        for watcher in row['watchers']:
            if watcher not in watchers:
                watchers.append(watcher)
    else:
        if row['watchers'][0] not in watchers:
            watchers.append(row['watchers'][0])


# In[8]:


print(managers)
print(25*"*")
print(watchers)


# In[9]:


# MANAGERS
dct_man={}
for man in managers:
    dct_man.setdefault(man,[])
#WATCHERS
dct_watcher={}
for watcher in watchers:
    dct_watcher.setdefault(watcher,[])


# In[10]:


# appending values (project_name & priority) to dictionary for each manager & watcher
# we are appending priority value as well because, we will be using the same to sort the list of tuples

#MANAGERS
for ind,row in df.iterrows():
    if len(row['managers'])!=1:
        for man in row['managers']:
            dct_man[man].append((row['name'],row['priority']))
    else:
        dct_man[row['managers'][0]].append((row['name'],row['priority']))
#WATCHERS
for ind,row in df.iterrows():
    if len(row['watchers'])!=1:
        for watcher in row['watchers']:
            dct_watcher[watcher].append((row['name'],row['priority']))
    else:
        dct_watcher[row['watchers'][0]].append((row['name'],row['priority']))


# In[19]:


print(dct_man)
print(50*"*")
print(dct_watcher)


# In[12]:


from operator import itemgetter

# we are sorting list of tuples based on 2nd position value of tuple i.e index 1 value

#MANAGERS
for man in managers:
    dct_man[man]=sorted(dct_man[man],key=itemgetter(1))
#WATCHERS
for watcher in watchers:
    dct_watcher[watcher]=sorted(dct_watcher[watcher],key=itemgetter(1))
    


# In[14]:


#MANAGERS
dct_man_res={}
for man in managers:
    dct_man_res.setdefault(man,[])
#WATCHERS
dct_watcher_res={}
for watcher in watchers:
    dct_watcher_res.setdefault(watcher,[])
    

# now here we are just getting project_name value from the list of tuple (as we are done with sorting based on priority value)

#MANAGERS
for man in managers:
    for item in dct_man[man]:
        dct_man_res[man].append(item[0])
#WATCHERS
for watcher in watchers:
    for item in dct_watcher[watcher]:
        dct_watcher_res[watcher].append(item[0])
        


# In[21]:


import json

#Writing data to json files

#MANAGERS
js_managers=json.dumps(dct_man_res)
with open("managers.json","w") as file:
    file.write(js_managers)
    
#WATCHERS
js_watchers=json.dumps(dct_watcher_res)
with open("watchers.json","w") as file:
    file.write(js_watchers)

