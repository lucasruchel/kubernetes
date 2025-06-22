# Modulo 2

## Construção da imagem

Será construída uma imagem com a tag kapp:**$VERSION**, sendo que a versão será de acordo com a versão definida no arquivo pyproject.toml

```bash
chmod +x scripts/build-image.sh
./scripts/build-image.sh
```

## Upload da imagem no Docker Hub

Para fazer o upload da imagem no Docker Hub é necessário definir as variáveis **$DOCKER_HUB_USER** e **$DOCKER_HUB_TOKEN**, altere no comando a baixo para permitir o envio para ser repositório.

É assumido que existe um repositório no DockerHub na conta **$DOCKER_HUB_USER** que possua o nome **kapp**

```bash
chmod +x scripts/push-image.sh
./scripts/push-image.sh
```

## Criação do cluster e componentes no kind

Criação do cluster kubernetes utilizando o Kind (Kubernetes in Docker) com 3 nós. 1 nó master e 2 workers.

```bash
kind create cluster --config manifests/multi-node.yml
```

Criação dos recursos necessários no kubernetes para exposição da aplicação. Foi utilizado a criação de um namespace chamado **kapp**, dentro do namespace foi definido um deployment com a aplicação armazenada no dockerhub, altere no arquivo **deployment.yml** o usuário do **docker Hub**.

```bash

kubectl apply -f manifests/namespace.yml
kubectl apply -f manifests/deployment.yml
kubectl apply -f manifests/service.yml

```

## Teste da aplicação

Para testes da aplicação foi utilizado o kubectl proxy:

```bash

kubectl proxy --port=8080

```

Para acessar a aplicação é necessário utilizar o browser no seguinte endereço:

```

http://localhost:8080/api/v1/namespaces/kapp/services/kapp/proxy/

```
