import numpy as np
import matplotlib.pyplot as plt
import random
nums = [] 
def gaussian(sigma,mu,x):
    return (1/np.sqrt(2*np.pi*sigma*sigma))*np.exp(-(x-mu)*(x-mu)/(2*sigma*sigma))
sigma = 1
mu =0

xi = np.linspace(-100,100,10000000)
yi = gaussian(sigma,mu,xi)

for i in range(10000): 
	temp = random.gauss(mu, sigma) 
	nums.append(temp) 
nums = np.array(nums)     
plt.xlim(-5,5)
plt.hist(nums, bins = 200,density = True)     
plt.plot(xi,yi)
plt.show()