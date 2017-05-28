# dotenv-python
read .env(-ish) configuration file for python web applications

## Feature

* clean code base
* simple api
* adheres to recent .env regulation

## Install

```shell
pip install dotenv-python
```

## API

Put .env file at root directory.

Learn about .env file from [https://github.com/bkeepers/dotenv](https://github.com/bkeepers/dotenv)

* Initialize

```python
from dotenv import DotEnv


# if .env file is at the same directory
dotenv = DotEnv()
# or else
dotenv = DotEnv('/path/to/your/.env')

```

* Get value by key

```python
# if not exist or value is 'null', None return
value = dotenv.get('KEY')
# or you can specify a default value
value = dotenv.get('KEY', 'default')
```

* Check if key exists

```python
# True if exists and False if not
exist = dotenv.has('KEY')
```

* Get all env data as Dict

```python
data = dotenv.all()
```

* Print all data to screen

```python3
dotenv.dump()
```

## Example

* Your .env file
```shell
  MongoDb='mongodb://localhost:27017/dot'
  Mysql="mysql://localhost:3306/env"
```

* And Your main.py file

```python
from dotenv import DotEnv

dotenv = DotEnv('.env')
dotenv.dump()
print(dotenv.get('MongoDb', 'It isn\'t MongoDb key, it return this message'))
print(dotenv.get('Mon', 'It isn\'t Mon key, it return this message'))
```
