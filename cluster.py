import numpy as np
import math

#Stores the number of iterations
count = 0

#Function that takes in the initial seed values as well as an array containing the points to be clustered. It then computes the euclidean distance between each point and each seed. It then adds the point to the nearest cluster based on the least euclidean distance. This is done recursively until the same points are assigned to each cluster in consecutive rounds.
def k_means(center1,center2,center3,coordinates):
  cluster_1 = []
  name_1 = []
  cluster_2 = []
  name_2 = []
  cluster_3 = []
  name_3 = []
  center_1 = center1
  center_2 = center2
  center_3 = center3
  global count
  for x in range(8):
    eDistance1 = math.dist(center_1,coordinates[x])
    eDistance2 = math.dist(center_2,coordinates[x])
    eDistance3 = math.dist(center_3,coordinates[x])
    min_dist = min(eDistance1,eDistance2,eDistance3)
    if min_dist == eDistance1:
      cluster_1.append(coordinates[x])
      name_1.append(x+1)
    if min_dist == eDistance2:
      cluster_2.append(coordinates[x])
      name_2.append(x+1)
    if min_dist == eDistance3:
      cluster_3.append(coordinates[x])
      name_3.append(x+1) 
 #Computing the mean value of each cluster to get the new centoid
  c1 = list(np.mean(cluster_1, axis = 0))
  c2 = list(np.mean(cluster_2, axis = 0))
  c3 = list(np.mean(cluster_3, axis = 0))
  
  f = open("output.txt", "a")
  #Checking if the current centroid is equal to the new centroid.This is the convergence point of the algorithm
  if c1 == center_1 and c2 == center_2 and c3 == center_3:
  	f.write("The total number of iterations is " + str(count))
  else:
  	print(center_1)
  	print(center_2)
  	print(center_3)
  	f.write("Iteration " + str(count) + "\n\n")
  	count = count + 1
  	f.write("Cluster 1: " + str(name_1).replace('[','').replace(']','') +"\n")
  	f.write("Centroid: " + str(tuple(center_1)) + "\n\n")
  	f.write("Cluster 2: " + str(name_2).replace('[','').replace(']','') +"\n")
  	f.write("Centroid: " + str(tuple(center_2)) + "\n\n")
  	f.write("Cluster 3: " + str(name_3).replace('[','').replace(']','') +"\n")
  	f.write("Centroid: " + str(tuple(center_3)) + "\n\n")
  	center_1 = c1
  	center_2 = c2
  	center_3 = c3
  	f.close()
  	k_means(center_1,center_2,center_3,coordinates)
  	print(count)
  	
coordinates = [[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]
#When running K-means, set the initial seeds (initial centroid of each cluster) as examples 1, 4 and 7.
c_1 = [2,10]
c_2 = [5,8]
c_3 = [1,2]
#Call to the function k_means that takes in the initial seed values and creates 3 clusters for the points given
k_means(c_1,c_2,c_3,coordinates)
