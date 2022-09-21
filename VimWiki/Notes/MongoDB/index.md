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
to show all databases in the cluster:
- $ show dbs
to choose an specific database:
- $ use <database_name>
now 'db' is pointing to your desire database.
to show all collections in said db:
- $ show collections
to find under the query '"<key>":"<value>"':
- $ db.<collection>.find({query})
to iterate the cursor use 'it'
to count number of values that fullfil query, append '.count()' to the query.

to get one document:
- $ db.<collection>.findOne()

to insert a document
- $ db.<collection>.insert(<document>)
to insert many documents:
- $ db.<collection>.insert([<document1>,<document2>,..,,<documentN>])
as default if many are inserted they are done in order!
to change order you need to add the 'ordered' option:
- $ db.<collection>.insert([<document1>,<document2>,..,,<documentN>],{'ordered': false})

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
