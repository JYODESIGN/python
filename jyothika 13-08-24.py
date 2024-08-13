#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nterms=int(input("how many terms"))


# In[ ]:


n1,n2=0,1
count=0


# In[ ]:


if nterms<=0:
    print("enter a positive integer")


# In[ ]:


print('fibonacci series:')


# In[3]:


n = 10
num1 = 0
num2 = 1
next_number = num2 
count = 1

while count <= n:
print(next_number, end=" ")
count += 1
num1, num2 = num2, next_number
next_number = num1 + num2
print(fibonacci)



# In[5]:


def Fibonacci(n):
 if n < 0:
  print("Incorrect input")
 elif n == 0:
  return 0
 elif n == 1 or n == 2:
  return 1
 else:
  return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))


# In[11]:


def rightrotate (lists,num):
    output_list=[]
    for item in range(len(lists)-num,len(lists)):
        outut_list.append(lists[item])
    for item in range(0,len(lists)-num):
        output_list.append(lists[item])
        
        return output_list
    
    rotate_num=3
    list_1=[1,2,3,4,5,6]
    print(rightrotate(lit_1,rotate_num))


# In[12]:


rightrotate (78,9)


# In[13]:


n=3
list_1=[1,2,3,4,5,6]
list_1=(list_1[len(list_1)-n:len(list_1])+list_1[0:len(list_1)]
               print(list_1)


# In[ ]:




