
# coding: utf-8

# In[78]:


##input data
import pandas as pd
import matplotlib.pyplot as plt


# In[79]:


CLTCB = 'CLTCB'
NNTCB = 'NNTCB'
PMTCB = 'PMTCB'
FFTCB = ['CLTCB','NNTCB','PMTCB']
ELNIB = 'ELNIB'
ELISB = 'ELISB'
NUETB = 'NUETB'
RETCB = 'RETCB'
column_list = ['TETCD',
'TETPB',
'GDPRX',
'NGTCP',
'TETCV',
'ESTCP',
'TETGR',
'TEGDS',
'TPOPP',
'ARTCP',
'AVTCP',
'DFTCP',
'EMTCP',
'ENTCP',
'JFTCP',
'KSTCP',
'LGTCP',
'LUTCP',
'MGTCP',
'P1TCP',
'PAPRP',
'PATCP',
'PCTCP',
'POTCP',
'RFTCP',
'NGMPK',
'NGEIK',
'NGTCK',
'NGTXK',
'FFETK',
'NUETK',
'CLPRP',
'CLTCP',
]


# # 按照能源分类
# # According to Enegry class
# ## Non-Renewable Sources
# ### Fossil fuels:
#     #### coal (CL)
#     #### net imports of coal coke (U.S. only)
#     #### natural gas excluding supplemental gaseous fuels (NN)
#     #### petroleum products excluding fuel ethanol blended into motor gasoline(PM)
#     
#     
# ### Nuclear electric power (NU)
# ## Renewable Sources
#     #### fuel ethanol minus denaturant (EM)
#     #### geothermal direct use energy and geothermal heat pumps (GE)
#     #### conventional hydroelectric power (HY)
#     #### solar thermal direct use energy and photovoltaic electricity net generation (SO)
#     #### electricity produced by wind (WY)
#     #### wood and wood-derived fuels (WD)
#     #### biomass waste (WS) 
# 

# In[82]:


city_list = ['AZ','CA','NM','TX']
for city in city_list:
    town = pd.read_csv('C:/Users/59531/Desktop/preprocessing/'+city+'.csv')
    AZ_resource_profile = pd.DataFrame()
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Coal Total consumption',value=town[CLTCB],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Natural Gas Total consumption',value=town[NNTCB],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Petroleum Total consumption',value=town[PMTCB],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Fossil Fuels Total consumption',value=town[PMTCB]+town[NNTCB]+town[CLTCB],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Nuclear electric Total consumption',value=town[NUETB],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Renewable Sources Total consumption',value=town[RETCB],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Non-Renewable Sources Total consumption',value=AZ_resource_profile['Nuclear electric Total consumption']+AZ_resource_profile['Fossil Fuels Total consumption'],allow_duplicates=False)
    AZ_resource_profile.insert(len(AZ_resource_profile.columns),column='Total Enegry consumption',value=AZ_resource_profile['Renewable Sources Total consumption']+AZ_resource_profile['Non-Renewable Sources Total consumption'],allow_duplicates=False)
    AZ_resource_profile.plot()
    AZ_town_data = pd.DataFrame()
    for each in column_list:
        if each in AZ_town.columns:
            AZ_town_data.insert(len(AZ_town_data.columns),column=each,value=AZ_town[each],allow_duplicates=False)
    AZ_town_data.to_csv('C:/Users/59531/Desktop/city_data/'+city+'_town_data.csv')

