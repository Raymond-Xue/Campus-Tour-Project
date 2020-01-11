AUTHOR: Daihao Xue
DATE: 12/11/2019


Run the Program:
This project was wrote by Python. Please enter 'python Map.py' to run the program. 
Please enter start point and end point with their label. Like 'DDD', 'AAA', 'A8', 'J'. Black
Hole 'XXX' is not included in my program. If you enter an endpoint, you will lead to a
dijkstra algorithm, if you simply tapped return, you will be led to Prim algorithm.
Please enter travel method with 'walk' or 'skate'.
Please enter time method with 0 or 1. 0 means not to minimize time and will return a 
minimum distance path. 1 will return a minimum time path.

Explanation of my implementation:
For the framework, I implemented the class Vertex and the class Graph.
For the data structure, I implemented the Heap with reference to the python source
code heapq.
For part 1, I implemented Dijkstra algorithm for the shortest path algorithm.
For part 2, I implemented Prim's algorithm for MST and DFS to traverse it.
I am still working on finding the Hamilton path and Hamilton Cycle but I have not
worked it out. All codes I have not are included in initialization.py.

File Included:
Read_files.py: Read vertex and edge file from source data files.
time_calcuation.py: Calculate the time cost on each edge according to the travel
		method and the road type.
initialization.py: All the data structures and algorithms are implemented here.
Map.py: Use this file to run the code and output to file.
Dijkstra_Output.txt: Results of 12 inputs are included.
OutputTourP.txt:  Minimal spanning tree using Prim's Algorithm, starting at vertex J.
OutputTourPP.txt: Pre-order traversal of the Prim spanning tree to form a cycle.
OutputTourJ.txt:  My shortest distance cycle tour, no skateboard, starting at vertex J.
OutputTourJS.txt: My minimum time cycle tour, with skateboard, starting at vertex J.
OutputPathJC.txt: My shortest distance path tour, no skateboard, vertex J to castle.
OutputPathJCS.txt: My minimum time path tour, with skateboard, vertex J to castle.
plotting.txt: used to plot route on the full map.
plotting_cropped.txt: used to plot route on the cropped map.
dijkstra.txt: Single route output according to your input for dijkstra.
prim.txt: Single route output according to your input for prim.