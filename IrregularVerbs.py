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

while True:
    verbo = random.choice(list(verbos.keys()))
    correto_past, correto_participle = verbos[verbo]

    print(f"\nVerbo: {verbo}")

    resposta_past = input("Simple Past: ").strip().lower()
    if resposta_past == "sair":
        break

    resposta_part = input("Past Participle: ").strip().lower()
    if resposta_part == "sair":
        break
