#curl -i -H 'Content-Type: application/json' -d @Docker.json localhost:8080/v2/apps/

#curl -X PUT -H "Content-Type: application/json" localhost:8080/v2/apps/hollabolla -d@Docker.json


#curl -X PUT -H "Content-Type: application/json" localhost:8080/v2/apps -d@Docker.json
curl -X POST -H "Content-Type: application/json" localhost:8080/v2/apps -d@Docker2.json
#curl -X PUT -H "Content-Type: application/json" localhost:8080/v2/apps/ubuntu -d@Docker.json
