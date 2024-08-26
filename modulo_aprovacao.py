
lista = [{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
		{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
		{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]
		

         
def aprovacao(lista):
    for dicionario in lista:
        print(f"nome: {dicionario['nome']}, notas: {dicionario['notas']}")
        
print(aprovacao(lista))