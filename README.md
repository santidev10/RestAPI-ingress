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



