# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:40:13 2019

@author: 薛代豪
"""
from Read_files import ReadFile
from time_calcuation import Time
import initialization

#Get the output of Dijkstra algorithm
#Pass in the travel method, whether to minimum time, start point and end point
def Dijkstra(walk, time, SRC, END):
    edges = ReadFile.read_edge_file('MapDataEdges.txt')
    vertices = ReadFile.read_vertex_file('MapDataVertices.txt')
    #Generate the Graph
    g = initialization.Graph()
    for vertex in vertices:
        if vertex[1] != 'XXX':
            g.add_vertex(vertex[1])
    for edge in edges:
        if walk == 1 and time == 0:
            g.add_edge(edge[1], edge[2], edge[5])
        if walk == 1 and time == 1:    
            g.add_edge(edge[1], edge[2], Time().time_calculation(edge[5], edge[8], 1))
        if walk == 0 and time == 0:
            if edge[8] == '(x)' or edge[8] == '(F)' or edge[8] == '(U)' or edge[8] == '(D)':
                g.add_edge(edge[1], edge[2], edge[5])
            else:
                edge[9] += '['
                g.add_edge(edge[1], edge[2], edge[5])
        if walk == 0 and time == 1:
            if edge[8] == '(x)' or edge[8] == '(F)' or edge[8] == '(U)' or edge[8] == '(D)':
                g.add_edge(edge[1], edge[2], Time().time_calculation(edge[5], edge[8], 0))
            else:
                edge[9] += '['
                g.add_edge(edge[1], edge[2], Time().time_calculation(edge[5], edge[8], 1))
     
    STRS = ""
    STRE = ""
    #Call the function to get the shortest path.
    initialization.dijkstra(g, g.vertex_list[SRC])
    route = initialization.get_route(g.vertex_list[END])
    
    File = open('dijkstra.txt', 'w', encoding = 'utf-8')
    File1 = open('plotting.txt', 'w', encoding = 'utf-8')
    File2 = open('plotting_cropped.txt', 'w', encoding = 'utf-8')
    File.write('************* WELCOME TO THE BRANDEIS MAP *************\n')
    for v in vertices:
        if v[1] == SRC:
            STRS = v[4]
        if v[1] == END:
            STRE = v[4]
    File.write('Enter start (return to quit): ' + STRS[1:-1] + '\n')
    File.write('Enter finish (or return to do a tour): ' + STRE[1:-1] + '\n')
    if walk == 1:
        File.write('Have a skateboard (y/n - default=n)? n\n')
    else:
        File.write('Have a skateboard (y/n - default=n)? y\n')
    if time == 1:
        File.write('Minimize time (y/n - default=n)? y\n\n')
    else:
        File.write('Minimize time (y/n - default=n)? n\n\n')
    
    dist = 0
    totaltime = 0
    for i in range(len(route) - 1):
        for edge in edges:
            if edge[1] == route[i].label and edge[2] == route[i + 1].label:
                cor_s = []
                cor_e = []
                for vertex in vertices:
                    if vertex[1] == route[i].label:
                        cor_s.append(vertex[2])
                        cor_s.append(vertex[3])
                    if vertex[1] == route[i + 1].label:
                        cor_e.append(vertex[2])
                        cor_e.append(vertex[3])
                #Write to the plotting file to plot the map.
                #Coordinate in the data file is not same as the picture.
                #So reduce the value to make the plotting function useful.
                File1.write(str(cor_s[0] * 0.4578) + ' ')
                File1.write(str(cor_s[1] * 0.4578) + ' ')
                File1.write(str(cor_e[0] * 0.4578) + ' ')
                File1.write(str(cor_e[1] * 0.4578))
                File1.write('\n')
                File2.write(str(cor_s[0] * 0.4578 - 150) + ' ')
                File2.write(str(cor_s[1] * 0.4578 - 125) + ' ')
                File2.write(str(cor_e[0] * 0.4578 - 150) + ' ')
                File2.write(str(cor_e[1] * 0.4578 - 125))
                File2.write('\n')
                dist += edge[5]
                #Write to output according to the sample
                for v in vertices:
                    if v[1] == route[i].label:
                        File.write('From: (' + str(edge[1]) + ') ' + str(v[4]) + '\n')
                        break
                if edge[9] != '""':
                    if edge[9][-1] != '[':
                        File.write('On: ' + str(edge[9]) + '\n')
                    else:
                        File.write('On: ' + str(edge[9][:-1]) + '\n')
                File.write('Walk ' + str(edge[5]) + ' feet in direction ' + str(edge[6]) + ' degrees '+ str(edge[7]) + '.\n')
                for v in vertices:
                    if v[1] == route[i + 1].label:
                        File.write('To: (' + str(edge[2]) + ') ' + str(v[4]) + '\n')
                        break
                if edge[9][-1] == '[':
                    time_tmp = Time().time_calculation(edge[5], edge[8], 1)
                else:
                    time_tmp = Time().time_calculation(edge[5], edge[8], walk)
                if time_tmp < 1.0:
                    File.write('(' + str(time_tmp * 60) + ' seconds)\n')
                else:
                    File.write('(' + str(time_tmp) + ' minutes)\n')
                if edge[9][-1] == '[':
                    totaltime += Time().time_calculation(edge[5], edge[8], 1)
                else:
                    totaltime += Time().time_calculation(edge[5], edge[8], walk)
                break
        File.write('\n')
    File.write('leg = ' + str(i + 1) + ', distance = ' + str(dist) + ' feet, time = ' + str(totaltime) + ' minutes')
    File.close()

#Get the output of Prim algorithm
#Pass in the travel method, whether to minimum time and the start point.
def Prim(walk, time, SRC):
    edges = ReadFile.read_edge_file('MapDataEdges.txt')
    vertices = ReadFile.read_vertex_file('MapDataVertices.txt')
    g = initialization.Graph()
    MST = initialization.Graph()
    #Generate the graph.
    for vertex in vertices:
        #avoid passing in the black hole.
        if vertex[1] != 'XXX':
            g.add_vertex(vertex[1])
    for edge in edges:
        if walk == 1 and time == 0:
            g.add_edge(edge[1], edge[2], edge[5])
        if walk == 1 and time == 1:    
            g.add_edge(edge[1], edge[2], Time().time_calculation(edge[5], edge[8], 1))
        if walk == 0 and time == 0:
            if edge[8] == '(x)' or edge[8] == '(F)' or edge[8] == '(U)' or edge[8] == '(D)':
                g.add_edge(edge[1], edge[2], edge[5])
            else:
                edge[9] += '['
                g.add_edge(edge[1], edge[2], edge[5])
        if walk == 0 and time == 1:
            if edge[8] == '(x)' or edge[8] == '(F)' or edge[8] == '(U)' or edge[8] == '(D)':
                g.add_edge(edge[1], edge[2], Time().time_calculation(edge[5], edge[8], 0))
            else:
                edge[9] += '['
                g.add_edge(edge[1], edge[2], Time().time_calculation(edge[5], edge[8], 1))
     
    STRS = ""
    STRE = ""
    #Get the MST and get the tour route.
    initialization.prim(g, MST, g.vertex_list[SRC])
    for vertex in MST.vertex_list:
        vertex.visited = 0
    initialization.DFS(MST,SRC)
    route = MST.route
    
    File = open('prim.txt', 'w', encoding = 'utf-8')
    File1 = open('plotting.txt', 'w', encoding = 'utf-8')
    File2 = open('plotting_cropped.txt', 'w', encoding = 'utf-8')
    File.write('************* WELCOME TO THE BRANDEIS MAP *************\n')
    for v in vertices:
        if v[1] == SRC:
            STRS = v[4]
    STRE = 'tour'
    File.write('Enter start (return to quit): ' + STRS + '\n')
    File.write('Enter finish (or return to do a tour): ' + STRE + '\n')
    if walk == 1:
        File.write('Have a skateboard (y/n - default=n)? n\n')
    else:
        File.write('Have a skateboard (y/n - default=n)? y\n')
    if time == 1:
        File.write('Minimize time (y/n - default=n)? y\n\n')
    else:
        File.write('Minimize time (y/n - default=n)? n\n\n')
    
    dist = 0
    totaltime = 0
    count_v = []
    for i in range(len(route)):
        count_v.append(route[i][0])
        count_v.append(route[i][1])
        for edge in edges:
            if edge[1] == route[i][0] and edge[2] == route[i][1]:
                cor_s = []
                cor_e = []
                for vertex in vertices:
                    if vertex[1] == route[i][0]:
                        cor_s.append(vertex[2])
                        cor_s.append(vertex[3])
                    if vertex[1] == route[i][1]:
                        cor_e.append(vertex[2])
                        cor_e.append(vertex[3])
                #Write to the plotting file to plot the map.
                #Coordinate in the data file is not same as the picture.
                #So reduce the value to make the plotting function useful.
                File1.write(str(cor_s[0] * 0.4578) + ' ')
                File1.write(str(cor_s[1] * 0.4578) + ' ')
                File1.write(str(cor_e[0] * 0.4578) + ' ')
                File1.write(str(cor_e[1] * 0.4578))
                File1.write('\n')
                File2.write(str(cor_s[0] * 0.4578 - 150) + ' ')
                File2.write(str(cor_s[1] * 0.4578 - 125) + ' ')
                File2.write(str(cor_e[0] * 0.4578 - 150) + ' ')
                File2.write(str(cor_e[1] * 0.4578 - 125))
                File2.write('\n')
                dist += edge[5]
                #Write to output according to the sample
                for v in vertices:
                    if v[1] == route[i][0]:
                        File.write('From: (' + str(edge[1]) + ') ' + str(v[4]) + '\n')
                        break
                if edge[9] != '""':
                    if edge[9][-1] != '[':
                        File.write('On: ' + str(edge[9]) + '\n')
                    else:
                        File.write('On: ' + str(edge[9][:-1]) + '\n')
                File.write('Walk ' + str(edge[5]) + ' feet in direction ' + str(edge[6]) + ' degrees '+ str(edge[7]) + '.\n')
                for v in vertices:
                    if v[1] == route[i][1]:
                        File.write('To: (' + str(edge[2]) + ') ' + str(v[4]) + '\n')
                        break
                if edge[9][-1] == '[':
                    time_tmp = Time().time_calculation(edge[5], edge[8], 1)
                else:
                    time_tmp = Time().time_calculation(edge[5], edge[8], walk)
                if time_tmp < 1.0:
                    File.write('(' + str(time_tmp * 60) + ' seconds)\n')
                else:
                    File.write('(' + str(time_tmp) + ' minutes)\n')
                if edge[9][-1] == '[':
                    totaltime += Time().time_calculation(edge[5], edge[8], 1)
                else:
                    totaltime += Time().time_calculation(edge[5], edge[8], walk)
                break
        File.write('\n')
        '''
        if len(set(count_v)) >= 150:
            break
        '''
    File.write('leg = ' + str(i + 1) + ', distance = ' + str(dist) + ' feet, time = ' + str(totaltime) + ' minutes')
    File.close()

SRC = str(input('Enter start(use the label of of vertices)\n'))
END = str(input('Enter finish(or return to do a tour)\n'))
walk_or_skate = str(input('walk or skate?(Enter walk or skate)\n'))
time = str(input('Do you want to minimize time?(1 to minimize time and 0 not)\n'))
walk = 2 ** 30
if walk_or_skate == 'walk':
    walk = 1
if walk_or_skate == 'skate':
    walk = 0
time = int(time)
if END == '':
    Prim(walk, time, SRC)
else:
    Dijkstra(walk, time, SRC, END)