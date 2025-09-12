class Edge:

    def __init__(self,relation_name:str, from_vertex: "Vertex", to_vertex:"Vertex"):
        self.relation_name = relation_name
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
