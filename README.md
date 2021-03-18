# stunning-octo-robot
This repo is designed to be used as training

## NOTES

``` bash
docker run -d --name kuard --publish 8080:8080 gcr.io/kuar-demo/kuard-amd64:blue
docker stop kuard
docker system prune # delete all untagged images, all stopped containers etc`
kubectl config get-contexts
kubectl config use-context docker-desktop
```

p30