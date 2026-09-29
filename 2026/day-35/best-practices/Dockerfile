FROM node:22-alpine

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY index.js .

USER appuser

CMD ["node", "index.js"]
