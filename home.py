from graph import Graph
from cypherInterpreter import CypherInterpreter

def loop(interpreter: CypherInterpreter):
    while(True):
        command = input()

        if command == "logout":
            break
        
        interpreter.execute(command)

if __name__ == "__main__":
    graph = Graph("neo4j")
    interpreter = CypherInterpreter(graph)
    loop(interpreter)
