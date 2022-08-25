docker rm -f timerservice_cont loggerservice_cont

docker build . -t timerservice -f timerservice/Dockerfile

docker build . -t loggerservice -f loggerservice/Dockerfile

docker run -d --name=timerservice_cont --network=mynet -p 8080:5000 timerservice

docker run -d --name=loggerservice_cont --network=mynet -p 8081:5000 loggerservice
