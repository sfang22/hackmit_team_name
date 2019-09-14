const functions = require('firebase-functions');
const cors = require('cors')({ origin: true });
const admin = require('firebase-admin');
const serviceAccount = require("path/to/");

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://hack-mit-2e096.firebaseio.com"
});

const database = admin.database().ref('/items');
//Post method

exports.helloWorld = functions.https.onRequest((request, response) => {
    response.send("Hello from Firebase!");
   });
  
exports.addItem = functions.https.onRequest((req, res) => {
 return cors(req, res, () => {

  if(req.method !== 'POST') {
   return res.status(401).json({
    message: 'Not allowed'
   })
  }
  //debugging
  console.log(req.body)

  const item = req.body.item

  database.push({item });
  
  let items = [];
  return database.on('value', (snapshot) => {
   snapshot.forEach((item) => {
    items.push({
     id: "11111",//item.key,
     items: "hello"//item.val().item
    });
   });
   res.status(200).json(items)
  }, (error) => {
   res.status(error.code).json({
    message: `Something went wrong. ${error.message}`
   })
  })

 })
})

