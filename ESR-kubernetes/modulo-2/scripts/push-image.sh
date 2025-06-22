# Login em docker hub
echo $DOCKER_HUB_TOKEN | docker login -u $DOCKER_HUB_USER --password-stdin

# Pega versão utilizada para realizar tag
cd app/
VERSION=$(cat pyproject.toml | grep version | cut -f2 -d'"')

docker tag kapp:$VERSION $DOCKER_HUB_USER/kapp:$VERSION

docker push $DOCKER_HUB_USER/kapp:$VERSION


