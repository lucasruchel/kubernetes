# Módulo 6

A Atividade consiste em criar um registry privado, na qual deverão ser provisionados recursos como a criação de volumes PVC, PV



Etapas: 
- criar toda a estrutura de deployment para um registry privado. ( o registry pode ser de livre escolha: registry, harbor, etc)

- Criar um serviço para permitir o acesso interno ao registry
  
Obs.: Para simular um ambiente real em que as imagens docker sejam mantidas mesmo com o reagendamento do pod contendo o registry, optou-se por utilizar um volume docker e mapear esse volume nos nós workers do kind utilizando o **hostPath**. Recurso não recomendado para produção, sendo recomendado utilizar sistemas de arquivos distribuídos ou recursos do próprio provedor de nuvem.

## Criação do cluster Kubernetes utilizando o **kind** (Kubernetes in Docker)

Inicialmente será necessário criar um volume docker para persistir as alterações no registry mesmo que os nós worker sejam removidos ou o pod do registry seja reagendado.

```bash

docker volume create kind-pv-registry

```

O ambiente criado será um cluster com 4 nós. 1 nó master e 3 workers. Foi ajustado o arquivo contendo a configuração do mapeamento do volume nos nós.

```bash
   kind create cluster --config manifests/multi-node.yml
```

## Criação do deployment com 1 réplicas

Será criado um namespace chamado **modulo-6**.

```bash

kubectl apply -f manifests/namespace.yml

```

Antes de criarmos o nosso deployment com o registry, iremos criar o volume que armazenará os dados do registry, persistindo em caso de parada do cluster ou do POD. O volume será mapeado no deployment através de um PVC que é a solicitação de uso desse recurso pelo POD.

```bash
   kubectl apply -f manifests/registry-pv.yml
   kubectl apply -f manifests/registry-pvc.yml
```


E por fim será adicionado o deployment **registry-deployment** com 1 réplica.

```bash

kubectl apply -f manifests/deployment.yml

```

Será criado um service do tipo ClusterIP, permitindo que os nós tenham acesso dentro do cluster pelo Ip do Serviço ou utilizando o domínio registry.modulo-6.svc.cluster.local

```bash

kubectl apply -f manifests/service.yml

```

