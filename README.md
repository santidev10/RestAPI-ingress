1) Created a Kubernetes cluster in AWS using KOPS:

[ec2-user@ip-172-31-64-74 ~]$ kops create cluster \
 --state=${KOPS_STATE_STORE} \
 --node-count=2 \
 --master-size=t2.medium \
 --node-size=t2.medium \
 --zones=us-east-1a,us-east-1b \
 --name=${KOPS_CLUSTER_NAME} \
 --master-count 1

kops update cluster --name clusters.santigrace.com --yes

2) Created the apps and push them to dockerhub

[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/add:1

[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/substract:1

[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/division:1

[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/random:1


3) Apps source code (add.py, substract.py, division.py, randoms.py) located in src/

4) Kubernetes Services yaml files (add-svc.yml, division-svc.yml, random-svc.yml, substract-svc.yml) located in src/kube-manifests/

5) Ingress Controller and Resource files (default-server-secret.yaml, loadbalancer-aws-elb.yaml, nginx-ingress-daemonset.yml, rbac.yaml, ingressresource_pathbased.yml, nginx-config.yaml, ns-and-sa.yaml) located in src/kube-manifests/ingress-manifests

6) You can access the services such as:

http://ticketmaster.santigrace.com/add?num1=9&num2=7
http://ticketmaster.santigrace.com/substract?num1=43&num2=54
http://ticketmaster.santigrace.com/division?num1=10&num2=3
http://ticketmaster.santigrace.com/random?num1=3
http://ticketmaster.santigrace.com/random



