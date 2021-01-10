import cors from 'cors';
import express from 'express';
import MongoClient from 'mongodb';

const apiPath = '/api'
const uri = "mongodb+srv://admin:RWdjNx8uvt9e^Z@akcapp.q6och.mongodb.net/AkcApp?retryWrites=true&w=majority";
const client = new MongoClient.MongoClient(uri)

const server = express()
server.use(express.json());
server.use(
  cors({
    origin: 'http://localhost:3000',
    credentials: true,
  })
);

client.connect().then((client, _err) => {
  const db = client.db('AkcApp');
    
  server.listen(3001, () => {
    console.log(`Example app listening at http://localhost:3001`)
  });
  
  server.get(`${apiPath}/breed/:id`, (req, res) => {
    db.collection('BreedData')
      .findOne({ _id: new MongoClient.ObjectId(req.params['id']) })
      .then(data => { res.json(data) })
  });  
  
  server.get(`${apiPath}/breed-table`, (_req, res) => {
    db.collection('BreedData')
      .find({}, { projection: { breed_name: 1, attributes: 1 }})
      .sort({ breed_name: 1 })
      .toArray((_err, result) => { res.json(result) });
  });  
});

client.close();
