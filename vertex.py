from edge import Edge
class Vertex:
    
    def __init__(self, name:str, properties: dict):
        self.name = name
        self.properties  = properties
        self.in_edges:list[Edge] = []
        self.out_edges:list[Edge] = []

    def connect(self,name:str, vertex: "Vertex"):

        edge = Edge(relation_name=name, from_vertex=self, to_vertex=vertex)
        self.out_edges.append(edge)
        vertex.in_edges.append(edge)

    def update(self, new_properties: dict = None, new_name: str = None):

        if new_properties:
            self.properties.update(new_properties)
        if new_name:
            self.name = new_name

    def delete(self):

        for edge in list(self.in_edges):
            edge.from_vertex.out_edges.remove(edge)
        for edge in list(self.out_edges):
            edge.to_vertex.in_edges.remove(edge)
    
    def printAll(self):
        print(f"name: {self.name}")
        print(f"properties: {self.properties}")
        for edge in self.in_edges:
            print(f" in relation: {edge.relation_name}\n from: {edge.from_vertex.name}")
        for edge in self.out_edges:
            print(f"out relation: {edge.relation_name}\n to: {edge.to_vertex.name}")

    