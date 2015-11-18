# neo4j-flask
An asset tracking application written in Python powered by Flask and Neo4j.

## Usage

Make sure [Neo4j](http://neo4j.com/download/other-releases/) is running first!

**If you're on Neo4j >= 2.2, make sure to set environment variables `NEO4J_USERNAME` and `NEO4J_PASSWORD`
to your username and password, respectively:**

```
$ export NEO4J_USERNAME=username
$ export NEO4J_PASSWORD=password
```

Or, set `dbms.security.auth_enabled=false` in `conf/neo4j-server.properties`.

Then:

```
git clone https://github.com/boltomli/neo4j-flask.git
cd neo4j-flask
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```

[http://localhost:5000](http://localhost:5000)
