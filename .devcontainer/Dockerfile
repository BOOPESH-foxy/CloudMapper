# state 1 to install graphviz and generate svg
FROM alpine:3.18 AS builder

# install graphviz
RUN apk add --no-cache graphviz

WORKDIR /app
COPY graph.dot .

RUN dot -Tsvg graph.dot -o account-map.svg

# stage 2 to serve only the generated svg file
FROM nginx:alpine

COPY --from=builder /app/account-map.svg /usr/share/nginx/html/index.html
EXPOSE 80