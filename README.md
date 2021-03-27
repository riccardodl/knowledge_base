p.143

## NOTES

__Deployments__ contain *replicas of* pods, a __pod__ contains one or more __containers__.

Usually a pod contains one container, unless you really want more services linked up together.

Pod is the logical unit of kubernetes. A pod lives and dies on a __node__.

To manage pods you use deployments, which abstracts nodes dying etc.

You want to put a load balancer in front of a deployment (read many pods). What you are creating now is a __Service__.

A service abstracts pods. It exposes an application.
Services can have multiple [types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types).

The service gives a __cluster ip__ (to talk with the cluster) and a __node port__ (if you hit it, traffic gets into one of the pods).

You also need to expose all of this (with AWS you use ELB).

Service and deployment don't know about each other, they manage the same pods using labels. The service is intra-cluster.

__Cluster__ = set of nodes.

Node -> container -> pod -> deployment -> service

Some resources are cluster-wide, some aren't, to access them you need to specify a namespace (fx. kube-system).

RBAC = authorization & authentication -> ````kubectl create rolebinding joe --clusterrole=admin --user=users:joe --dry-run -o yaml```.

A pod request is the amount of resources the node guarantees to have for the pod, the limit is the max the pod can hade. if limit > request resources are given in a best effort manner.

kubectl uses the JSONPath query language to select fields in the returned object.

kubernetes components: API server, persistent storage (etcd) to keep pods manifest, scheduler do autodeploy pods. 

### CHAP.3
Kubernetes proxy is responsible for routing traffic to load-balanced services. Present in every node (daemonSets).
Kubernetes DNS is a deployment.
Dashboard is a deployment as well.
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml`
`http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`
`kubectl -n kube-system describe secret default`

### CHAP.4
Namespaces can be thought as folders.
`k apply -f test.yaml view-last-applied`
to remove a label `k label pods <podname> <label>-`
`port-forward` can also be done against service/<service-name>, but requests will end up in a single pod inside that service. NOT load balanced.

### CHAP.5
Multiple container can be defined in the same pod (via the specs). You can define a mounthPath for the pod and then give the containers mount points (maybe with different names) to the volume. It can be used for caching, sharing resources etc.

### CHAP.6
`kubectl get deployments --show-labels`
`kubectl get deployments -L <deployment-name>`
`kubectl get pods --selector="ver=2, !canary, env in (prod, pre-prod)"`

### CHAP:7
To scale pods, put them in a deployment `kubectl scale deployments/<my-deplo> --replicas=4`
Instead of `kubectl run` use `kubectl create deployment alpaca-prod --image=gcr.io/kuar-demo/kuard-amd64:blue --port=8080` to create a deployment.
`kubectl get endpoints <service> --watch` to see the status of the endpoint, if a deployment is accepting traffic.
With a service listening on a port defined in a NodePorts, any node in the cluster can contact my service. (NodePorts is used to expose services to all nodes of the cluster, clusterIp makes me visible only within the node).
I can SSH tunnel into a node with a NodePort exposed with `ssh <node> -L 8080:localhost:<nodePort>` __You get <nodePort> via kubectl describe service <my-service>__
LoadBalancer extends on NodePort.
For every service, a buddy endpoint is created. Endpoints is what system uses to communicate with a service instead of ClusterIP.

### CHAP:8
Http based load balancing in k8s is called Ingress, it implements the virtual hosting pattern. Multiple ingress files get merged in the ingress controller, which is exposed by a LoadBalancer service. Ingress controller must be installed separately. Contour is an ingress controller that uses Envoy as load balancer. K8s only provides a common ingress specification.
An Ingress object can only refer to an upstream service within the same namespace. However multiple Ingress objects in different namespaces can specify subpaths for the same host, they end up getting merged in the end. This can lead to unexpected routing behaviour. Some ingress controllers allow path rewriting or regex.
 sudo nano /etc/hosts 10.105.120.45

### CHAP:9
Reconciliation loop. ReplicaSets do not own the Pods they create, they use label selector queries. To debug a pod change its label (ReplicaSets will recreate + you have the pod running to debug).
`--cascade=false` flag if you wanna delete the rs definition, but not the pods that were managed by the rs.

### CHAP:10
ReplicaSets manage Pods, Deployments manage ReplicaSets. Relations managed by labels and label selectors.
`k describe deploy` has OldReplicaSet and NewReplicaSet, if I'm in the middle of a rollout, both values will be filled. `k rollout history --revision=<revision-you-wanna-check-if-any>` and `k rollout status` help too. You can `pause` and `resume` rollouts.
When you rollout a deployment the revision gets "recycled", so the original revision (the one you rolled back to) is removed. The recreate strategy simply kills all the pods in a replica set and update the pod spec (rs notices and recreates pods).
Rollout strategy: maxUnavailable you control how many old replicas to kill at a time, with maxSurge you specify you allow provisioning of additional resources, temporarily. Killing of old pods depends on readiness check, you need to specify them on the pod definition, otherwise the deployment controller is running blind.
If you have a deadlock a rollout will never terminate (never report readiness), so, timeout your rollouts (so they get marked failed). Note that if a new pod manages to get rolled out, the timer resets (the timeout only marks progress, not total rollout time).


### CHAP:11
DeamonSets creates a pod on every node, unless a selector is used. DS specifies nodeName field in pod definition. DS are ignored by kube-sched. Reconciliation loop like replicaSets.

### CHAP:12
If a pod fails before job completion, the pod will be rescheduled. If not enough resources available the job will not be scheduled. Small chance of duplicates in certain node failure scenarios. Completions and Parallelism attributes. By default a unique label is applied by the job object itself (can be overridden).

### CHAP:13


### CHAP:14


### CHAP:15


### CHAP:16


### CHAP:17


### CHAP:18

## Links
https://kubernetes.io/docs/concepts/overview/components/ read this


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
* `kubectl proxy` __similar to port forward, but instead of sending TCP traffic you send HTTP requests, port foward is for internal access and debugging, proxy is to forward traffic__
* `kubectl top nodes` __top__
* `kubectl expose deployment <my-deplo>` __To create a service__
* `k get deploy kuard-deployment -o jsonpath --template {.spec.selector.matchLabels}` __Which labels is my deployment matching?__
* `kubectl replace -f <filename> --save-config` __Replace the deployment in the file and save the modified config in its annotation__
* `kubectl rollout status deployments <deployment-name>` __Check the rollout status__
* `kubectl label <resource>` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____
* `` ____

Examples: `KUARD_LB=$(kubectl get service kuard -o jsonpath='{.status.loadBalancer.ingress[*].hostname}')` __query a specific deployment for a parameter__

### Terraform
* `terraform init --backend-config="<key>=<value>"` ____
* `terraform apply -var="<key>=<value>"` ____
* `terraform show` __look the current state of the infrastructure__
* `TF_VAR_<variable>` __this environment-variable can be set to set the <variable> terraform variable.__
* `` ____
* `` ____
* `` ____
* `` ____

### Docker
* `docker run -d --name kuard --publish 8080:8080 gcr.io/kuar-demo/kuard-amd64:blue` ____
* `docker stop kuard` ____
* `docker system prune ` __delete all untagged images, all stopped containers etc`__

