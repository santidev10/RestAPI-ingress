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

2) Created the apps and push them to docker

[ec2-user@ip-172-31-64-74 src]$ sudo docker run -p 5000:5000 -d santi10/add:1
a3eafee0b51aeb3036c397f268852971b16c2b05fb56a426fc4afe3005e7ab3c
[ec2-user@ip-172-31-64-74 src]$ sudo docker run -p 5001:5000 -d santi10/substract:1
9beb29471509c9d54b59644d136307537e2b63a9845a45d00d544394e9538861
[ec2-user@ip-172-31-64-74 src]$ sudo docker run -p 5002:5000 -d santi10/division:1
f25240c2d1cfd22cbf8e69fd17fee489c56c9413e92ee37f7c39db67476fe9cf
[ec2-user@ip-172-31-64-74 src]$ sudo docker run -p 5003:5000 -d santi10/random:1
15edf3581db91a3b93bc46330511e4c5addb33ab29b94110d6e0007fe55070ea
[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/add:1
[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/substract:1
[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/division:1
[ec2-user@ip-172-31-64-74 src]$ sudo docker push santi10/random:1



