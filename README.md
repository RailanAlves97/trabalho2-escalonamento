# Trabalho 2 — Sim# Trabalho 2 — Simulador de Escalonamento de Processos

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Sistemas Operacionais  
**Professor:** Guibson Krause  
**Integrante:** Railan Alves Souza  
**Linguagem:** Python 3

## Objetivo

Desenvolver um simulador simples de escalonamento de processos para demonstrar como diferentes algoritmos organizam a execução de processos na CPU e calcular os respectivos tempos de espera e de turnaround.

## Algoritmos implementados

- **FCFS (First Come, First Served):** executa os processos na ordem em que aparecem na lista.
- **SJF (Shortest Job First):** executa primeiro o processo com menor tempo de CPU.
- **Prioridade:** executa primeiro o processo com menor número de prioridade, considerando que números menores representam prioridades mais altas.
- **Round Robin:** distribui o tempo de CPU entre os processos em turnos, utilizando quantum igual a 2 unidades de tempo.

## Cenários de teste

O programa utiliza três cenários de teste, conforme os dados definidos para o trabalho. Em cada cenário, os quatro algoritmos são executados para permitir a comparação dos resultados.

Todos os processos chegam no instante zero.

## Como executar

É necessário ter o Python instalado no computador.

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o terminal integrado.
3. Execute o seguinte comando:

```powershell
python main.py
```

## Resultados apresentados

Para cada algoritmo e cenário, o programa apresenta:

- Sequência de execução dos processos, com os instantes de início e término de cada segmento.
- Tempo de CPU de cada processo.
- Tempo de turnaround de cada processo.
- Tempo de espera de cada processo.
- Tempo médio de espera.
- Turnaround médio.

## Critérios de cálculo

**Turnaround:** tempo decorrido entre a chegada do processo e sua conclusão.

**Tempo de espera:** tempo em que o processo permanece aguardando para utilizar a CPU.

Como todos os processos chegam no instante zero e não são considerados custos de troca de contexto, os cálculos utilizam os tempos de execução definidos em cada cenário.

## Considerações finais

O simulador permite observar como diferentes algoritmos de escalonamento produzem sequências de execução e tempos de espera distintos, mesmo quando utilizam os mesmos processos. Os resultados ajudam a comparar o comportamento de cada algoritmo nos cenários propostos.

