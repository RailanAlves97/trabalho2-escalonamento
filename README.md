# Trabalho 2 — Simulador de Escalonamento de Processos

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Sistemas Operacionais  
**Professor:** Guibson Krause  
**Integrante:** Railan Alves Souza  
**Linguagem:** Python 3

## Objetivo

Desenvolver um simulador simples para demonstrar como diferentes algoritmos organizam a execução de processos na CPU.

## Algoritmos implementados

- **FCFS:** executa os processos na ordem da lista.
- **SJF:** executa primeiro o processo com menor tempo de CPU.
- **Prioridade:** executa primeiro o processo com o menor número de prioridade.
- **Round Robin:** divide a CPU em turnos de tempo, utilizando quantum 2.

## Cenários

O programa utiliza os três cenários fornecidos pelo professor e executa os quatro algoritmos em cada um deles.

## Como executar

É necessário ter o Python instalado.

No VS Code, abra o terminal na pasta do projeto e execute:

```powershell
python simulador.py
```

## Resultados

O programa apresenta a sequência de execução, o tempo de espera, o turnaround e as médias de cada algoritmo.