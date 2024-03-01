const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const { MongoClient, ServerApiVersion } = require('mongodb'); 
const dotenv = require('dotenv'); 
const path = require('path');

dotenv.config({ path: path.resolve(__dirname, '../.env') }); // load environment variables from .env file

const app = express(); // create express app
app.use(express.json()); 
app.use(cors());

// connect to mongodb
const uri = process.env.MONGODB_URL; 
// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

// Connect the client to the server	(optional starting in v4.7)
client.connect();

// Send a ping to confirm a successful connection
client.db("admin").command({ ping: 1 });
console.log("Pinged your deployment. You successfully connected to MongoDB!");

// routes
const overallDB = client.db("fantasy_music").collection("overall"); // overall collection of the database
const billboardDB = client.db("fantasy_music").collection("billboard_hot_100_artists"); // billboard collection of the database
const billboardAlbumsDB = client.db("fantasy_music").collection("billboard_hot_200_albums"); // billboard collection of the database 
const billboardSongsDB = client.db("fantasy_music").collection("billboard_hot_200_songs"); // billboard collection of the database   

// landing page
app.get('/', async (req, res) => {
    res.send('Landing Page');
});

// get overall data
app.get('/overall', async (req, res) => {
    const overallData = await overallDB.find({}).toArray(); // find all data in the overall collection of the database
    res.json(overallData);
});

// get billboard hot 100 artists data
app.get('/billboard-hot-100-artists', async (req, res) => {
    const billboardData = await billboardDB.find({}).toArray(); // find all data in the overall collection of the database
    res.json(billboardData);
});

// get billboard hot 200 albums data
app.get('/billboard-hot-200-albums', async (req, res) => {
    const billboardAlbumsData = await billboardAlbumsDB.find({}).toArray(); // find all data in the overall collection of the database
    res.json(billboardAlbumsData);
});

// get billboard hot 200 songs data
app.get('/billboard-hot-200-songs', async (req, res) => {
    const billboardSongsData = await billboardSongsDB.find({}).toArray(); // find all data in the overall collection of the database
    res.json(billboardSongsData);
});

app.get('/my-team', async (req, res) => {
    res.send('My Team Page');
});

// add something for selected...
// 22 minutes in video: https://www.youtube.com/watch?v=R81g-2r6ynM

app.get('/predictions', async (req, res) => {
    res.send('Predictions Page');
});

app.listen(3001, () => {
    console.log('Server listening on port 3001');
});
