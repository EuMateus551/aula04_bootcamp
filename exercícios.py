#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista_de_numeros = []

for n in range(0, 11):
    lista_de_numeros.append(n)

    print(n**2)

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista_de_linguagens = ["Python", "Java", "C++", "JavaScript"]
trocar_linguagem = lista_de_linguagens.index("C++")
lista_de_linguagens[trocar_linguagem] = "Ruby"

print(lista_de_linguagens)

#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: dict = {
    "Título": "Jogador número 1",
    "Autor": "Ernest Cline",
    "Ano de publicação": "2011"
}

print(livro["Título"])
print(livro["Autor"])
print(livro["Ano de publicação"])

#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
string: str="Banana"
contador: list={}

for caractere in string:
    if caractere in contador:
        contador[caractere]+=1
    else:
        contador[caractere]=1
    
    
print(contador)

#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.