# Módulo 4

Objetivo: Demonstrar as restrições para execução de PODs utilizando Taint e Tolerations.

Atividade: Considerando o uso do kind, crie um cluster com 1 nodes workrs representando o nodepool A e 2 nodes workers representando o nodepool B

A ideia é que os nodes pools tenham esta característica: (no caso do kind isso ficará apenas convencionado os nodepools serão iguais)

nodepool - tipo A
 - hardware=low
 - Apps básicas = ngnix

nodepool - tipo B
 - hardware=high
 - Apps Criticas = apache

Etapas:
- Fazer o deploy do nginx sem ter configurado taints e tolerations
- Configurar taint e tolerations
- Fazer o deploy de apache

## Criação do cluster Kubernetes utilizando o **kind** (Kubernetes in Docker)

O ambiente criado será um cluster com 4 nós. 1 nó master e 3 workers.

```bash
   kind create cluster --config manifests/multi-node.yml
```

## Criação do deployment sem Taint

Será criado um namespace chamado **modulo-4**, neste namespace será adicionado o deployment **nginx-deployment** com apenas 1 réplica.

```bash

kubectl apply -f manifests/namespace.yml
kubectl apply -f manifests/deployment-nginx.yml

```

Observar os nós em que os PODs foram criados

```bash
   kubectl get pods -o wide
```

## Definição dos Taints e Tolerations

Os seguintes nós estão dispiníveis e serão aplicadas os Taints de acordo com o esquema:
- kind-worker    hardware=low:NoExecute
- kind-worker2   hardware=high:NoExecute
- kind-worker3   hardware=high:NoExecute

Comandos:

```bash
kubectl taint nodes kind-worker hardware=low:NoExecute --overwrite
kubectl taint nodes kind-worker2 kind-worker3 hardware=high:NoExecute --overwrite
```

## Ajustes nos manifestos para Tolerar as restrições dos nós

```bash
   
   kubectl apply -f manifests/deployment-apache-with-toleration.yml
   kubectl apply -f manifests/deployment-nginx-with-toleration.yml

```

