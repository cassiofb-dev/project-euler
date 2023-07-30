FROM alpine:latest

RUN apk -U upgrade

RUN apk add gcc libc-dev python3 nodejs
