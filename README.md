# Openshift DevSpaces

## Install the DevSpaces operator

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

## Install Openshift DevSpaces (Che) Cluster Instance

```
oc apply -k components/stack
```

The DevSpaces stack can take up to 10 minutes to populate its
registries and become ready.

Look for the following pods to be ready in the `devspaces` project:

```
NAME                                   READY   STATUS    RESTARTS   AGE
che-gateway-55697854bf-twq47           4/4     Running   0          77s
devfile-registry-577789b564-5wbqh      1/1     Running   0          8m7s
devspaces-7679d5cfcb-8lzw4             1/1     Running   0          63s
devspaces-dashboard-65cf874b95-v9f9c   1/1     Running   0          2m
plugin-registry-746bb64444-j26hw       1/1     Running   0          7m54s
```

### Sample Applications

```
pip install tensorflow==2.10.0 tensorflow-estimator==2.10 tensorflow-io-gcs-filesystem==0.33 torch==2.0.1 torchvision==0.15.2  
```

Tensorflow 2.10 (versions >v2.10 report runtime errors)

```
python src/tf-beginner.py
```

Pytorch

```
python src/pytorch-gpu.py
```

### Teardown

Delete the DevSpaces cluster instance and the `devspaces` namespace.

```
oc delete -k components/operators
```

### Links

- https://github.com/devfile/developer-images
