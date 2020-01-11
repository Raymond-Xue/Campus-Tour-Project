# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:31:40 2019

@author: 薛代豪
"""
from collections import defaultdict

class Vertex:
    def __init__(self, label):
        self.label = label                      #label of vertex(deal with input)
        self.adjacent = defaultdict(int)        #neighbors of each vertex
        self.adjacent_MST = defaultdict(int)    #children of each vertex in MST
        self.dist_src = 2 ** 30                 #distance to source
        self.dist_pre = 2 ** 30                 #distance to parent
        self.pre = None                         #record vertex's parent
        self.visited = 0                        #record whether a vertex has been visited

    #add neighbors to dictionary
    def add_adj(self, adj, weight):
        self.adjacent[adj] = weight

    
class Graph:
    def __init__(self):
        self.vertex_list = defaultdict(float)   #vertices in the graph
        self.vertex_num = 0                     #num of vertices in the graph
        self.total_dist = 0                     #record total tour distance of prim
        self.route = []                         #record the route of tour

    #add vertex to graph.
    def add_vertex(self, name):
        if name not in self.vertex_list.keys():
            self.vertex_num += 1
            new_vertex = Vertex(name)
            self.vertex_list[name] = new_vertex

    #get vertex from graph
    def get_vertex(self, name):
        if name.label in self.vertex_list.keys():
            return self.vertex_list[name.label]
        else:
            return None

    #add edge to the graph. If endpoints of the edge not in the
    #graph, add the endpoints to the graph first.
    def add_edge(self, start, end, weight):
        if start not in self.vertex_list:
            self.add_vertex(start)
        if end not in self.vertex_list:
            self.add_vertex(end)
        self.vertex_list[start].add_adj(self.vertex_list[end], weight)

    #reload the iterator for future operation
    def __iter__(self):
        return iter(self.vertex_list.values())

    #reload in operation for future operation
    def __contains__(self, n):
        return n in self.vertex_list
   
class Heap:
    def __init__(self, graph_list):
        self.graph_list = graph_list    #pass in the graph to form a heap
        self.array = []                 #vertices in the graph
        self.size = 0                   #size of the heap
    
    #swap nodes in the heap. Usually call this function while sorting the heap
    def swap_node(self, v1, v2):
        tmp = self.array[v1]
        self.array[v1] = self.array[v2]
        self.array[v2] = tmp
        
    #get the vertex according to the index
    def get_vidx(self, i):
        index = self.array[i]
        return self.graph_list.get_vertex(index)
        
    #Percdown while deletemin or sorting
    def Percdown(self, i):
        endpos = self.size - 1
        i = int(i)
        while i < endpos:
            lchild = 2 * i + 1
            rchild = 2 * i + 2
            if lchild >= endpos:
                break
            vi = self.get_vidx(i)
            vr = self.get_vidx(rchild)
            vl = self.get_vidx(lchild)
            
            #select the smaller one from left and right child as the child
            #to swap
            if vl.dist_src <= vr.dist_src:
                childpos = lchild
            else:
                childpos = rchild
            
            val = vi.dist_src 
            child_vertex = self.get_vidx(childpos)
            #if value of current is smaller than any child, stop the 
            #Percdown procedure.
            if val < child_vertex.dist_src:
                break
            
            self.swap_node(childpos, i)
            i = childpos
        
    #Perup while intert
    def Percup(self, i):
        while i > 0:
            vi = self.get_vidx(i)
            #get index of parent node
            parentpos = (i - 1) // 2
            vp = self.get_vidx(parentpos)
            #if current node is smaller than parent, swap.
            if vi.get_dist_src() < vp.get_dist_src():
                self.swap_node(parentpos, i)
                i = parentpos
            else:
                break
    
    #Insert a vertex into the heap
    def Insert(self, i):
        self.array.append(i)
        self.size += 1
        self.Percup(self.size  - 1)
        
    #Delete the node with smallest value.
    def Deletemin(self):
        if self.size > 1:
            self.swap_node(0, self.size - 1)
            del self.array[self.size - 1]
            self.size -= 1
            self.Percdown(0)
        elif self.size == 1:
            del self.array[0]
            self.size -= 1
    
    #build the heap
    def Heap_Construction(self, adj_list):
        for item in adj_list:
            self.size += 1
            self.array.append(item)
        i = self.size / 2
        while i >= 0:
            self.Percdown(i)
            i -= 1
            
#Dijkstra algorithm to find the shortest route between two nodes
def dijkstra(G, start):
    priority = G
    start.dist_src = 0
    H = Heap(priority)
    H.Heap_Construction(priority)
    #Traverse the heap
    while H.size > 0:
        changed = False
        current = H.array[0]
        H.Deletemin()
        #Traverse the neighbor of corrent node.
        for vertex_tmp in current.adjacent:
            dist_tmp = current.dist_src + current.adjacent[vertex_tmp]
            #Update distance to source if route with current is 
            #shorter than the original one.
            if dist_tmp < vertex_tmp.dist_src:
                vertex_tmp.dist_src = dist_tmp
                vertex_tmp.pre = current
                changed = True
        #If distance to source is updated in any point, re-sort the heap
        if changed:
            i = H.size / 2
            while i >= 0:
                H.Percdown(i)
                i -= 1
        
#Prim algorithm to generate the MST       
def prim(G, MST, start):
    priority = G
    start.dist_src = 0
    start.dist_pre = 0
    H = Heap(priority)
    H.Heap_Construction(priority)
    src_set = []
    m = 0
    #Traverse the heap
    while H.size > 0:
        if m == 0:
            current = H.array[0]
        m += 1
        H.Deletemin()
        #build a set of visited vertices
        src_set.append(current)
        current.visited = 1
        MIN = 2 ** 30
        endpoint = None
        startpoint = None
        children = []
        #Get all the possible edges related to the visited set.
        for item in src_set:
            for vertex_tmp in item.adjacent:
                if vertex_tmp.visited == 0:
                    children.append([item, vertex_tmp])
        #Choose the minimum edge and add the endpoint to the set.
        for item in children:
            if item[0].adjacent[item[1]] < MIN:
                MIN = item[0].adjacent[item[1]]
                startpoint = item[0]
                endpoint = item[1]
        #re-sort the heap             
        i = H.size / 2
        while i >= 0:
            H.Percdown(i)
            i -= 1
        #Add the chosen edge to MST
        if endpoint != None and startpoint != None:
            endpoint.pre = startpoint
            MST.add_edge(startpoint, endpoint, MIN)
            MST.add_edge(endpoint, startpoint, MIN)
            startpoint.adjacent_MST[endpoint] = MIN
            endpoint.adjacent_MST[startpoint] = MIN   
        src_set.append(endpoint)
        current = endpoint

#Use the Pre information in Vertex to trace back and find the whole route
def get_route(END):
    current = END
    R = [END]
    while current.pre:
        current = current.pre
        R.append(current)
    #Reverse the original route list.
    #This is because we get the route from the destination to the source.
    R.reverse()
    return R
#Pre-order traverse the MST
def DFS(MST, SRC):
    SRC_V = None
    #Set the current vertex visited
    for vertex in MST.vertex_list:
        if vertex.label == SRC:
            vertex.visited = 1
            SRC_V = vertex
    list_tmp = SRC_V.adjacent_MST
    #Traverse each children of current point, recurrently call the DFS function
    for child in list_tmp:
        if child.visited == 0:
            #Record the route if the child is not visited
            MST.route.append([SRC_V.label, child.label])
            #Add the cost of the edge to total distance.
            #This could be the time or the distance
            MST.total_dist += SRC_V.adjacent_MST[child]
            child_label = child.label
            DFS(MST,child_label)
            #Record the back edges while DFS.
            #This back edge is different from the traditional difinition
            #of back edge of DFS Tree. This is to record the process of
            #backtracking.
            MST.route.append([child.label, SRC_V.label])

#Judge whether a point is available while looking for the Hamilton Path.
def unvisited(v, last_v, path):
    if v.pre == last_v.pre:
        return False
    if v in path:
        return False
    return True

#Looking for the Hamilton Path.
#There are still bugs in it.
def Hamilton(SRC, G, path):
    priority = G
    H = Heap(priority)
    H.Heap_Construction(priority)
    for i in range(G.vertex_num - 1):
        print(i)
        for v in H.array: 
            if len(path) > 0 and v != SRC:
                v.pre = SRC
                if unvisited(v, path[-1], path) == True: 
                    path.append(v)

                    if Hamilton(v, G, path) == True: 
                        return True
                    del path[-1]
        return False
#Call the Hamilton Function to print the path.
def HamPath(SRC, G): 
    path = [SRC]
  
    if Hamilton(SRC, G, path) == False: 
        print("No Hamilton Path")
        return False
  
    print(path)   



    


        

                
                
