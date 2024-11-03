def calcular_salario():
    try:
        salario_fixo = float(input("Informe o salário fixo do vendedor: "))
        comissao_por_carro = float(input("Informe a comissão fixa por carro vendido: "))
        total_vendas = float(input("Informe o valor total das vendas: "))
        carros_vendidos = int(input("Informe a quantidade de carros vendidos: "))

        if salario_fixo < 0 or comissao_por_carro < 0 or total_vendas < 0 or carros_vendidos < 0:
            return "Erro: Todos os valores devem ser números positivos."
        
        salario_final = salario_fixo
        if carros_vendidos > 0:
            salario_final += comissao_por_carro * carros_vendidos
            salario_final += 0.05 * total_vendas 
            if carros_vendidos > 10:
                salario_final += 0.10 * total_vendas  
        
        return f"O salário final do vendedor é: R$ {salario_final:.2f}"
    
    except ValueError:
        return "Erro: Por favor, insira valores numéricos válidos."

print(calcular_salario())
