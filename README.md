#  Mission Control AI — Space FIAPo

Sistema inteligente de monitoramento e telemetria espacial desenvolvido em Python para a **Global Solution (GS2026.1)**. O projeto simula o ecossistema de uma sala de controle de solo, processando variáveis críticas de uma missão aeroespacial experimental através de regras lógicas estruturadas para mitigar falhas e apoiar a tomada de decisões.

---

##  Equipe: FIAPo Da Manga
- **Projeto:** Mission Control AI
- **Missão Experimental:** Space FIAPo
- Pedro Andreassa Zamai RM: 569318
- Pedro Yoshikado Garcia RM: 570449
- Thiago Maluf Hofmann RM: 569852

---

##  Objetivos do Sistema

- **Processamento de Matrizes:** Armazenar e iterar sobre dados históricos de telemetria (6 ciclos completos).
- **Modularização Avançada:** Arquitetura limpa dividida em 10 funções especialistas e independentes.
- **Análise Multivariável:** Avaliação individual de 5 sistemas vitais por ciclo.
- **Cálculo de Risco Ponderado:** Atribuição de score de risco acumulado.
- **Diagnóstico de Tendência:** Identificação preditiva do comportamento da missão (Melhora, Piora ou Estabilidade).
- **Foco de Danos:** Isolamento matemático da área de engenharia mais afetada por anomalias.

---

##  Arquitetura de Dados e Regras de Negócio

Os dados são injetados através de uma matriz estruturada, onde cada linha representa um ciclo de leitura composto por:
`[Temperatura, Comunicação, Bateria, Oxigênio, Estabilidade]`

###  Matriz de Limiares Lógicos e Scores

O motor de análise avalia cada indicador de acordo com as seguintes regras de integridade:

| Sistema | Intervalo / Condição | Classificação | Pontos de Risco | Mensagem de Alerta |
| :--- | :--- | :--- | :---: | :--- |
| **Temperatura Interna** | `< 18 °C` | ATENÇÃO | 1 | Temperatura baixa |
| | `18 °C` a `30 °C` | NORMAL | 0 | Temperatura estável |
| | `31 °C` a `35 °C` | ATENÇÃO | 1 | Temperatura elevada |
| | `> 35 °C` | CRÍTICO | 2 | Risco de superaquecimento |
| **Comunicação Base** | `< 30%` | CRÍTICO | 2 | Comunicação com a base em nível crítico |
| | `30%` a `59%` | ATENÇÃO | 1 | Comunicação instável |
| | `>= 60%` | NORMAL | 0 | Comunicação estável |
| **Sistema de Energia** | `< 20%` | CRÍTICO | 2 | Bateria em nível crítico |
| (Bateria) | `20%` a `49%` | ATENÇÃO | 1 | Bateria abaixo do recomendado |
| | `>= 50%` | NORMAL | 0 | Energia estável |
| **Suporte de Oxigênio** | `< 80%` | CRÍTICO | 2 | Oxigênio em nível crítico |
| | `80%` a `89%` | ATENÇÃO | 1 | Oxigênio abaixo do ideal |
| | `>= 90%` | NORMAL | 0 | Oxigênio adequado |
| **Estabilidade** | `< 40%` | CRÍTICO | 2 | Estabilidade operacional crítica |
| **Operacional** | `40%` a `69%` | ATENÇÃO | 1 | Estabilidade operacional reduzida |
| | `>= 70%` | NORMAL | 0 | Estabilidade operacional adequada |

---

##  Lógica de Tomada de Decisão (Ciclos)

A somatória dos pontos de risco gerados pelos 5 sistemas dita a classificação e a ação automática de contingência:

* **0 a 2 pontos:** `MISSÃO ESTÁVEL`  
  * *Recomendação:* Manter operação normal e continuar monitoramento.
* **3 a 5 pontos:** `MISSÃO EM ATENÇÃO`  
  * *Recomendação:* Monitorar sistemas em atenção e preparar plano de contingência.
* **6 a 10 pontos:** `MISSÃO CRÍTICA`  
  * *Recomendação:* Ativar modo de segurança e priorizar suporte à vida, energia e comunicação.

---

##  Estrutura de Arquivos

```text
mission-control-ai/
│
├── mission_control.py   # Script principal com motor lógico em Python 3
└── README.md            # Documentação técnica do projeto
```

---

## Como Executar
1. Certifique-se de que possui o Python 3.x instalado.
2. Clone o repositório para a sua máquina local:
```bash
    git clone https://github.com/ThiagoMaluf/Mission-Control-AI
```
3. Acesse a pasta do projeto:
```bash
    cd Mission-Control-AI
```
4. Execute o script via terminal:
```bash
    python mission_control.py
```

