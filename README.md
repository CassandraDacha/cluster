# CSC3022F ML Assignment 1 Clustering

We were tasked to create a  program that uses the K-means algorithm to cluster the following 8 examples into 3 clusters. 

## Files contained in the folder
cluster.py
output.txt
Makefile
requirements.txt

## How to compile the program
	make
## How to run the test program
	make run 
##Example usage:
	make run command should output such results to the txt file named output.txt
	Iteration 0

	Cluster 1: 1
	Centroid: (2, 10)

	Cluster 2: 3, 4, 5, 6, 8
	Centroid: (5, 8)

	Cluster 3: 2, 7
	Centroid: (1, 2)

	Iteration 1

	Cluster 1: 1, 8
	Centroid: (2.0, 10.0)

	Cluster 2: 3, 4, 5, 6
	Centroid: (6.0, 6.0)

	Cluster 3: 2, 7
	Centroid: (1.5, 3.5)

	Iteration 2

	Cluster 1: 1, 4, 8
	Centroid: (3.0, 9.5)

	Cluster 2: 3, 5, 6
	Centroid: (6.5, 5.25)

	Cluster 3: 2, 7
	Centroid: (1.5, 3.5)

	The total number of iterations is 3

#NOTE: Test are saved in the test folder

## License
[MIT](https://choosealicense.com/licenses/mit/)
