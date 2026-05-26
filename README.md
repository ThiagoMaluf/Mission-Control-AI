# Mission-Control-AI


Sistema de simulação de controle de missão espacial desenvolvido em Python.  
O projeto analisa ciclos de monitoramento e gera relatórios automáticos sobre o estado de uma missão espacial experimental.


# Objetivo

- Armazenar dados simulados de uma missão espacial
- Analisar ciclos de monitoramento
- Gerar alertas automáticos
- Calcular nível de risco por ciclo
- Classificar o estado da missão
- Identificar tendência (melhora ou piora)
- Detectar área mais afetada
- Exibir relatório final no terminal

# Como funciona

A missão é representada por uma matriz chamada `dados_missao`.
Cada linha representa um ciclo de monitoramento:


[temperatura, comunicacao, bateria, oxigenio, estabilidade]

Exemplo:

[25, 91, 86, 92, 88]

# Estrutura dos dados

Cada coluna representa um sistema da missão:

- Temperatura interna (°C)
- Comunicação com a base (%)
- Sistema de energia (%)
- Suporte de oxigênio (%)
- Estabilidade operacional (%)

# Regras de classificação

Cada variável é classificada e recebe pontos de risco:

- NORMAL = 0 ponto
- ATENÇÃO = 1 ponto
- CRÍTICO = 2 pontos

# Classificação do ciclo

A soma dos pontos define o estado do ciclo:

- 0 a 2 pontos → MISSÃO ESTÁVEL
- 3 a 5 pontos → MISSÃO EM ATENÇÃO
- 6 a 10 pontos → MISSÃO CRÍTICA

# Análise de tendência

O sistema compara o primeiro e o último ciclo:

- Último > Primeiro → Missão piorou
- Último < Primeiro → Missão melhorou
- Igual → Missão estável

# Área mais afetada

O sistema soma os pontos de cada área ao longo de todos os ciclos e identifica qual sistema apresentou maior risco acumulado

# Relatório final

O sistema apresenta um relatório detalhado mostrando:
    Ciclos analisados;
    média de temperatura, comunicação, bateria, oxigênio e estabilidade;
    Ciclo mais crítico;
    Pontuação de risco;
    Quantidade de ciclos críticos;
    Situação da missão;
    Área mais afetada;
    Situação final da missão;
    Conclusão.