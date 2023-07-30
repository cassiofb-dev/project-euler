FROM alpine:latest

RUN apk -U upgrade

RUN apk add hyperfine \
            gcc libc-dev \
            rust \
            python3 \
            openjdk17 \
            nodejs \
