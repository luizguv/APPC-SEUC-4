# Sistema de Escoamento de Unidades de Carga
O **SEUC-4** é um sistema de monitoramento de pressão desenvolvido para a Refinaria Delta-9. Após uma tempestade comprometer os servidores centrais, este software foi projetado para operar diretamente nos sensores, processando dados em tempo real sem a necessidade de armazenamento de histórico.

## Problema
O Duto Principal de Escoamento (DPE) da refinaria corre riscos críticos:
1. **Ruptura:** Se a pressão subir excessivamente.
2. **Cristalização:** Se a pressão cair demais e o fluído entupir o sistema.
3. **Fadiga de Material:** Dois picos de pressão consecutivos na Zona Vermelha destroem as juntas de expansão devido à vibração harmônica.

## Regras
O sistema realiza o processamento imediato de cada leitura baseando-se nas seguintes regras:
* **Ajuste Térmico Automático:** 
  * Leituras > 150 UPCs: Acréscimo de 8%.
  * Leituras ≤ 150 UPCs: Redução de 4%.
* **Classificação por Zonas:**
  * **Zona Verde (Estável):** Entre 120 e 180 UPCs.
  * **Zona Amarela (Oscilação):** Fora da Verde, mas abaixo de 250 UPCs.
  * **Zona Vermelha (Crítica):** Qualquer valor acima de 250 UPCs.
* **Protocolo de Travamento:** Interrupção imediata se duas leituras consecutivas atingirem a Zona Vermelha.

## Estrutura
**main.py**, **contas.py**, **impressoes.py**.

## Como Executar
O projeto foi desenvolvido em **Python 3** e é compatível com o IDLE oficial ou VSCode.
