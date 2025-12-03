import random

verbos = {
    "arise": ("arose", "arisen"),
    "be": ("was/were", "been"),
    "become": ("became", "become"),
    "begin": ("began", "begun"),
    "break": ("broke", "broken"),
    "bring": ("brought", "brought"),
    "build": ("built", "built"),
    "buy": ("bought", "bought"),
    "choose": ("chose", "chosen"),
    "come": ("came", "come"),
    "cut": ("cut", "cut"),
    "do": ("did", "done"),
    "drink": ("drank", "drunk"),
    "drive": ("drove", "driven"),
    "eat": ("ate", "eaten"),
    "fall": ("fell", "fallen"),
    "feel": ("felt", "felt"),
    "find": ("found", "found"),
    "fly": ("flew", "flown"),
    "forget": ("forgot", "forgotten"),
    "get": ("got", "gotten"),
    "give": ("gave", "given"),
    "go": ("went", "gone"),
    "have": ("had", "had"),
    "hear": ("heard", "heard"),
    "hold": ("held", "held"),
    "keep": ("kept", "kept"),
    "know": ("knew", "known"),
    "leave": ("left", "left"),
    "lose": ("lost", "lost"),
    "make": ("made", "made"),
    "meet": ("met", "met"),
    "read": ("read", "read"),
    "run": ("ran", "run"),
    "say": ("said", "said"),
    "see": ("saw", "seen"),
    "sell": ("sold", "sold"),
    "sit": ("sat", "sat"),
    "speak": ("spoke", "spoken"),
    "take": ("took", "taken"),
    "write": ("wrote", "written")
}
print("Treino de Verbos Irregulares em Inglês!")
print("Digite 'sair' para encerrar.\n")

def atualizar_pontuacao(acertos):
    return acertos + 1

print("Treino de Verbos Irregulares - 10 Rodadas!")
print("-------------------------------------------")

pontuacao = 0
rodadas = 10

for rodada in range(1, rodadas + 1):
    print(f"\nRodada {rodada}/{rodadas}")
    
    verbo = random.choice(list(verbos.keys()))
    correto_past, correto_part = verbos[verbo]

    print(f"Verbo: {verbo}")

    resp_past = input("Simple Past: ").strip().lower()
    resp_part = input("Past Participle: ").strip().lower()

    if resp_past == correto_past and resp_part == correto_part:
        print("Acertou!")
        pontuacao = atualizar_pontuacao(pontuacao)
    else:
        print("Errou.")
        print(f"O correto é: {correto_past} / {correto_part}")

print("\n-------------------------------------------")
print(f"Jogo encerrado! Sua pontuação final: {pontuacao} de {rodadas}")
print("-------------------------------------------")
