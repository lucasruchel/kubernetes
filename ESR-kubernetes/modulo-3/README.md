# Módulo 3

## Criação do cluster Kubernetes utilizando o **kind** (Kubernetes in Docker)

O ambiente criado será um cluster com 5 nós. 1 nó master e 4 workers.

```bash

   kind create cluster --config manifests/multi-node.yml

```

## Criação dos recursos para testes

Será criado um namespace chamado **modulo-3**, neste namespace será adicionado o deployment **kapp-deployment** com apenas 1 réplica.

```bash

kubectl apply -f manifests/namespace.yml
kubectl apply -f manifests/deployment.yml

```

## Execução da Atividade

O intuito é marcar os nós como indisponíveis e verificar o comportamento dos Pods nos nós marcados.

Para verificar o nó em que o **POD** está executando:
```
kubectl get pods -o wide -n modulo-3
```

Para marcar o nó como não agendável:
```
kubectl cordon <NÓ>
```

O comando acima faz com que os PODS em execução no nó marcada como não agendável não sejam alterados, apenas não serão criados novos pods neste nó. Para remover os PODS em execução o seguinte comando:
```
kubectl drain <NÓ> --ignore-daemonsets
```
** Note que o nó pode possuir daemonsets, que são serviços que executam em cada nó do cluster.*
  
Para reestabelecer o nó, podemos executar o comando:
```
kubectl uncordon <NÓ>
```
No entanto, os Pods não serão escalonados para nó novamente até que seja necessário a criação de novos nós.




