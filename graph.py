from vertex import Vertex
import json
import uuid

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

        v1.connect(relation_name=relation_name, vertex=v2)

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
        return self.vertices.get(name).printAll()

    def getNeighborsByRelation(self, from_vertex: str, relation_name:str):

        v = self.vertices[from_vertex]
        return [edge.to_vertex for edge in v.out_edges if edge.relation_name == relation_name]

    def showGraph(self):
        for vertex in self.vertices.values():
            vertex.printAll()

    def exportToJson(self, filename: str):
        data = {
            "vertices": [],
            "edges": []
        }

        for v in self.vertices.values():
            data["vertices"].append({
                "name": v.name,
                "properties": v.properties
            })

            for edge in v.out_edges:
                data["edges"].append({
                    "from": v.name,
                    "to": edge.to_vertex.name,
                    "relation": edge.relation_name
                })

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Grafo exportado para {filename}")