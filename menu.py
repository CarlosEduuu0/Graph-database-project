from graph import Graph

def menu():
    graph = Graph(name="meu grafo")
    while(True):
        print("===== Neo4j =====")
        user_input = input("\n\n\n1) adicionar vertice\n2) conectar vertices\n3) atualizar vertices\n4) deletar vertice\n5) atualizar conexao\n6) desconectar vertices\n7) printar grafo\n\n\n")

        if user_input == "sair":
            break
        elif user_input == "1":

            vertex_name = input("digite o nome do vertice\n")
            properties_size = int(input("quantas propriedades terá o seu vertice?\n"))
            vertex_properties = {}
            for i in range(properties_size):
                key = input("digite o nome da propriedade\n")
                value = input("digite o valor da propriedade\n")
                vertex_properties[key] = value
            graph.addVertex(name= vertex_name, properties=vertex_properties)

        elif user_input == "2":

            from_vertex = input("de qual vertice vira a conexao\n")
            to_vertex = input("qual vertice recebera a conexao\n")
            relation_name = input("qual sera o nome da relacao\n")
            graph.connectVertices(relation_name=relation_name, from_vertex=from_vertex, to_vertex=to_vertex)
        elif user_input == "3":
            print("funcao nao feita ainda")
        elif user_input == "4":
            print("funcao nao feita ainda")
        elif user_input == "5":
            print("funcao nao feita ainda")
        elif user_input == "6":
            print("funcao nao feita ainda")
        elif user_input == "7":
            graph.showGraph()

if __name__ == "__main__":
    menu()