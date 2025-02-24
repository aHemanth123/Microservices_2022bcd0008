const amqp = require('amqplib/callback_api');

console.log("Worker Service is running...");

setInterval(() => {
    console.log("Processing background tasks...");
}, 5000);
