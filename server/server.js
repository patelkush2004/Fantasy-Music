const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const { MongoClient, ServerApiVersion } = require('mongodb'); // extra

const app = express(); // create express app

app.use(express.json()); 
app.use(cors());

/*
// connect to mongodb
mongoose.connect('mongodb+srv://kushpatel:haTZRTXVWw53OtU3@fantasymusic.ammhffo.mongodb.net/?retryWrites=true&w=majority', { 
    // useNewUrlParser: true, 
    // useUnifiedTopology: true  // these are not required because they are now default
})
.then(() => console.log('MongoDB Connected...'))
.catch(err => console.log(err));
*/

const uri = "mongodb+srv://kushpatel:haTZRTXVWw53OtU3@fantasymusic.ammhffo.mongodb.net/?retryWrites=true&w=majority";
// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});
async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();

    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");

    // routes
    const overallDB = client.db("fantasy_music").collection("overall"); // overall collection of the database

    // landing page
    app.get('/', async (req, res) => {
        res.send('Landing Page');
    });

    // get overall data
    app.get('/overall', async (req, res) => {
        const overallData = await overallDB.find({}).toArray(); // find all data in the overall collection of the database
        res.json(overallData);
    });

    app.listen(3001, () => {
        console.log('Server listening on port 3001');
    });

  } 
  catch (err) {
    console.log(err.stack);
  }
}
run().catch(console.dir); // this calls the async function and the 

