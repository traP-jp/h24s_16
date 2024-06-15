FROM node:20.11.1-alpine3.19

WORKDIR /app

COPY ./client .

RUN npm ci && npm run build