const express = require('express');
const app = express();

app.get('/oi', (req, res) => {
    res.send('Oi do JavaScript microservice!');
});

app.listen(3000, () => {
    console.log('Server rodando na porta 3000');
});
