def calcular_valor_final_investimento(valor_inicial, taxa_juros, periodo):
    # Calcula o valor final com juros compostos
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    
    # Arredonda o valor final para duas casas decimais
    valor_final_arredondado = round(valor_final, 2)
    
    return valor_final_arredondado
    
valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

resultado = calcular_valor_final_investimento(valor_inicial, taxa_juros, periodo)
print(f"Valor final do investimento: R$ {resultado}")