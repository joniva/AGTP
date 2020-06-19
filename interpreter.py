#Libraries

import matplotlib.pyplot as plt
import numpy as np

#Getting rid of all of the additional markers on the plot
#for a clean look

plt.rcParams["toolbar"]="None"
plt.axis("off")

#Number of sides the shape has
sides = 1

def createShape():

    #For now, this program will only work with linear functions 3*x+1
    #and constant functions (x=5, y=5)

    for i in range(sides):

        #For now, we will use an if statemenent to see what type of function
        #they are inputing, in the GUI it will be a drop down menu

        lineType = input("What type is the function(linear,const_y,const_x): ")

        if lineType == "linear":
            line = input("Input function: ")
            dom_s = float(input("dom_s: "))
            dom_f = float(input("dom_f: "))
            x = np.linspace(dom_s,dom_f,100)
            y = eval(line)
            plt.plot(x,y,linewidth=2.5,color="k")
        
        elif lineType == "const_y":
            line = float(input("Input function: "))
            dom_s = float(input("dom_s: "))
            dom_f = float(input("dom_f: "))
            x = np.linspace(dom_s,dom_f,100)
            y = [line]*100 
            plt.plot(x,y,linewidth=2.5,color="k")

        elif lineType == "const_x":
            line = float(input("Input function: "))
            dom_s = float(input("dom_s: "))
            dom_f = float(input("dom_f: "))
            y = np.linspace(dom_s,dom_f,100)
            x = [line]*100
            plt.plot(x,y,linewidth=2.5,color="k")

    plt.rcParams['toolbar'] = 'None'
    plt.show()

createShape()



