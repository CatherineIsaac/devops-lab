# Hello DevOps

A minimal Python HTTP application packaged with Docker.

## Requirements

- Docker

## Build the image

docker build -t hello-devops:v1 .

## Run the application

docker run -d --name hello-devops-app -p 8000:8000 hello-devops:v1

## Test the endpoint

curl http://localhost:8000

Expected response:

Hello from my DevOps application!
