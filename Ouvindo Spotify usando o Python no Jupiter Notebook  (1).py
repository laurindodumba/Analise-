
# coding: utf-8

# # ANÁLISE DE DADOS DA PREFEITURA DE INDIAL/SC #
# 

# In[32]:


link_original = "http://api.willcode.tech/funcionarios/?USUARIO=USUARIO&SENHA=SENHA_SECRETA&ACAO=LISTAR-TODOS"
link_reduzido = "https://bit.ly/3wlc41V"


# In[33]:


import requests

url = link_reduzido
response = requests.request("GET", url, headers={}, data={})


# In[34]:


print(response.text)


# In[38]:


import ast
import pandas as pd
df = pd.DataFrame.from_dict(ast.literal_eval(response.text))
df


# In[41]:


import urllib.request as urllib_request
from urllib.request import urlopen


# In[42]:


urllib_request.__version__


# In[43]:


import bs4


# In[44]:


bs4.__version__

