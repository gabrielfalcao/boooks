# Boooks


## Preparing the environment


Ensure that you have python 2.7


```bash
pip install -U pip distribute virtualenvwrapper  # update global dependencies
mkvirtualenv boooks  # create a virtual env
pip install -r development.txt  # install project dependencies (local, because are only used by this project)
```

## Prepare the database

1. Ensure that mysql is running

```bash
brew info mysql
```
Then follow the instructions to run mysql

2. Prepare the database before running `make run`

```bash
make db
```


## Building assets and running the project

```bash
workon boooks  # enter the virtual env where all the project dependencies are installed
python manage.py assets build  # building dependencies
make run  # running the server on http://localhost:8000
```

now go to [http://localhost:8000](http://localhost:8000)


## Deploying

First, ensure that you have amazon credentials and github token and that those are exported as environment variables:

```bash
export AWS_ACCESS_KEY_ID="yourkeyid"
export AWS_SECRET_ACCESS_KEY="yoursecretkey"
export GITHUB_TOKEN="toktoktok"
```

Then make sure that you edit the file `deploy/vpcs/boooks.yml` and change the value under `ansible_roles_path` to the path where you cloned the boooks repository plus `/deploy`

Last thing, ensure that you have the ssh key `weedlabs-master.pem` at `~/.ssh`

```bash
cd deploy
floresta vpcs/boooks.yml --yes --ensure-vpc --inventory-path="inventory" --ansible -vvvv -M library -u ubuntu --extra-vars='{"github_token":"$(GITHUB_TOKEN)","AWS_ACCESS_KEY_ID":"$(AWS_ACCESS_KEY_ID)","AWS_SECRET_ACCESS_KEY":"$(AWS_SECRET_ACCESS_KEY)"}'
```

### Listing machines

```bash
cd deploy
floresta vpcs/boooks.yml --list-machines
```
