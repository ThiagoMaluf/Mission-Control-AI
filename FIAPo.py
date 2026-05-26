# ============================================================
# MISSION CONTROL AI
# ============================================================

nome_missao = "Space FIAPo"
equipe = "Fiapo Da Manga"

dados_missao = [
    [25, 91, 86, 92, 88],
    [28, 66, 69, 92, 86],
    [31, 67, 59, 89, 68],
    [27, 49, 55, 83, 52],
    [19, 28, 19, 78, 35],
    [22, 66, 44, 79, 53]
]

areas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Oxigênio",
    "Estabilidade operacional"
]

# ============================
# FUNÇÕES DE ANÁLISE
# ============================

def analisar(valor, tipo):
    if tipo == "temp":
        if valor < 18:
            return "CRÍTICO", 2, "Temperatura extremamente baixa"
        elif valor <= 30:
            return "NORMAL", 0, "Temperatura estável"
        elif valor <= 35:
            return "ATENÇÃO", 1, "Temperatura elevada"
        else:
            return "CRÍTICO", 2, "Grande risco"

    if tipo == "com":
        if valor < 30:
            return "CRÍTICO", 2, "Comunicação impossivel"
        elif valor <= 59:
            return "ATENÇÃO", 1, "Comunicação instável"
        else:
            return "NORMAL", 0, "Comunicação estável"

    if tipo == "bat":
        if valor < 20:
            return "CRÍTICO", 2, "Bateria em nivel crítico"
        elif valor <= 49:
            return "ATENÇÃO", 1, "Bateria fraca"
        else:
            return "NORMAL", 0, "Energia estável"

    if tipo == "oxi":
        if valor < 80:
            return "CRÍTICO", 2, "Oxigênio crítico"
        elif valor <= 89:
            return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
        else:
            return "NORMAL", 0, "Oxigênio adequado"

    if tipo == "est":
        if valor < 40:
            return "CRÍTICO", 2, "Baixa estabilidade"
        elif valor <= 69:
            return "ATENÇÃO", 1, "Estabilidade reduzida"
        else:
            return "NORMAL", 0, "Estabilidade adequada"


def classificar(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def recomendacao(risco):
    if risco <= 2:
        return "Manter missão e continuar monitoramento."
    elif risco <= 5:
        return "Monitorar sistemas e preparar contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida."


# ============================
# PROGRAMA
# ============================

print("=" * 60)
print("Space FIAPo")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

riscos = []
pontuacao_areas = [0, 0, 0, 0, 0]

# ============================
# CICLOS
# ============================

for i, c in enumerate(dados_missao):

    print(f"\nCICLO {i+1}")
    print("-" * 60)

    t, com, bat, oxi, est = c

    s1, p1, m1 = analisar(t, "temp")
    s2, p2, m2 = analisar(com, "com")
    s3, p3, m3 = analisar(bat, "bat")
    s4, p4, m4 = analisar(oxi, "oxi")
    s5, p5, m5 = analisar(est, "est")

    risco = p1 + p2 + p3 + p4 + p5
    riscos.append(risco)

    pontuacao_areas[0] += p1
    pontuacao_areas[1] += p2
    pontuacao_areas[2] += p3
    pontuacao_areas[3] += p4
    pontuacao_areas[4] += p5

    print(f"Temperatura: {t} °C | {s1} | {m1}")
    print(f"Comunicação: {com}% | {s2} | {m2}")
    print(f"Bateria: {bat}% | {s3} | {m3}")
    print(f"Oxigênio: {oxi}% | {s4} | {m4}")
    print(f"Estabilidade: {est}% | {s5} | {m5}")

    print(f"\nPontuação de risco do ciclo: {risco}")
    print(f"Classificação do ciclo: {classificar(risco)}")
    print(f"Recomendação: {recomendacao(risco)}")


# ============================
# RELATÓRIO
# ============================

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")
print("-" * 35)
print(f"\nQuantidade de ciclos analisados: {len(dados_missao)}")

media = lambda x: sum(x)/len(x)

print("-" * 35)
print(f"Média de temperatura: {media([c[0] for c in dados_missao]):.2f} °C")
print(f"Média de comunicação: {media([c[1] for c in dados_missao]):.2f}%")
print(f"Média de bateria: {media([c[2] for c in dados_missao]):.2f}%")
print(f"Média de oxigênio: {media([c[3] for c in dados_missao]):.2f}%")
print(f"Média de estabilidade: {media([c[4] for c in dados_missao]):.2f}%")
print("-" * 35)


print(f"\nCiclo mais crítico: {riscos.index(max(riscos)) + 1}")
print("-" * 35)
print(f"Maior pontuação de risco: {max(riscos)}")
print(f"Risco médio da missão: {sum(riscos)/len(riscos):.2f}")
print(f"Quantidade de ciclos críticos: {len([r for r in riscos if r >= 6])}")

# situação
print("\nSituação da missão:")

print("-" * 35)
if riscos[-1] > riscos[0]:
    print("A missão apresentou piora.")
elif riscos[-1] < riscos[0]:
    print("A missão apresentou melhora.")
else:
    print("A missão permaneceu estável.")
print("-" * 35)


# áreas
print("\nPontuação acumulada por área:")
for i in range(5):
    print(f"{areas[i]}: {pontuacao_areas[i]} pontos")

print("\nÁrea mais afetada:")

print("-" * 20)
print(areas[pontuacao_areas.index(max(pontuacao_areas))])
print("-" * 20)

# classificação final
media_risco = sum(riscos)/len(riscos)

print("\nSituação final da missão:")

print("-" * 60)
print(classificar(media_risco))
print("-" * 60)

print("\nConclusão:")

print("-" * 60)
if media_risco <= 2:
    print(
        "A missão permaneceu estável durante a maior parte da operação."
    )

elif media_risco <= 5:
    print(
        "A missão apresentou instabilidade moderada e exige monitoramento."
    )

else:
    print(
        "A missão apresentou instabilidade relevante durante a operação."
    )
print("-" * 60)