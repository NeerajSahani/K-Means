import math
import numpy as np
class KMeans:
    def __init__(self, k=2, iters=300):
        self.k=k
        self.iter = iters

    def eucledian_distance(self, x ,y):
	    return math.sqrt(((x[0]-y[0])**2 + (x[1]-y[1])**2))

    def fit(self, data):
        self.data = data
        if len(self.data) < self.k:
            print('dataset is too short')

    def cluster_centers_(self):
        mean=[i for i in self.data[:self.k]]
        dist=[0 for i in range(self.k)]
        prev=None
        for iterations in range(self.iter):
            self.cluster=[[] for i in range(self.k)]
            for i in range(len(self.data)):
                for j in range(self.k):
                    dist[j] = self.eucledian_distance(mean[j],self.data[i])
                self.cluster[dist.index(min(dist))].append(self.data[i])
            for i in range(self.k):
                mean[i]=np.mean(np.array(self.cluster[i]),0)
                

        return mean

    def labels_(self):
        label=[]
        for i in self.data:
            for j in range(len(self.cluster)):
                    if self.cluster[j].count(i) !=0:
                            label.append(j)
        return label


if __name__ == '__main__':
  alg=KMeans(2)
  data=[[1,2],[3,1.5],[2,1.9],[3,4],[6,7],[5,8],[7,6.5],[5,6]]
  alg.fit(data)
  c=alg.cluster_centers_()
  l=alg.labels_()
  print(c, l)
