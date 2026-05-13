def ajustar_pressao(pressao): # Aplica o ajuste da pressão
    if pressao >= 150:
        return pressao * 1.08
    return pressao * 0.94


def classificar_pressao(pressao): # Retorna a zona de classificação: verde, amarela ou vermelha.
    if 120 <= pressao <= 180:
        return "verde"
    elif pressao < 250:
        return "amarela"
    return "vermelha"


def exibir_status(i, pressao, zona, total_leituras, cont_crit): # Exibe a classificação da pressão lida.
    print(f"=== Leitura {i + 1}/{total_leituras} ===")
    if zona == "verde":
        print(f"Pressão {pressao:.2f} UPC: Zona Verde (ESTÁVEL)!")
    elif zona == "amarela":
        print(f"Pressão {pressao:.2f} UPC: Zona Amarela (OSCILAÇÃO)!")
    else:
        print(f"Pressão {pressao:.2f} UPC: Zona Vermelha (CRÍTICA)!")
        if cont_crit == 1:
            print("ATENÇÃO: Mais uma leitura crítica consecutiva acionará o protocolo de travamento de emergência!")


def exibir_relatorio(media, porc_verde, menor, maior, leituras_feitas, total_leituras, travamento, cont_verde, cont_amarelo, cont_vermelho, ultima_pressao): # Exibe as métricas finais.
    print(f"\nPorcentagem de leituras feitas na zona verde : {porc_verde:.2f}%")
    print(f"Média das pressões após o ajuste: {media:.2f} UPC")
    print(f"Menor pressão registrada: {menor:.2f} UPC")
    print(f"Maior pressão registrada: {maior:.2f} UPC")
    print(f"Última pressão registrada antes de finalizar: {ultima_pressao:.2f} UPC")
    print(f"Leituras na zona verde: {cont_verde} | Amarela: {cont_amarelo} | Vermelha: {cont_vermelho}")
    if travamento == True:
        porc_realizadas = (leituras_feitas / total_leituras) * 100
        print(f"Ocorreram {leituras_feitas} de {total_leituras} leituras. O percentual é de: {porc_realizadas:.2f}%.")

def ler_pressao(): # Lê a pressão e rejeita valores negativos
    pressao = float(input("Informe a pressão (UPC): "))
    while pressao < 0:
        print("Valor inválido! A pressão não pode ser negativa!")
        pressao = float(input("Informe a pressão (UPC): "))
    return pressao

def ler_total_leituras(): # Lê o total de leituras e rejeita valores menores ou iguais a zero
    total = int(input("Digite o número total de leituras do turno: "))
    while total <= 0:
        print("Valor inválido! O número de leituras deve ser maior que zero!")
        total = int(input("Digite o número total de leituras do turno: "))
    return total        

def seuc(): # Função principal.
    total_leituras = ler_total_leituras()
    cont_crit = 0
    cont_verde = 0
    cont_amarelo = 0
    cont_vermelho = 0
    leituras_feitas = 0
    soma = 0
    menor = 99999999999
    maior = 0
    travamento = False
    ultima_pressao = 0

    for i in range(total_leituras):
        pressao = ler_pressao()
        pressao = ajustar_pressao(pressao)
        zona = classificar_pressao(pressao)

        exibir_status(i, pressao, zona, total_leituras, cont_crit)

        if zona == "verde":
            cont_verde += 1
            cont_crit = 0
        elif zona == "amarela":
            cont_crit = 0
            cont_amarelo += 1
        else:
            cont_crit += 1
            cont_vermelho += 1

        soma += pressao
        leituras_feitas += 1
        ultima_pressao = pressao

        if pressao < menor:
            menor = pressao
        
        if pressao > maior:
            maior = pressao

        if cont_crit == 2:
            print("PROTOCOLO DE TRAVAMENTO INICIADO!\nINTERROMPENDO ESCOAMENTO POR SEGURANÇA...")
            travamento = True
            break

    exibir_relatorio(soma / leituras_feitas, (cont_verde / leituras_feitas) * 100, menor, maior, leituras_feitas, total_leituras, travamento, cont_verde, cont_amarelo, cont_vermelho, ultima_pressao)


seuc()
