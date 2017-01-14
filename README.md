# Not Missing Out

This repository contains code for https://notmissingout.uk

## Development setup

Install python (version 3.4+) and postgres.

```sh

virtualenv --python=python3 ENV_dev
. ENV_dev/bin/activate
pip install -r requirements/dev.txt
initdb -D notmissingout_db
postgres -D notmissingout_db &
createdb notmissingout
createuser -d notmissingout
cd notmissingout
DATABASE_URL=postgresql://notmissingout@localhost:5432/notmissingout DJANGO_DEBUG=true python manage.py migrate
DATABASE_URL=postgresql://notmissingout@localhost:5432/notmissingout DJANGO_DEBUG=true python manage.py runserver
```

To update requirements/dev.txt:

```sh

deactivate
rm -r ENV_dev
virtualenv --python=python3 ENV_dev
. ENV_dev/bin/activate
pip install -r requirements/dev.in
pip freeze > requirements/dev.txt
```
