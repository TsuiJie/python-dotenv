# dotenv-python
read .env(-ish) configuration file for python web applications

## Feature

* clean code base
* simple api
* adheres to recent .env regulation

## Install

```
pip install dotenv-python
```

## API

Put .env file at root directory.

Learn about .env file from [https://github.com/bkeepers/dotenv](https://github.com/bkeepers/dotenv)

* Initialize

```
from dotenv import DotEnv


# if .env file is at the same directory
dotenv = DotEnv()
# or else
dotenv = DotEnv('/path/to/your/.env')

```

* Get value by key

```
# if not exist or value is 'null', None return
value = dotenv.get('KEY')
# or you can specify a default value
value = dotenv.get('KEY', 'default')
```

* Check if key exists

```
# True if exists and False if not
exist = dotenv.has('KEY')
```

* Get all env data as Dict

```
data = dotenv.all()
```

* Print all data to screen

```
dotenv.dump()
```

