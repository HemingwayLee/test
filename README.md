# Why we need the cloud
* Reduce the cost of maintaining Hardware & Software & IT related stuff
  * VM services are easier to use/setup/deploy/snaphot/update/rollback
    * Bs-series: low-cost solution
    * Fsv2: Compute optimized
    * Dv3: general purpose
    * Ev3: Memory optimized
  * Monitoring services is easier (e.g., charts/reports/status)
  * Easier to do Disaster recovery (DR) and Replication

* Better computational power and pay as you go

# Choose between private cloud, public cloud, and hybird cloud

![terms](https://i.imgur.com/Aj0HhN7.jpg)

![pass](https://user-images.githubusercontent.com/8428372/90464008-51d40b00-e147-11ea-86a0-a5f5a175e050.png)

* Most of services on Azure are PasS and IaaS

## Comparison
| AWS | Azure | Google Cloud |
| --- | --- | --- |
| EC2 | Virtual Machines | Compute Engine |
| ECS | Azure Container Service (ACS) |  | 
| EC2 Container Registry | Azure Container Registry (ACR) | Container Registry | 
| EKS | Azure Kubernetes Service (AKS) | Google Kubernetes Engine | 
| Lambda | Azure Functions | Cloud Functions | 
| AWS Auto Scaling | Virtual Machine Scale Sets | Managed instance groups (MIGs) | 
| S3 | Azure Storage Account | Cloud Storage | 
| RDS | SQL Database (or Azure Database for PostgreSQL) | Cloud SQL |   
| DynamoDB | Cosmos DB | Cloud Bigtable | 
| ElastiCache | Azure Redis Cache | Memorystore | 
| AWS CLI | Azure CLI | unified CLI | 

### Comparison
https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services  
https://cloud.google.com/docs/compare/aws  

## Commonly Used Services
* VM
  * for demo
  * easy to setup
  * Pay as you go (if we use ACR, we need to pay everyday)
* Azure Container Registry (ACR)
  * like private Docker Hub
  * We can run containers in Azure Container Instance (ACI), Azure App Service, and Azure Kubernetes Service (AKS) 
  * Easy to setup the same environment
  * From maintenance point of view, limited packaged services reduces the attack surface overall
* Storage Account
* Azure Database for PostgreSQL
* Azure Kubernetes Service

## Architecture
![arch1](https://geekflare.com/wp-content/uploads/2019/09/traditional-vs-new-gen.png)

## Basic commands
![commands](https://geekflare.com/wp-content/uploads/2019/09/docker-architecture.png)

## Compare to VM
| VM | docker container |
| --- | --- |
| Each VM has its own OS | Each container can share OS |
| Boots in Minutes | Boots in seconds |
| Few GBs in size | Few KBs/MBs in size |
| Can move to new host easily | Destroyed or re-created rather than moving |

## Docker Hub
This is the official registry which is used to host various Docker images.

## Private docker registry
* We need to login first:  
```
docker login xxx.azurecr.io
```

* pull from private repo
```
docker pull xxx.azurecr.io/my_nginx:51
```

* push to private repo
```
docker tag my_ubuntu xxx.azurecr.io/my_ubuntu
docker push xxx.azurecr.io/my_ubuntu
```

## docker compose
