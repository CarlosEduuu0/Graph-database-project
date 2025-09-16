from graph import Graph
import os

def menu():
    graph = Graph(name="meu grafo")
    while(True):
        os.system("cls")
        print("================ Menu de Testes ================")
        print("1. Adicionar Vértice")
        print("2. Conectar Vértices")
        print("3. Atualizar Vértices")
        print("4. Deletar Vértice")
        print("5. Atualizar Conexão")
        print("6. Descartar Vértices")
        print("7. Printar Grafo")
        print("8. Procurar Vértice")
        print("9. Exibir Vizinhos")
        print("10. Exportar JSON")
        print("11. Sair")
        print("================================================")
        user_input = input("Digite uma opção: ")

        if user_input == "11":
            break
        elif user_input == "1":
            # TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("============== Adicionar Vértice ===============")
            vertex_name = input("Digite o nome do vertice\n")
            properties_size = int(input("Quantas propriedades terá o seu vertice?\n"))
            vertex_properties = {}
            for i in range(properties_size):
                key = input("Digite o nome da propriedade\n")
                value = input("Digite o valor da propriedade\n")
                vertex_properties[key] = value
            graph.addVertex(name= vertex_name, properties=vertex_properties)

        elif user_input == "2":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("============== Conectar Vértices ===============")
            from_vertex = input("De qual vertice vira a conexao\n")
            to_vertex = input("Qual vertice recebera a conexao\n")
            relation_name = input("Qual sera o nome da relacao\n")
            graph.connectVertices(relation_name=relation_name, from_vertex=from_vertex, to_vertex=to_vertex)
        elif user_input == "3":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("============== Atualizar Vértices ==============")
            vertex_newName = None
            vertex_newProperties = None
            vertex_name = input("Digite o nome do vertice a ser atualizado\n")
            choice = input("Digite 1 para atualizar o nome do vertice")
            if choice == "1":
                choice = 0
                vertex_newName = input("Digite o novo nome do vertice\n")

            choice = input("Digite 1 para atualizar as propriedades do vertiec")
            if choice == "1":
                properties_size = int(input("Quantas propriedades terá o seu vertice?\n"))
                vertex_newProperties = {}
                for i in range(properties_size):
                    key = input("Digite o nome da propriedade\n")
                    value = input("Digite o valor da propriedade\n")
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
            os.system("cls")
            print("=============== Deletar Vértices ===============")
            vertex_name = input("Digite o nome do vertice a ser apagado")
            graph.deleteVertex(vertex_name)
        elif user_input == "5":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("============== Atualizar Conexão ===============")
            from_vertex = input("De qual vertice vem a conexao\n")
            to_vertex = input("Qual vertice recebe a conexao\n")
            new_relation_name = input("Qual sera o novo nome da relacao\n")
            graph.updateRelation(from_vertex=from_vertex, to_vertex=to_vertex, new_name = new_relation_name)
        elif user_input == "6":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("============== Descartar Vértices ==============")
            from_vertex = input("De qual vertice vem a conexao\n")
            to_vertex = input("Qual vertice recebe a conexao\n")
            graph.disconnect(from_vertex=from_vertex, to_vertex=to_vertex)
        elif user_input == "7":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("================ Printar Grafo =================")
            graph.showGraph()
            print("================================================")
            input("Pressione qualquer tecla para continuar. . .")
        elif user_input == "8":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("=============== Procurar Vértices ==============")
            vertex_name = input("Digite o nome do vertice\n")
            graph.getVertex(vertex_name)
        elif user_input == "9":
            #TRATAR ERROS NO INTERPRETADOR
            os.system("cls")
            print("=============== Exibir Vizinhos ================")
            print("=============== Exibir Vizinhos ================")
            vertex_name = input("Digite o nome do vertice\n")
            graph.getVertex(vertex_name)

        elif user_input == "10":
            graph.exportToJson('grafo.json')
            print("Grafo exportado!")
            
if __name__ == "__main__":
    menu()