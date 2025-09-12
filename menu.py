from graph import Graph

def menu():
    graph = Graph(name="meu grafo")
    while(True):
        print("===== Neo4j =====")
        user_input = input("\n\n\n1) adicionar vertice\n2) conectar vertices\n3) atualizar vertices\n4) deletar vertice\n5) atualizar conexao\n6) desconectar vertices\n7) printar grafo\n8) procurar vertice\n9) exibir vizinhos\n\n\n")

        if user_input == "sair":
            break
        elif user_input == "1":
            # TRATAR ERROS NO INTERPRETADOR

            vertex_name = input("digite o nome do vertice\n")
            properties_size = int(input("quantas propriedades terá o seu vertice?\n"))
            vertex_properties = {}
            for i in range(properties_size):
                key = input("digite o nome da propriedade\n")
                value = input("digite o valor da propriedade\n")
                vertex_properties[key] = value
            graph.addVertex(name= vertex_name, properties=vertex_properties)

        elif user_input == "2":
            #TRATAR ERROS NO INTERPRETADOR

            from_vertex = input("de qual vertice vira a conexao\n")
            to_vertex = input("qual vertice recebera a conexao\n")
            relation_name = input("qual sera o nome da relacao\n")
            graph.connectVertices(relation_name=relation_name, from_vertex=from_vertex, to_vertex=to_vertex)
        elif user_input == "3":
            #TRATAR ERROS NO INTERPRETADOR
            vertex_newName = None
            vertex_newProperties = None
            vertex_name = input("digite o nome do vertice a ser atualizado\n")
            choice = input("digite 1 para atualizar o nome do vertice")
            if choice == "1":
                choice = 0
                vertex_newName = input("digite o novo nome do vertice\n")

            choice = input("digite 1 para atualizar as propriedades do vertiec")
            if choice == "1":
                properties_size = int(input("quantas propriedades terá o seu vertice?\n"))
                vertex_newProperties = {}
                for i in range(properties_size):
                    key = input("digite o nome da propriedade\n")
                    value = input("digite o valor da propriedade\n")
                    vertex_properties[key] = value
            if vertex_newName and vertex_newProperties:
                graph.updateVertex(name=vertex_name, new_name=vertex_newName, new_properties= vertex_newProperties)
            elif vertex_newName:
                graph.updateVertex(name=vertex_name, new_name=vertex_newName)
            elif vertex_newProperties: 
                graph.updateVertex(name=vertex_name, new_properties= vertex_newProperties)
            else:
                graph.updateVertex(name=vertex_name)

        elif user_input == "4":
            #TRATAR ERROS NO INTERPRETADOR

            vertex_name = input("digite o nome do vertice a ser apagado")
            graph.deleteVertex(vertex_name)
        elif user_input == "5":
            #TRATAR ERROS NO INTERPRETADOR

            from_vertex = input("de qual vertice vem a conexao\n")
            to_vertex = input("qual vertice recebe a conexao\n")
            new_relation_name = input("qual sera o novo nome da relacao\n")
            graph.updateRelation(from_vertex=from_vertex, to_vertex=to_vertex, new_name = new_relation_name)
        elif user_input == "6":
            #TRATAR ERROS NO INTERPRETADOR

            from_vertex = input("de qual vertice vem a conexao\n")
            to_vertex = input("qual vertice recebe a conexao\n")
            graph.disconnect(from_vertex=from_vertex, to_vertex=to_vertex)
        elif user_input == "7":
            #TRATAR ERROS NO INTERPRETADOR

            graph.showGraph()
        elif user_input == "8":
            #TRATAR ERROS NO INTERPRETADOR

            vertex_name = input("digite o nome do vertice\n")
            graph.getVertex(vertex_name)
        elif user_input == "9":
            #TRATAR ERROS NO INTERPRETADOR

            vertex_name = input("digite o nome do vertice\n")
            graph.getVertex(vertex_name)
if __name__ == "__main__":
    menu()