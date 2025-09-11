from vertex import Vertex

class Graph:

    def __init__(self, name:str):
        self.name = name
        self.vertices:dict[str, Vertex] = {}

    def addVertex(self, name:str, properties:dict):

        if name in self.vertices:
            raise ValueError(f"Vertex {name} already exists")
                
        vertex = Vertex(name = name, properties=properties)

        self.vertices[name] = vertex

    def connectVertices(self, relation_name:str, from_vertex:str, to_vertex:str):

        v1 = self.vertices[from_vertex]
        v2 = self.vertices[to_vertex]

        v1.connect(name=relation_name, vertex=v2)

    def updateVertex(self, name: str, new_properties: dict = None, new_name: str = None):

        if name not in self.vertices:
            raise ValueError(f"Vertex {name} not found")
        
        vertex = self.vertices[name]

        vertex.update(new_name=new_name, new_properties=new_properties)

        if new_name:
            self.vertices[new_name] = self.vertices.pop(name)
    
    def deleteVertex(self, name: str):

        if name not in self.vertices:
            raise ValueError(f"Vertex {name} not found")
        
        vertex = self.vertices[name]

        vertex.delete()

        del self.vertices[name]

    

    def updateRelation(self, from_vertex: str, to_vertex: str, new_name: str = None):

        v1 = self.vertices[from_vertex]

        for edge in v1.out_edges:
            if edge.to_vertex.name == to_vertex:
                if new_name:
                    edge.name = new_name
                return
        raise ValueError("Edge not found")
    
    def disconnect(self, from_vertex: str, to_vertex: str):
        
        v1 = self.vertices[from_vertex]
        v2 = self.vertices[to_vertex]

        edge_to_remove = None

        for edge in v1.out_edges:
            if edge.to_vertex == v2:
                edge_to_remove = edge
                break

        if edge_to_remove:
            v1.out_edges.remove(edge_to_remove)
            v2.in_edges.remove(edge_to_remove)

    def getVertex(self, name: str) -> "Vertex":
        return self.vertices.get(name)

    def getVertices(self, filter_fn=None):

        if filter_fn:
            return [v for v in self.vertices.values() if filter_fn(v)]
        return list(self.vertices.values())

    def getNeighbors(self, name: str):

        v = self.vertices[name]
        return [edge.r_vertex for edge in v.out_edges]
