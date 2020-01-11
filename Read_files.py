# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:35:04 2019

@author: 薛代豪
"""
class ReadFile:
    
    #read vertex file
    def read_vertex_file(file_name):
        vertex_file = open(file_name, 'r')
        vertices = []
        for line in vertex_file:
            if len(line) > 10 and (line[0] + line[1]) !='//':
                tmp = []
                elements = line.split()
                tmp.append(int(elements[0]))
                tmp.append(elements[1])
                tmp.append(int(elements[2]))
                tmp.append(int(elements[3]))
                name_list = elements[4:]
                tmp.append(" ".join(name_list))
                vertices.append(tmp)
        vertex_file.close()
        return vertices

    #read edge file
    def read_edge_file(file_name):
        edge_file = open(file_name, 'r')
        edges = []
        for line in edge_file:
            if len(line) > 10 and (line[0] + line[1]) !='//':
                tmp = []
                elements = line.split()
                tmp.append(int(elements[0]))
                tmp.append(elements[1])
                tmp.append(elements[2])
                tmp.append(int(elements[3]))
                tmp.append(int(elements[4]))
                tmp.append(int(elements[5]))
                tmp.append(int(elements[6]))
                tmp.append(elements[7])
                tmp.append(elements[8])
                name_list = elements[9:]
                tmp.append(" ".join(name_list))
                edges.append(tmp)
        edge_file.close()
        return edges
#print(ReadFile.read_edge_file('MapDataEdges.txt'))
