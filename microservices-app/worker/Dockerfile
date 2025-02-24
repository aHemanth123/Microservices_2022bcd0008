# Use Node.js official image
FROM node:18

# Set working directory
WORKDIR /usr/src/app

# Copy application files
COPY package.json ./
RUN npm install

COPY . .

# Run the worker script
CMD ["node", "worker.js"]
