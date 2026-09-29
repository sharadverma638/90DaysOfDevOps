FROM node:22 AS builder

WORKDIR /app

COPY package.json index.js ./

RUN npm run build

FROM node:22-alpine

WORKDIR /app

COPY --from=builder /app/dist/index.js .

CMD ["node", "index.js"]
