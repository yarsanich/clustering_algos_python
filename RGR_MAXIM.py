import math
import numpy as np
from RGR_EVRISTIKA import calculateDistance
import matplotlib.pyplot as plt

if __name__=="__main__":
        print("Enter your points in (x,y);(x1,y1);(...,...);(x_n,y_n) sequence")
        points = input()

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

        clasters = []
        clasters.append((x_list[0],y_list[0]))
        L_index = 0
        L = 0
        LL = []
        D_i = [[]]
        start_point = [x_list[0],y_list[0]]
        for i in range(0,len(x_list)):
            D_i[0].append(calculateDistance(start_point[0],start_point[1],x_list[i],y_list[i]))
            if (calculateDistance(start_point[0],start_point[1],x_list[i],y_list[i])>L and i!=0):
                L = calculateDistance(start_point[0],start_point[1],x_list[i],y_list[i])
                L_index = i
        LL.append(L)
        start_point = [x_list[L_index],y_list[L_index]]
        #print (start_point)
        while(True):
            D_i.append([])
            cur_index = len(clasters)
            for i in range(0,len(x_list)):
                D_i[cur_index].append(calculateDistance(start_point[0],start_point[1],x_list[i],y_list[i]))

            print (D_i[1])
            max_A = 0
            new_claster_index = 0
            D_i = [list(i) for i in zip(*D_i)]
            A_array = []
            for i in range(0,len(D_i)):
                min_index = 0
                A_min = 1e9
                for j in range(0,cur_index):
                        #print (D_i[i])
                        if (A_min > D_i[i][j] and D_i[i][j]>0):
                            A_min = D_i[i][j]
                A_array.append(A_min)
            #print (A_array)
            for j in range(len(A_array)):
                if A_array[j] > max_A and A_array[j]!=1e9 and (x_list[j],y_list[j]) not in clasters:
                    max_A = A_array[j]
                    new_claster_index = j
            L_cur = max_A
            LL.append(L_cur)
            clasters.append((x_list[new_claster_index],y_list[new_claster_index]))
            start_point = [x_list[new_claster_index],y_list[new_claster_index]]
            if (L_cur>0.5*(sum(LL)/(cur_index))):
                break
            D_i = [list(i) for i in zip(*D_i)]
        print (clasters)

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
