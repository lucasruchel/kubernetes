#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")/../app/

VERSION=$(cat pyproject.toml | grep version | cut -f2 -d'"')

docker build -t kapp:$VERSION .