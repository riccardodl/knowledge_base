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
If a pod fails before job completion, the pod will be rescheduled. If not enough resources available the job will not be scheduled. Small chance of duplicates in certain node failure scenarios. Completions and Parallelism attributes. By default a unique label is applied by the job object itself (can be overridden). restartPolicy never will create a lot of "junk" pods, better use onFailure.
You can schedule CronJob (spec.schdule field).

### CHAP:13
ConfigMap is combined with a pod right before it is run. Three ways to use ConfigMap, mount it into a pod (a file created for each entry), environmental variable, created dynamically via command line argument. Secrets can be specified directly with `--from-literal=<key>=<value>`. Secrets are base64 encoded. ConfigMap are UTF-8 text files. To replace a secret is smart to apply the new secret with --dry-run (it will encode it and output on stdout) and then pipe it with `kubectl replace -f -` which reads from stdin. Updates to secrets or configmaps will be pushed to all volumes that use them in a couple of seconds.

### CHAP:14
Role and RoleBinding apply to a namespace, ClusterRole and ClusterRoleBinding to the whole cluster. Cannot use namespaced roles for CRDs (which are not namespaced). AggregationRule to combine existing roles. You can assign bindings to groups.

### CHAP:15
StatefulSet are deployed sequentially and the individual pods are uniquely identifiable, they have an increasing id at the end of the pod name, instead of a random string. We need a headless service to manage the StatefulSet. Headless because it will not have a clusterIp associated to it (No need for load balancing since pods have a unique identity).

### CHAP:16
CLuster admins privileges are required to extend k8s. Extension happen with CRD, or via the CNI/CSI/CRI interface extensions (Container network interface/Storage/Runtime).
Requests flow:
User -> Authentication/Authorization -> Admission control (validation and mutation) -> API Server -> Storage

Admission controllers (there are several) can modify and reject API requests.
Another extension method is CRDs. CRDs are meta-resources, they define resources.

### CHAP:17


### CHAP:18
Filesystems as the source of truth
Code review to ensure quality of changes
Feature flags for staged roll forward and roll back

