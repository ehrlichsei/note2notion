const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    const data = { title: 'My Page', message: 'Hello, world!' };
    res.render('index', data);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
