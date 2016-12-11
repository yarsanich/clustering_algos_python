import numpy as np
import random
import matplotlib.pyplot as plt

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        for i in enumerate(mu):
            print (x,i[1],np.linalg.norm(x-mu[i[0]]))
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(list(X), K)
    mu = random.sample(list(X), K)
    #print (oldmu,mu)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def init_board():
    X = np.array([[1,1],[1,2],[2,2],[2,7],[1,7],[11,4],[5,4],[4,5],[3,5],[0,1]])
    return X

if __name__ == '__main__':
    #find_centers(init_board(),3)
    print(find_centers(init_board(),5)[1])
    clasters = find_centers(init_board(),5)[1]
    x_list = [x[0] for x in init_board()]
    y_list = [y[1] for y in init_board()]

    plt.plot(x_list,y_list,"ro")
    plt.axis([-5,20,-5,20])
    #plt.show()

    for claster in clasters:
        xx = list()
        yy = list()
        for member in clasters[claster]:
            xx.append(member[0])
            yy.append(member[1])
        r = lambda: random.randint(0,255)
        plt.plot(xx,yy,'#%02X%02X%02X' % (r(),r(),r()),linestyle='None',marker="s")

    plt.axis([-5,20,-5,20])
    plt.show()
