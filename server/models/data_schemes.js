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
/*
const billboardHot100ArtistsSchema = new Schema({
    rank: {
        type: Number, 
        required: true
    },
    artist: {
        type: String,
        required: true
    },
    artistPicture: {
        type: String,
        required: true
    },
})

const billboardHot200AlbumsSchema = new Schema({
    rank: {
        type: Number, 
        required: true
    },
    album: {
        type: String,
        required: true
    },
    artist: {
        type: String,
        required: true
    },
    albumPicture: {
        type: String,
        required: true
    },
})

const billboardHot200SongsSchema = new Schema({
    rank: {
        type: Number, 
        required: true
    },
    song: {
        type: String,
        required: true
    },
    artist: {
        type: String,
        required: true
    },
    artistPicture: {
        type: String,
        required: true
    },
})
*/
const Overall = mongoose.model('Overall', overallSchema);
//const BillboardHot100Artists = mongoose.model('BillboardHot100Artists', billboardHot100ArtistsSchema);
//const BillboardHot200Albums = mongoose.model('BillboardHot200Albums', billboardHot200AlbumsSchema);
//const BillboardHot200Songs = mongoose.model('BillboardHot200Songs', billboardHot200SongsSchema);

module.exports = Overall;
//module.exports = BillboardHot100Artists;
//module.exports = BillboardHot200Albums;
//module.exports = BillboardHot200Songs;
