// //this is how we create a user in the mongo database 
// // then below it is creating a books collection database

db.createUser({
    user: 'Jon',
    pwd: 'password',
    customData: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
})
//to view all is db.getUsers()
//to drop user you run db.dropUser('name to delete')

db.books.insert({              //insert takes in a javascript object
    "name": "OOP Programming",
    "publishedDate": new Date(),
    "authors": [       //an array of data here
      { "name": "Jon Snow jr"}, //expects to recieve an object pass in with curly
    ]
}) 

db.books.insert({
    "name": "OOP Programming Python with Stuff",
    "startDate": new Date(),
    "authors": [   
      { "name": "Jon Snow Python"},
    ]
}) 


//----------------------------------------------------------------------------------------------

//insert many takes an array-gives you inserted and acknowledged true
//creates a hash value and unique structure so it can be retrieved 
// //mongo returns a hash value for the id-so it is unique
db.books.insertMany([   
    {
        "name": "Confident Ruby",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Avdi Grimm" }
        ]
    },
    {
        "name": "Python Rocks",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Benjamin Nicklaus" }
        ]
    },
    {
        "name": "Python Broski",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Ben and J" }
        ]
    },
])  


//------------------------------------------------------------------------------------------

//PROJECTION
// // to retrieve certain values/components back use 1's and 0's
// // 1 is what you want and 0 is what you do not want
// // to limit what is returned below
db.books.find(
    {
        name: "Confident Ruby"     // pass in first object here
    },
    {
        _id: 0,
        name: 1,                  // when we want the name use 1
        publishedDate: 1,         // second object we want the published Date
        authors: 1
    }
).pretty()


//-------------------------------------------------------------------------------------------
// REGULAR EXPRESSION  insert below 
db.books.insert({
    "name": "Deep Work: Rules for Focused Success in a Distracted World PYTHON",
    "publishedDate": new Date(),
    "authors": [
        {"name": "cal py Newport"}
    ]
});
// // How to Query for a Portion of a String
// //inserting a new book
// //implementing a regualr expression
db.books.findOne({ name: /.*deep work.*/i }) // when you see text in between slashes means reg expression-trying to match a pattern in a string
// //regardless *match what ever matches deep work for example*
// // the i means it is making it case insensetive 



// // How to Delete Documents 
db.books.remove({name: "OOP Programming"}, 1) //remove one item passing in an explicit number to be removed

//----------------------------------------------------------------------------------------------


// //How to Include Nested Fields in a find Query
// //ability to query document don't care if active
// //starting code below
db.books.insert({
  "name": "Blink",
  "publishedDate": new Date(),
  "authors": [
      { "name": "Malcome Gladwell", "active": "true"},
      { "name": "Ghost Writer", "active": "true"}
  ]
});
// //adjusted code from above
// query the document but don't care if the author is active
db.books.find(
    {
        name: "Blink"
    },
    {
        name: 1,
        publishedDate: 1,
        "authors.name": 1,  //authors is the array with all the objects-mongo goes into array and brings back name attribute
    }
)


//---------------------------------------------------------------------------------------


// //How to check if field exists in a document
db.books.insert( 
    {
      "name": "Deep Work: Rules for Focused Success in a Distracted World",
      "publishedDate": new Date(),
      "reviews": 100,
      "authors": [
        {"name": "Cal Newport"}
      ]
    }
  )
//to run the query there is a specific function
//use the commands below 
db.books.find({ reviews: { $exists: true } })     //if it has the values
db.books.find({ reviews: { $exists: false } })    //if it doesn't have the values
//could be used to clean the databases



