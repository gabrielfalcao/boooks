# Boooks

## Running


Ensure that you have python 2.7


```bash
pip install -U pip distribute virtualenvwrapper
pip install -r development.txt
python manage.py assets build
make run
```

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
