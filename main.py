
from collections import deque

cenarios={
"1 - Processos curtos":[("P1",3,1),("P2",1,1),("P3",2,1)],
"2 - Curtos e longos":[("P1",8,1),("P2",2,1),("P3",1,1)],
"3 - Prioridades diferentes":[("P1",4,3),("P2",2,1),("P3",3,2)]
}
QUANTUM=2

def mostrar(nome,seq,espera,turn):
    print(f"\n=== {nome} ===")
    print("Sequência:")
    print("; ".join([f"{p} de {i} a {f}" for p,i,f in seq]))
    print("\nProc Espera Turnaround")
    for p in espera:
        print(f"{p:>2} {espera[p]:>6} {turn[p]:>10}")
    print(f"Espera média: {sum(espera.values())/3:.2f}")
    print(f"Turnaround médio: {sum(turn.values())/3:.2f}")

def nao_preemptivo(proc,key):
    ordem=sorted(enumerate(proc),key=lambda x:(key(x[1]),x[0]))
    t=0;seq=[];esp={};tur={}
    for _,(n,c,p) in ordem:
        seq.append((n,t,t+c)); esp[n]=t; t+=c; tur[n]=t
    return seq,esp,tur

def rr(proc,q):
    fila=deque([(i,n,c,p) for i,(n,c,p) in enumerate(proc)])
    t=0;seq=[];rest={n:c for n,c,_ in proc};tur={}
    while fila:
        i,n,c,p=fila.popleft()
        u=min(q,rest[n]); seq.append((n,t,t+u)); t+=u; rest[n]-=u
        if rest[n]>0: fila.append((i,n,c,p))
        else: tur[n]=t
    esp={n:tur[n]-c for n,c,_ in proc}
    return seq,esp,tur

for nome,proc in cenarios.items():
    print(f"\n######## {nome} ########")
    mostrar("FCFS",*nao_preemptivo(proc,lambda x:0))
    mostrar("SJF",*nao_preemptivo(proc,lambda x:x[1]))
    mostrar("Prioridade",*nao_preemptivo(proc,lambda x:x[2]))
    mostrar("Round Robin",*rr(proc,QUANTUM))
