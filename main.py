
def seuc():
    total_leituras = int(input("Digite o número total de leituras que irá ocorrer durante o turno: "))
    cont = 0
    media = 0
    cont_verde = 0
    leituras_feitas = 0
    soma = 0
    menor = 999999999999999

    for i in range(total_leituras):
        pressao = float(input("Informe a pressão (UPC): "))
        if pressao > 150:
            pressao *= 1.08
        else:
            pressao *= 0.94

        if pressao < menor:
            menor = pressao

        soma += pressao
        leituras_feitas += 1

        if 120 <= pressao <= 180:
            print(f"A pressão está em {pressao:.2f}, portanto está na zona Verde(ESTÁVEL)!")
            cont = 0
            cont_verde += 1
        elif pressao < 250:
            print(f"A pressão está em {pressao:.2f}, portanto está na zona Amarela(OSCILAÇÃO)!")
            cont = 0
        else:
            print(f"A pressão está em {pressao:.2f}, portanto está na zona Vermelha(CRÍTICA)!")
            cont += 1
        if cont == 2:
            #i = (total_leituras + 1)
            #print("PROTOCOLO DE TRAVAMENTO FOI INICIADO!\nINTERROMPENDO ESCOAMENTO POR SEGURANÇA...")
            break
    media = soma / leituras_feitas
    porc = (cont_verde / leituras_feitas) * 100

    print(f"A porcentagem de leituras feitas na zona verde é {porc:.2f}%.")
    print(f"A média das pressões já ajustadas é de: {media:.2f} UPC.")
    print(f"Menor pressão registrada após o ajuste é: {menor:.2f} UPC.")

seuc()
