# Simulador de rendimento do investimento com desconto de IOF e IR
# Alunas:
# Maria Eduarda Guimarães Costa 24114290121
# Maria Eduarda Fernandes Calado 24112490094


# Receber o valor inicial do investimento, validando a entrada.
while True:
    entrada = input("Digite o valor inicial do seu investimento: ")
    if not entrada:
        print("Por favor, informe um valor.")
    else:
        try:
            valor_inicial = float(entrada)
            if valor_inicial <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                break 
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Receber o tempo de investimento (em dias), validando a entrada.
while True:
    entrada = input("Digite o tempo de investimento (em dias): ").strip()
    if not entrada:
        print("Por favor, informe o tempo de investimento.")
    else:
        try:
            tempo_investimento = int(entrada)
            if tempo_investimento <= 0:
                print("O tempo deve ser maior que zero. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

# Calcular o rendimento baseado em 14,15% ao ano.
def calcular_rendimento_bruto(valor_inicial, tempo_investimento):
    rendimento_diario = (14.15 / 100) / 365
    valor_bruto = valor_inicial * (1 + rendimento_diario) ** tempo_investimento
    return valor_bruto


# Cálculo do IOF
def calcular_iof(valor_bruto, tempo_investimento) :
    # tabela do iof regresssivo (em porcentagem)
    tabela_iof = {
    1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66, 11: 63, 
    12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36, 20: 33, 21: 30,
    22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
}
    if tempo_investimento > 30:
        return 0.0
    
    percentual_iof = tabela_iof.get(tempo_investimento, 0) / 100
    valor_iof = valor_bruto * percentual_iof
    rendimento_liquido = valor_bruto - valor_iof
    return valor_iof

# Calcular desconto
def tabela_ir( rendimento_liquido, tempo_investimento):
    if tempo_investimento <= 180:
        aliquota_ir = 22.5
    elif tempo_investimento <= 360:
        aliquota_ir = 20.0
    elif tempo_investimento <= 720:
        aliquota_ir = 17.5
    else:
        aliquota_ir = 15.0
            
    valor_ir = rendimento_liquido * (aliquota_ir / 100)
    rendimento_final = rendimento_liquido - valor_ir
    valor_final = valor_inicial + rendimento_final
    return valor_final, valor_ir, rendimento_final

# Cálculo do valor final bruto
valor_bruto = calcular_rendimento_bruto(valor_inicial, tempo_investimento)
rendimento_bruto = valor_bruto - valor_inicial

# Aplicação de IOF
valor_iof = calcular_iof(rendimento_bruto, tempo_investimento)

# Aplicação de IR sobre o rendimento líquido de IOF
rendimento_liquido = rendimento_bruto - valor_iof
# Valor final com os descontos
valor_final, valor_ir, rendimento_final = tabela_ir(rendimento_liquido, tempo_investimento)

# Impressão dos resultados
print("Resultado da simulação:")
print(f"Valor inicial investido: R$ {valor_inicial:,.2f}")
print(f"Tempo de aplicação: {tempo_investimento} dias")
print(f"Rendimento bruto: R$ {(valor_bruto - valor_inicial):,.2f}")
print(f"IOF descontado: R$ {valor_iof:,.2f}")
print(f"IR descontado: R$ {(rendimento_liquido - (valor_final - valor_inicial)):,.2f}")
print(f"Valor final líquido: R$ {valor_final:,.2f}")
