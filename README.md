# Note to notion

create .env in your local, add

````
secret_key = **********************
database_id_inspiration = ******************************
````

### install dependency
```
python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```

### run unit testcases
```
python3 -m unittest discover -s server/tests/unit -p "test_*.py"

```

or run only API connection test
```
python3 -m unittest discover -s server/tests/integration -p "test_notion_api_connection.py"
```

### run flask server
```
python3 app.py
```

### run client web GUI
```
cd client
python -m http.server
```

## port
 the client is on port 8000
 the api is on port 5002



# run locally process

```
cd server
python3 main.py
python3 run_translator.py
```