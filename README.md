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

### run testcases
```
python3 -m unittest discover -s server/notion_connection/tests -p "test_*.py"

```