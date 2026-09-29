FROM ubuntu

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY hello.txt .

EXPOSE 8080

CMD ["cat", "hello.txt"]
