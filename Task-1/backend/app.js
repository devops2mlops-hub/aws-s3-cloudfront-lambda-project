const express = require('express');
const app = express();

// Root API
app.get('/', (req, res) => {
    res.json({
        status: "ok",
        message: "Backend API is running 🚀"
    });
});

// Optional test route
app.get('/test', (req, res) => {
    res.json({
        message: "Test route working ✅"
    });
});

module.exports = app;
