# Openshift DevSpaces

Install the DevSpaces operator. 
```
oc apply -k components/operators
```

The DevSpace operator should install the DevWorkspace operator so
there should be (2) operators installed.
```
oc get operators
```
```
NAME                                                              AGE
devspaces.openshift-operators                                     20d
devworkspace-operator.openshift-operators                         20d
```

Install Openshift DevSpaces (Che) Cluster
```
oc apply -k components/stack
```

The DevSpaces stack can take up to 10 minutes to populate its
registries and become ready.

Look for the following pods to be ready:
```
NAME                                   READY   STATUS    RESTARTS   AGE
che-gateway-55697854bf-twq47           4/4     Running   0          77s
devfile-registry-577789b564-5wbqh      1/1     Running   0          8m7s
devspaces-7679d5cfcb-8lzw4             1/1     Running   0          63s
devspaces-dashboard-65cf874b95-v9f9c   1/1     Running   0          2m
plugin-registry-746bb64444-j26hw       1/1     Running   0          7m54s
```

### Teardown

Delete the DevSpaces cluster instance and the `devspaces` namespace.

```
oc delete operator devworkspace-operator.openshift-operators devspaces.openshift-operators
```

Why do they re-appear if the subscription is deleted?
