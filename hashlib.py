#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib


# In[2]:


print(hashlib.algorithms_available)


# In[4]:


crypt = hashlib.sha256()
crypt.update(b"hello")
print(crypt.hexdigest())#hexdigest () Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits.
print(crypt.digest_size)


# In[ ]:


#if value is found in dictionary then it is possible to hash decrypt


# In[10]:


#using salt in hash


# In[ ]:


https://docs.python.org/3/library/hashlib.html


# In[11]:


import hashlib,binascii # Convert between binary and ASCII


# In[ ]:


# hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)


# In[18]:


dk = hashlib.pbkdf2_hmac('sha256',b'hello',b'kishan',100000,dklen = 64)
print(binascii.hexlify(dk))


# In[ ]:




