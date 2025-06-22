#!/bin/bash

cd app/

VERSION=$(cat pyproject.toml | grep version | cut -f2 -d'"')

docker build -t kapp:$VERSION .