from graph import Graph
from cypherInterpreter import CypherInterpreter
from menu import menu
import os

def loop(interpreter: CypherInterpreter):
    while(True):
        os.system("cls")
        print("==================== Cypher Interpreter ====================\n")
        print("=========================== GUIA ===========================")
        print('Exemplo CREATE (a:Person {name:"João", age:"30"})')
        print('CREATE (b:City {name:"Belém"})')
        print('CREATE (a)-[:LIVES_IN]->(b)')
        print('MATCH (a:Person)-[:LIVES_IN]->(b:City) RETURN b')
        print('Escreva "logout" para sair')
        print("============================================================")
        print("Insira um Comando CYPHER: ", end="")
        command = input()

        if command == "logout":
            break
        interpreter.execute(command)

if __name__ == "__main__":
    graph = Graph("neo4j")
    interpreter = CypherInterpreter(graph)

    while(True):
        os.system("cls")
        print("================== Graph-Database-Project 😎 ==================")
        print("1. Cypher Interpreter")
        print("2. Menu de Testes")
        print("3. Sair")
        print("================================================================")
        input_user = input("Escolha uma opção: ")

        if input_user == "1":
            os.system("cls")
            loop(interpreter)
        
        elif input_user == "2":
            os.system("cls")
            menu()

        elif input_user == "3":
            os.system("cls")
            break
            
        else:
            os.system("cls")
            print("Opção Inválida!")