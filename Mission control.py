nome_missao = "Space FIAPo"
equipe = "FIAPo Da Manga"

dados_missao = [
    [25, 91, 86, 92, 88],
    [28, 66, 69, 92, 86],
    [31, 67, 59, 89, 68],
    [27, 49, 55, 83, 52],
    [19, 28, 19, 78, 35],
    [22, 66, 44, 79, 53]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]
def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura baixa"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor <= 69:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(risco):
    if risco <= 2:
        return "Manter operação normal e continuar monitoramento."
    elif risco <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."


def analisar_tendencia(riscos_missao):
    if riscos_missao[-1] > riscos_missao[0]:
        return "A missão apresentou tendência de piora."
    elif riscos_missao[-1] < riscos_missao[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_areas, lista_areas):
    maior_idx = pontuacao_areas.index(max(pontuacao_areas))
    return lista_areas[maior_idx]


def calcular_media(valores):
    return sum(valores) / len(valores)

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

riscos = []
pontuacao_areas = [0, 0, 0, 0, 0]

for i, ciclo in enumerate(dados_missao):
    print(f"\nCICLO {i + 1}")
    print("-" * 60)

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    s1, p1, m1 = analisar_temperatura(temperatura)
    s2, p2, m2 = analisar_comunicacao(comunicacao)
    s3, p3, m3 = analisar_bateria(bateria)
    s4, p4, m4 = analisar_oxigenio(oxigenio)
    s5, p5, m5 = analisar_estabilidade(estabilidade)

    risco = p1 + p2 + p3 + p4 + p5
    riscos.append(risco)

    pontuacao_areas[0] += p1
    pontuacao_areas[1] += p2
    pontuacao_areas[2] += p3
    pontuacao_areas[3] += p4
    pontuacao_areas[4] += p5

    print(f"Temperatura: {temperatura} °C | {s1} | {m1}")
    print(f"Comunicação: {comunicacao}% | {s2} | {m2}")
    print(f"Bateria: {bateria}% | {s3} | {m3}")
    print(f"Oxigênio: {oxigenio}% | {s4} | {m4}")
    print(f"Estabilidade: {estabilidade}% | {s5} | {m5}")

    print(f"\nPontuação de risco do ciclo: {risco}")
    print(f"Classificação do ciclo: {classificar_ciclo(risco)}")
    print(f"Recomendação: {gerar_recomendacao(risco)}")

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")
print(f"\nQuantidade de ciclos analisados: {len(dados_missao)}")

media_temp  = calcular_media([c[0] for c in dados_missao])
media_com   = calcular_media([c[1] for c in dados_missao])
media_bat   = calcular_media([c[2] for c in dados_missao])
media_oxi   = calcular_media([c[3] for c in dados_missao])
media_est   = calcular_media([c[4] for c in dados_missao])

print(f"\nMédia de temperatura:  {media_temp:.2f} °C")
print(f"Média de comunicação:  {media_com:.2f}%")
print(f"Média de bateria:      {media_bat:.2f}%")
print(f"Média de oxigênio:     {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")

ciclo_mais_critico = riscos.index(max(riscos)) + 1
media_risco = calcular_media(riscos)
ciclos_criticos = len([r for r in riscos if r >= 6])

print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {max(riscos)}")
print(f"Risco médio da missão: {media_risco:.2f}")
print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

print("\nTendência da missão:")
print(analisar_tendencia(riscos))

print("\nPontuação acumulada por área:")
for i in range(5):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

area_mais_afetada = identificar_area_mais_afetada(pontuacao_areas, areas_monitoradas)
print(f"\nÁrea mais afetada:")
print(area_mais_afetada)

print(f"\nClassificação final da missão:")
print(classificar_ciclo(media_risco))

print("\nConclusão:")
if media_risco <= 2:
    print("A missão permaneceu estável durante a maior parte da operação.")
elif media_risco <= 5:
    print("A missão apresentou instabilidade moderada e exige monitoramento.")
else:
    print("A missão apresentou instabilidade relevante durante a operação.")

print("=" * 60)