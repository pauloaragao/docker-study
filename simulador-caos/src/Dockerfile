FROM node:25-slim
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN apt update && apt install stress --yes
COPY . .
RUN npm run compile
EXPOSE 3000

USER pauloaragao
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "executable" ]
CMD ["npm", "start"]
