FROM alpine:latest

RUN apk -U upgrade

RUN apk add hyperfine gcc libc-dev python3 nodejs
