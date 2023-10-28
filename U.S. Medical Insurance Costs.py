#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv

age_list = []
region_list = []
smoker_cost = []
nonsmoker_cost = []
age_parents = []

with open('insurance.csv') as insurance_data:
    insurance_data_reader = csv.DictReader(insurance_data)
    
    for row in insurance_data_reader:
        age_list.append(row['age'])
        region_list.append(row['region'])
        if row['smoker'] == "yes":
            smoker_cost.append(row['charges'])
        else:
            nonsmoker_cost.append(row['charges'])
        if int(row['children']) > 0:
            age_parents.append(row['age'])

def avg_funct(funct_list):
    avg_var_total = 0
    for list_item in funct_list:
        avg_var_total += float(list_item)
    return round(avg_var_total/len(funct_list),1)

print("Average age for insured parents is: $", avg_funct(age_parents))

print("Average cost for a smoker is: $", avg_funct(smoker_cost))

print("Average cost for a non-smoker is: $", avg_funct(nonsmoker_cost))

print("Average age of insured is: $", avg_funct(age_list))

print("Average age of insured is: $", avg_funct(age_list))


region_count_dict = {}
for region in region_list:
    if region in region_count_dict:
        region_count_dict[region] += 1
    else:
        region_count_dict[region] = 1

max_value = 0

for region in region_count_dict:
    if region_count_dict.get(region) > max_value:
        max_value = region_count_dict.get(region)
        max_region = region

print("The region with the most insured is the", max_region, "region")
        


# In[ ]:




