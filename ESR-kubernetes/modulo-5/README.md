# Módulo 5

Demonstrar o ciclo de atualização de uma aplicação utilizando o kubernetes. Explorando a feature de rollout do kubernetes.

Etapas: 
- Criar um deployment para uma app qualquer
- Configurar o deployment para instanciar 10 replicas
- Fazer o deploy 
- Deixar em um terminal o status do rollout
- Trocar a versão da image da app
- Reprovisionar e verificar andamento do rollout
- Reverter a app para a versão anterior e  verificar o andamento do rollout


## Criação do cluster Kubernetes utilizando o **kind** (Kubernetes in Docker)

O ambiente criado será um cluster com 4 nós. 1 nó master e 3 workers.

```bash
   kind create cluster --config manifests/multi-node.yml
```

## Criação do deployment com 10 réplicas

Será criado um namespace chamado **modulo-5**, neste namespace será adicionado o deployment **kapp-deployment** com 10 réplicas.

```bash

kubectl apply -f manifests/namespace.yml
kubectl apply -f manifests/deployment.yml

```

Observar o status de lançamento/atualização de um deployment
```bash
   kubectl get deployment -n modulo-5
   kubectl rollout status deployment/kapp-deployment -n modulo-5
```

Realizar a atualização da versão da imagem do container e observar as atualizações dos pods
```bash
   kubectl apply -f manifests/deploymentV2.yml
   kubectl rollout status deployment/kapp-deployment -n modulo-5
```

Realizar o rollback da última implantação do deployment
```bash
   kubectl rollout undo deployment/kapp-deployment -n modulo-5
   kubectl rollout status deployment/kapp-deployment -n modulo-5
```
