# Notes on MongoDB

ejemplo:
usuario: m001-student
password: m001-mongodb-basics

## import/export (JSON), restore/dump (BSON)

mongodump --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"

mongoexport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --collection=sales --out=sales.json

mongorestore --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"  --drop dump

mongoimport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --drop sales.json


 - Namespace - The concatenation of the database name and collection name is called a namespace.



## Explore Data - Queries

first login to your cluster (conect to Atlas cluster)
- $ mongo "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/admin"

### commmand line

- to iterate the cursor use 'it'
- to count number of values that fullfil query, append '.count()' to the query.


You can do operations on One or Many documents, you need to use de "updateOne" or "updateMany" commmand and it can take many different operators inside, for instance:
* to 'increment' the number use "$inc":
    - db.zips.updateMany({ "city": "HUDSON" }, { "$inc": { "pop": 10 } })
* to 'set' a value use "$set":
    - db.zips.updateOne({ "zip": "12534" }, { "$set": { "pop": 17630 } })
* to 'add' to an array a value, use "$push":
    - db.grades.updateOne({ "student_id": 250, "class_id": 339 },
                    { "$push": { "scores": { "type": "extra credit",
                                             "score": 100 }
                                }
                     })
Only deleteOne if deleting by "_id"

to delete many files that fullfil some query:
- db.<collection>.deleteMany(<query>)

to delete a collection:
- db.<collection>.drop()
