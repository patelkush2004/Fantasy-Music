// this data model is for the overall data of the app. it will store all 500 artists and their data

const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const overallSchema = new Schema({
    rank: {
        type: Number, 
        required: true
    },
    artist: {
        type: String,
        required: true
    },
    totalStreams: {
        type: Number, 
        required: true
    },
    dailyStreams: {
        type: Number,
        required: true
    },
    artistPicture: {
        type: String,
        required: true
    }
})

const Overall = mongoose.model('overall', overallSchema, 'overall'); //

module.exports = Overall;
