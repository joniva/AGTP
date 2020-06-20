#Libraries

import matplotlib.pyplot as plt
import numpy as np

#Getting rid of all of the additional markers on the plot
#for a clean look

plt.rcParams["toolbar"]="None"
plt.axis("off")

#Number of sides the shape has
sides = int(input("How many sides does the shape have: "))

#Creating a list to store all of the functions so I can referer later on to
#them in order to do different calculations

listFunction = [None] * sides
listDoms = [None] * sides
listDomf = [None] * sides

def createShape():

    #For now, this program will only work with linear functions 3*x+1
    #and constant functions (x=5, y=5)

    for i in range(sides):

        #For now, we will use an if statemenent to see what type of function
        #they are inputing, in the GUI it will be a drop down menu

        lineType = input("What type is the function(linear,const_y,const_x): ")
        
        #It looks repetitive at first but by configuring the plots this way
        #we can control individually how we draw each function which simplifies things

        line = input("Input function: ")
        dom_s = float(input("dom_s: "))
        dom_f = float(input("dom_f: "))
        listFunction.append(line)
        listDoms.append(dom_s)
        listDomf.append(dom_f)

        if lineType == "linear":
            x = np.linspace(dom_s,dom_f,100)
            y = eval(line)
            plt.plot(x,y,linewidth=2.5,color="k")
        
        elif lineType == "const_y":
            x = np.linspace(dom_s,dom_f,100)
            y = [line]*100 
            plt.plot(x,y,linewidth=2.5,color="k")

        elif lineType == "const_x":
            y = np.linspace(dom_s,dom_f,100)
            x = [line]*100
            plt.plot(x,y,linewidth=2.5,color="k")

    plt.rcParams['toolbar'] = 'None'
    plt.show()


createShape()



