const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express(); // create express app

app.use(express.json()); 
app.use(cors());

// connect to mongodb
mongoose.connect('mongodb+srv://kushpatel:haTZRTXVWw53OtU3@fantasymusic.ammhffo.mongodb.net/?retryWrites=true&w=majority', { 
    // useNewUrlParser: true, 
    // useUnifiedTopology: true  // these are not required because they are now default
})
.then(() => console.log('MongoDB Connected...'))
.catch(err => console.log(err));

// routes
const DataSchemes = require('./models/data_schemes');

// get overall data
app.get('/', async (req, res) => {
    res.send('Landing Page');
});

// get overall data
app.get('/overall', async (req, res) => {
    const overallData = await DataSchemes.find();
    res.json(overallData);

    res.send('Overall Data');
});

/*
// get billboard hot 100 artists
app.get('/api/billboardHot100Artists', (req, res) => {
    DataSchemes.BillboardHot100Artists.find()
        .then(data => res.json(data))
});

// get billboard hot 200 albums
app.get('/api/billboardHot200Albums', (req, res) => {
    DataSchemes.BillboardHot200Albums.find()
        .then(data => res.json(data))
});

// get billboard hot 100 songs
app.get('/api/billboardHot100Songs', (req, res) => {
    DataSchemes.BillboardHot100Songs.find()
        .then(data => res.json(data))
});
*/

app.listen(3001, () => {
    console.log('Server listening on port 3001');
});

