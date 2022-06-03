# importing required modules
import matplotlib.pyplot as plt
import numpy as np
 
# function to generate coordinates
def create_plot(ptype):
    # setting the x-axis values
    x = np.arange(-10, 10, 1)
    y = 2*x**+7*x-5
    
    plt.xlabel("Os X")
    plt.ylabel("Os Y")
    plt.title("Riesenie")
    plt.legend()
    return(x, y)


x, y = create_plot("Riesenie")
plt.scatter(x, y, label = "stars", color ='b', marker = "o", s = 20) 


plt.show()