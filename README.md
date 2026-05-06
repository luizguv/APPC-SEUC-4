# Sistema de Escoamento de Unidades de Carga
O **SEUC-4** é um sistema de monitoramento de pressão desenvolvido para a Refinaria Delta-9. Após uma tempestade comprometer os servidores centrais, este software foi projetado para operar diretamente nos sensores, processando dados em tempo real sem a necessidade de histórico.
O foco principal é modelar e calcular a variação de pressão, realizando ajustes automáticos e classificando os resultados para garantir a integridade do Duto Principal de Escoamento (DPE).

## Grupo 5
* **Enzo Dassi Carvalho** - RA: 26006046
* **João Pedro Silveira de Souza** - RA: 26009261
* **Luiz Gustavo Urias Vieira** - RA: 26005065

## Problema
O Duto Principal de Escoamento (DPE) corre riscos críticos que o sistema visa corrigir:
1.  **Ruptura:** Pressão excessiva.
2.  **Cristalização:** Queda excessiva de pressão, causando entupimento.
3.  **Fadiga de Material:** Dois picos consecutivos na Zona Vermelha destroem as juntas de expansão por vibração.

## Regras
O sistema realiza o processamento imediato baseando-se nas seguintes regras:
* **Leituras > 150 UPCs:** Acréscimo de 8%.
* **Leituras ≤ 150 UPCs:** Redução de 4%.
* **Zona Verde (Estável):** Entre 120 e 180 UPCs.
* **Zona Amarela (Oscilação):** Fora da Verde, mas abaixo de 250 UPCs.
* **Zona Vermelha (Crítica):** Qualquer valor acima de 250 UPCs.
* **Travamento:** Interrupção imediata se duas leituras consecutivas atingirem a Zona Vermelha.

## Desenvolvimento
O projeto foi desenvolvido puramente em **Python 3**, utilizando conceitos fundamentais da linguagem sem a dependência de bibliotecas externas:
* **Estruturas de Controle:** Uso de `if`, `else` e `elif` para a filtragem e classificação das pressões.
* **Estruturas de Repetição:** Uso de `for` e `while` para processar sequências de itens.
* **Modularização:** O código foi dividido em arquivos para melhor organização e manutenção.

### Estrutura
* `main.py`: Ponto de entrada do sistema.
* `contas.py`: Lógica matemática e processamento de dados.
* `impressoes.py`: Funções responsáveis pela saída de dados e interface com o usuário.
* O projeto é compatível com o IDLE oficial do Python ou **VSCode**.

## Referências
* Documentação do Python: [docs.python.org](https://docs.python.org/3/)
