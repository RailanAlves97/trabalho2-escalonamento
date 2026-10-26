from collections import deque
from copy import deepcopy

class Processo:
    def __init__(self, nome, cpu, prioridade):
        self.nome = nome
        self.cpu = cpu
        self.prioridade = prioridade

def imprimir_resultado(nome_algoritmo, agenda, processos, turnaround, espera):
    print("\n" + "=" * 60)
    print(nome_algoritmo)
    print("=" * 60)

    print("Sequência de execução:")
    print("; ".join(f"{p} de {i} a {f}" for p, i, f in agenda))

    print("\nProcesso | CPU | Turnaround | Espera")
    print("-" * 40)

    for p in processos:
        print(f"{p.nome:8} | {p.cpu:3} | {turnaround[p.nome]:10} | {espera[p.nome]:6}")

    media_espera = sum(espera.values()) / len(processos)
    media_turn = sum(turnaround.values()) / len(processos)

    print("-" * 40)
    print(f"Espera média: {media_espera:.2f}")
    print(f"Turnaround médio: {media_turn:.2f}")

def fcfs(processos):
    tempo = 0
    agenda = []
    turnaround = {}
    espera = {}

    for p in processos:
        inicio = tempo
        tempo += p.cpu
        agenda.append((p.nome, inicio, tempo))
        turnaround[p.nome] = tempo
        espera[p.nome] = tempo - p.cpu

    imprimir_resultado("FCFS", agenda, processos, turnaround, espera)

def sjf(processos):
    ordem = sorted(enumerate(processos), key=lambda x: (x[1].cpu, x[0]))
    ordem = [p for _, p in ordem]

    tempo = 0
    agenda = []
    turnaround = {}
    espera = {}

    for p in ordem:
        inicio = tempo
        tempo += p.cpu
        agenda.append((p.nome, inicio, tempo))
        turnaround[p.nome] = tempo
        espera[p.nome] = tempo - p.cpu

    imprimir_resultado("SJF", agenda, processos, turnaround, espera)

def prioridade(processos):
    ordem = sorted(enumerate(processos), key=lambda x: (x[1].prioridade, x[0]))
    ordem = [p for _, p in ordem]

    tempo = 0
    agenda = []
    turnaround = {}
    espera = {}

    for p in ordem:
        inicio = tempo
        tempo += p.cpu
        agenda.append((p.nome, inicio, tempo))
        turnaround[p.nome] = tempo
        espera[p.nome] = tempo - p.cpu

    imprimir_resultado("Prioridade", agenda, processos, turnaround, espera)

def round_robin(processos, quantum=2):
    fila = deque()
    restante = {}
    turnaround = {}
    agenda = []

    for p in processos:
        fila.append(p)
        restante[p.nome] = p.cpu

    tempo = 0

    while fila:
        p = fila.popleft()

        inicio = tempo
        executar = min(quantum, restante[p.nome])

        tempo += executar
        restante[p.nome] -= executar

        agenda.append((p.nome, inicio, tempo))

        if restante[p.nome] > 0:
            fila.append(p)
        else:
            turnaround[p.nome] = tempo

    espera = {}

    for p in processos:
        espera[p.nome] = turnaround[p.nome] - p.cpu

    imprimir_resultado(f"Round Robin (quantum={quantum})",
                       agenda, processos, turnaround, espera)

cenarios = [
    ("Cenário 1 - Processos curtos",
     [Processo("P1",3,1), Processo("P2",1,1), Processo("P3",2,1)]),

    ("Cenário 2 - Curtos e longos",
     [Processo("P1",8,1), Processo("P2",2,1), Processo("P3",1,1)]),

    ("Cenário 3 - Prioridades diferentes",
     [Processo("P1",4,3), Processo("P2",2,1), Processo("P3",3,2)])
]

for titulo, lista in cenarios:
    print("\n\n" + "#" * 60)
    print(titulo)
    print("#" * 60)

    fcfs(deepcopy(lista))
    sjf(deepcopy(lista))
    prioridade(deepcopy(lista))
    round_robin(deepcopy(lista), quantum=2)