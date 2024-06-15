FROM node:20.11.1-alpine3.19

WORKDIR /app

COPY ./frontend .

RUN npm ci && npm run build