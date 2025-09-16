import re
import os
from graph import Graph
from colorama import Fore, Style, init
import time

class CypherInterpreter:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.alias = {} 

    def execute(self, command: str):
        command = command.strip()

        match = re.match(r'CREATE\s*\((\w+):(\w+)\s*\{(.+?)\}\)', command, re.IGNORECASE)
        if match:
            alias, label, props = match.groups()
            props_dict = self._parse_props(props)
            node_id = props_dict.get("name", alias)
            self.graph.addVertex(node_id, props_dict)
            self.alias[alias] = node_id
            print(f"Nó {node_id} ({label}) criado com props {props_dict}")
            time.sleep(2)
            return 

        match = re.match(r'CREATE\s*\((\w+)\)-\[:(\w+)\]->\((\w+)\)', command, re.IGNORECASE)
        if match:
            origin_alias, relation, destination_alias = match.groups()
            from_vertex = self.alias.get(origin_alias)
            to_vertex = self.alias.get(destination_alias)
            self.graph.connectVertices(relation, from_vertex, to_vertex)
            self.graph.vertices[from_vertex].printAll()
            print(f"Aresta {relation} criada: {from_vertex} -> {to_vertex}")
            time.sleep(2)
            return 

        match = re.match(r'MATCH\s*\((\w+):?(\w+)?\)-\[:(\w+)\]->\((\w+):?(\w+)?\)\s*RETURN\s+(\w+)', command, re.IGNORECASE)
        if match:
            a, label_a, relation, b, label_b, ret = match.groups()
            from_vertex = self.alias.get(a, a)
            self.graph.vertices[from_vertex].printAll()
            result = self.graph.getNeighborsByRelation(from_vertex, relation)
            print(result)
            time.sleep(2)
            return 
        
        save = re.match(r'SAVE\s*\(([^)]+)\)', command, re.IGNORECASE)
        if save:
            filename = save.group(1).strip()
            if not filename.endswith('.json'):
                filename += '.json'
            self.graph.exportToJson(filename)
            return

        init()
        print(Fore.RED + f'\nERRO!!! Comando "{command}" não reconhecido' + Style.RESET_ALL)
        
        entrada = input(f"\nAperte Enter para continuar. . .")
        if entrada == "":
            os.system("cls")

    def _parse_props(self, props_str):
        """Transforma 'name:\"Gabriel\", age:\"22\"' em dict Python"""
        props = {}
        for item in props_str.split(","):
            k, v = item.split(":")
            props[k.strip()] = v.strip().strip('"')
        return props
