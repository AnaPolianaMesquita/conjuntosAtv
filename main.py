import random

def conjunto_usuario():
    print("\n--- CONJUNTO DO USUÁRIO (A) ---")
    print("Digite números inteiros ou palavras.")
    print("Separe os elementos por espaço (exemplo: 5 10 bola asa)")
    
    while True:
        inicio = input("Digite de 4 a 8 elementos: ").strip().split()
        
        elementos = []
        for item in inicio:
            if item not in elementos:
                elementos.append(item)
        
        if len(elementos) < 4 or len(elementos) > 8:
            print(f"Inválido! Você tem {len(elementos)} elemento. Insira novamente de 4 a 8\n")
            continue
        conjunto = set()
        for item in elementos:
            try:
                conjunto.add(int(item))
            except:
                conjunto.add(item)
        
        return conjunto

def conjunto_aleatorio():
    
    tamanho = random.randint(4, 8)
    conjunto_b = set()
    
    numeros = list(range(1, 11))
    palavras = ["elefante", "cachorro", "predio", "cor", "arvore", "sol", "volei", "mar", "nuvem", "branco"]
    
    while len(conjunto_b) < tamanho:
        if random.choice([True, False]):
            conjunto_b.add(random.choice(numeros))
        else:
            conjunto_b.add(random.choice(palavras))
    
    return conjunto_b

def resultados(conjunto_a, conjunto_b):
   
    print("\n" + "="*50)
    print("RESULTADOS DAS OPERAÇÕES")
    print("="*50)
    
    print(f"\nConjunto A (usuário): {conjunto_a}")
    print(f"Conjunto B (aleatório): {conjunto_b}")
    
    print("\n--- OPERAÇÕES ---")
    print(f" União (A ∪ B): {conjunto_a | conjunto_b}")
    print(f" Interseção (A ∩ B): {conjunto_a & conjunto_b}")
    print(f" Diferença (A - B): {conjunto_a - conjunto_b}")
    print(f" Diferença (B - A): {conjunto_b - conjunto_a}")
    print(f" Diferença simétrica (A Δ B): {conjunto_a ^ conjunto_b}")
    
    print("\n--- CARDINALIDADES ---")
    print(f" |A| = {len(conjunto_a)}")
    print(f" |B| = {len(conjunto_b)}")
    print(f" |A ∪ B| = {len(conjunto_a | conjunto_b)}")

def main():
    print("="*50)
    print("INICIO")
    print("="*50)
    
    conjunto_a = conjunto_usuario()
    conjunto_b = conjunto_aleatorio()
    resultados(conjunto_a, conjunto_b)
    
    print("\n" + "="*50)
    print("FIM!")
    print("="*50)

if __name__ == "__main__":
    main()