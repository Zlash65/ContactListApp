### Prerequisites

You need to have [NodeJS](https://nodejs.org/en/) and [MongoDB](https://www.mongodb.com/download-center#community) installed on 
your system.


## How to Run the App

1. Open cmd in the current directory where the files have been extracted. And type...
```
  npm install
```
*This should install all the required node modules you'll need to run the app.

2. You can either use the default location to create the database that'd be [ C:\data\db or \data\db depending whether you're using windows or linux/mac ] or you can locally create one in your current 
directory by running the command...
```
mkdir data
```
* This will create a directory in your current workspace.

3. Open a new cmd terminal and run the following command if you're gonna use the default location for database..
```
mongod
```

Or if you created data directory in the current work environment, then run..
```
mongod --dbpath "Path to your data directory"
```
* Dont use the quotes while giving path, also make sure your path looks like PATH\data or so.

4. In the other terminal that is open, run the command..
```
node server.js
```

5. Open up your browser and type [localhost:3000](http://localhost:3000)

