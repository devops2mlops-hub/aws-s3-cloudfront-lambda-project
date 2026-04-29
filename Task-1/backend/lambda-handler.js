const serverless = require('serverless-http');
const app = require('./app');

// Lambda handler
module.exports.handler = serverless(app);
