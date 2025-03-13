grafo = {
    'A': ['B', 'C'],  
    'B': ['A', 'D'], 
    'C': ['A', 'E'],  
    'D': ['B', 'F'], 
    'E': ['C', 'F'],  
    'F': ['D', 'E']   
}

for cidade, vizinhos in grafo.items():
    print(f'{cidade} tem vizinhos: {vizinhos}')