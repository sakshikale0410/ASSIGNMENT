#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT

# 1]. What is the difference between set and dictionary  , Explain with the suitable example

# In[25]:


S={1,2,3,4,5,6}
print(S)
d={'sky':'sun','garden':'flower'}
print(d)


# 2]Write a program to print the following pattern 

# In[26]:


n=3
for i in range(n):
    print(' ',end=' ')
    for j in range(i+1):
        print('*',end='')
    print()


# 3]Write a program to print n natural number in ascending order using a while loop?

# In[32]:


i=1
n=4
while i<=n:
    print(i)
    i+=1


# 4] Write a program in Python to swap between two numbers without using a third variable

# In[2]:


x=0
y=1
x,y=y,x
print(x)
print(y)


# 5] How to create a function with arguments in python?

# In[5]:


def student(name,grades):
    print(f'Name:{name}  Grade:{grades}')
student('sakshi kale','A')


# 6]Display a square of numbers from 1 to 10 using list comprehension

# In[4]:


numbers=list(range(1,11))
squares = [value ** 2 for value in numbers]
print(squares)


# 7. What is polymorphism? Explain with example( class)

# In[ ]:


class Animal:
    def speak(self):
        print('i am an animal')
class


# 8. Explain conditional probability with example?

# In[1]:


class Shape:
    def area(self,radius):
        return 3.14 * radius * radius
     
    def area(self,l,b):
        return l * b
    
o = Shape()
print(o.area(5,4))


# 9]Explain Emphirical rule  with diagram .

# In[ ]:


In a normal distribution, 68% of the observations fall within +/- 1 standard deviation from the mean


Mean +/- standard deviations	Percentage of data contained
1	                                 68%
2	                                 95%
3	                                 99.7%

EXAMPLE

Assume that a pizza restaurant has a mean delivery time of 30 minutes and a standard deviation of 5 minutes. 

Using the Empirical Rule, we can determine that 68% of the delivery times are between 25-35 minutes (30 +/- 5),
95% are between 20-40 minutes (30 +/- 2*5), and 99.7% are between 15-45 minutes (30 +/-3*5). 

The chart below illustrates this property graphically.


# 10.What is Hypothesis Testing ? What is the Role of p value in HT?

# In[ ]:


H0=ALL STUDENTS HAVE GRADE A  #NULL HYPOTHESIS
H1=NOT ALL STUDENTS HAVE GRADE A   #ALTERNATIVE HYPTHESIS

WE CREATE HO TO REJECT IT. WE APPLY TEST ON SOME SAMPLE AND MAKE INFERENCE ABOUT POPULATION .

WE FIND P VALUE AFTER APPLYING Z OR T TEST AT 95% LEVEL OF SIGNIFICANCE

IF P VALUE IS LESS THAN 0.05    WE REJECT NULL HYPOTHESIS
IF P VALUES IS GREATER THAN 0.05  WE FAIL TO REJECT NULL HYPOTHESIS




# Q2) List all the probability distributions with example?       5*1 = 5

# 1] EXPONENTIAL DISRTIBUTION 
#    Length of time between metro arrivals,
#    Length of time between arrivals at a gas station
#    The life of an Air Conditioner
#    
# 2]POISSON DISTRIBUTION
#     The number of emergency calls recorded at a hospital in a day.
#     The number of thefts reported in an area on a day.
#     The number of customers arriving at a salon in an hour.
#     
# 3]BERNOULLI DISTRIBUTION
#     answering the quiz,voting
#     
# 4]BINOMIAL DISTRIBUTION 
#    testing a drug
#    participating lucky draw
#    
# 5]NORMAL DISTRIBUTION
#   technical stock market
#   IQ
#   blood pressure
