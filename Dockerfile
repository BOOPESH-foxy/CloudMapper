FROM alpine:3.18 AS builder

# install graphviz ()
RUN apk add --no-cache graphviz

WORKDIR /app
COPY graph.dot .

RUN dot -Tsvg graph.dot -o account-map.svg

FROM nginx:alpine

COPY --from=builder /app/account-map.svg /usr/share/nginx/html/index.html
EXPOSE 80
