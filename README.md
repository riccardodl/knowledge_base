
# Introduction
This repo contains all the concepts useful to brush up your knowledge in enterprise software development and DevOps.

## Links
https://kubernetes.io/docs/concepts/overview/components/ official docs, very useful overview


## Commands

### MISC
* `az acr build --resource-group <rg> --registry <acr> --image <image>:<tag> .` __upload image to registry__

### HELM
* `helm repo add bitnami https://charts.bitnami.com/bitnami` __add a helm repo__
* `helm search repo bitnami` __list available images__


### Kubernetes
* `kubectl create secret` __to keep and spread secrets__
* `kubectl get endpoints ratings-api --namespace ratingsapp` __see what you are exposing__
* `kubectl config delete-context <context_name>` __clean kubeconfig context__
* `kubectl config set-context <ctx_name> --namespace=<ns>` __create a new context__
* `kubectl config use-context <ctx_name>` __use context as default__
* `kubectl port-forward [<pod-name> or services/<service-name>] 8080:80` __forward local traffic, to pod or load balancer__
* `kubectl cp <pod-name>:<filepath> <filepath>` __copy file to local machine__
* `kubectl cp $HOME/<filepath> <pod-name>:<filepath>` __copy file from remote machine__
* `$ kubectl get deployments kuard --export -o yaml > kuard-deployment.yaml $ kubectl replace -f kuard-deployment.yaml --save-config` __export a deployment into a file and then store changes__
* `kubectl run -i oneshot` __run a single job once__
* `kubectl proxy` __similar to port forward, but instead of sending TCP traffic you send HTTP requests, port forward is for internal access and debugging, proxy is to forward traffic__
* `kubectl top nodes` __top__
* `kubectl expose deployment <my-deplo>` __To create a service__
* `k get deploy kuard-deployment -o jsonpath --template {.spec.selector.matchLabels}` __Which labels is my deployment matching?__
* `kubectl replace -f <filename> --save-config` __Replace the deployment in the file and save the modified config in its annotation__
* `kubectl rollout status deployments <deployment-name>` __Check the rollout status__
* `kubectl label <resource>` ____
* `k create configmap test-config --from-file=test-config.txt --from-literal=extra-param=extra-value --from-literal=another-param=another-value` __Create ConfigMap__
* `k create secret generic <name> --from-file=<filename>` ____
* `kubectl replace -f -` __Read file from stdin and use it to replace a resource (fx. create with --dry-run -o yaml and then use this to update a secret from files on disk without having to manually base64-encode data)__
* `kubectl auth can-i get pods --subresource=logs` __Can if I'm auth to do a verb__
* `kubectl auth reconcile` __Reapply RBAC changes__
* `kubectl run -it --rm --image busybox busybox ping <svc dns name>` __Run pod interactively and ping__


Examples: `KUARD_LB=$(kubectl get service kuard -o jsonpath='{.status.loadBalancer.ingress[*].hostname}')` __query a specific deployment for a parameter__

### Terraform
* `terraform init --backend-config="<key>=<value>"` ____
* `terraform apply -var="<key>=<value>"` __pass sensitive variqables from command line__
* `terraform show` __look the current state of the infrastructure__
* `TF_VAR_<variable>` __this environment-variable can be set to set the <variable> terraform variable.__
* `terraform state list` __list all resources provisioned via terraform__
* `terraform plan -out=newplan` __write the plan into file, you can follow this with <terraform apply "newplan"__
* `terraform validate` __spellcheck tf files__
* `` ____

### Docker
* `docker run -d --name kuard --publish 8080:8080 gcr.io/kuar-demo/kuard-amd64:blue` ____
* `docker stop kuard` ____
* `docker system prune ` __delete all untagged images, all stopped containers etc__

