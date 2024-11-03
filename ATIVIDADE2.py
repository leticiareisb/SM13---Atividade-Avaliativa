def calcular_soma_produto():
    try:
        h1 = int(input("Informe a idade do primeiro homem: "))
        h2 = int(input("Informe a idade do segundo homem: "))
        m1 = int(input("Informe a idade da primeira mulher: "))
        m2 = int(input("Informe a idade da segunda mulher: "))

        if any(age <= 0 for age in [h1, h2, m1, m2]):
            return "Erro: Todas as idades devem ser números inteiros positivos."
        
        homem_mais_velho = max(h1, h2)
        homem_mais_novo = min(h1, h2)
        
        mulher_mais_velha = max(m1, m2)
        mulher_mais_nova = min(m1, m2)
        
        soma = homem_mais_velho + mulher_mais_nova
        produto = homem_mais_novo * mulher_mais_velha

        return f"Soma das idades: {soma}\nProduto das idades: {produto}"
    
    except ValueError:
        return "Erro: Por favor, insira idades numéricas inteiras."

print(calcular_soma_produto())
