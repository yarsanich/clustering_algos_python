import matplotlib.pyplot as plt
import math
import random
import numpy

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

class Claster:
    def __init__(self,index,members):
        self.index = index
        self.members = members
        self.main_member = members[0]

    def getMembers(self):
        print(self.members)

    def getIndex(self):
        print("Index of claster",self.index)

    def addMember(self,new_member):
        self.members.append(new_member)

if __name__ == "__main__":
    print("Enter your points in (x,y);(x1,y1);(...,...);(x_n,y_n) sequence")
    points = input()
    print("Enter your T(edge number)")
    T = int(input())


    points = points.split(';')
    x_list = list()
    y_list = list()
    for point in points:
        x,y = point.split(',')
        x = x.replace('(','')
        y = y.replace(')','')
        x = int(x)
        y = int(y)
        x_list.append(x)
        y_list.append(y)


    first_claster = Claster(1,[[x_list[0],y_list[0]]])
    clasters = list()
    clasters.append(first_claster)
    for i in range(0,len(x_list)):
        for j in range(0,len(clasters)):
            current_claster = clasters[j]
            flag = False
            if (i!=j and calculateDistance(x_list[i],y_list[i],current_claster.main_member[0],current_claster.main_member[1])<T):
                flag = True
                clasters[j].addMember([x_list[i],y_list[i]])
                print("Distance between %i %i %f < T" % (i,j,calculateDistance(x_list[i],y_list[i],current_claster.main_member[0],current_claster.main_member[1])))
                print("Then add to claster %i" % j)
                break
        if (not flag):
            print("All distances greater then T create new claster %i" % (len(clasters)+1))
            new_claster = Claster(len(clasters)+1,[[x_list[i],y_list[i]]])
            clasters.append(new_claster)

    '''
    for claster in clasters:
        claster.getMembers()
        claster.getIndex()
    '''

    plt.plot(x_list,y_list,"ro")
    plt.axis([-5,20,-5,20])
    plt.show()

    for claster in clasters:
        xx = list()
        yy = list()
        for member in claster.members:
            xx.append(member[0])
            yy.append(member[1])
        print(xx,yy)
        r = lambda: random.randint(0,255)
        plt.plot(xx,yy,'#%02X%02X%02X' % (r(),r(),r()),linestyle='None',marker="s")

    plt.axis([-5,20,-5,20])
    plt.show()
