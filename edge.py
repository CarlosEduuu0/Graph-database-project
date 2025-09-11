from vertex import Vertex
class Edge:

    def __init__(self,name:str, from_vertex:Vertex, to_vertex:Vertex):
        self.relation_name = name
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
