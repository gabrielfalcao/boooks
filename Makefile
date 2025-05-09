all: test

.PHONY: deploy

test: unit functional

prepare:
	@pip install -q curdling
	@curd install -r development.txt

clean:
	@git clean -Xdf # removing files that match patterns inside .gitignore

unit:
	@python manage.py unit

functional: db
	@python manage.py functional

acceptance:
	@python manage.py acceptance

shell:
	python manage.py shell

run: static
	python manage.py run

check:
	python manage.py check


migrate-forward:
	@[ "$(reset)" == "yes" ] && echo "drop database if exists boooks_db_local;create database boooks_db_local" | mysql -uroot || echo "Running new migrations..."
	@alembic upgrade head

migrate-back:
	@alembic downgrade -1

db:
	echo "drop database if exists boooks_db_local;create database boooks_db_local" | mysql -uroot
	python manage.py db

docs:
	markment -t .theme spec
	open "`pwd`/_public/index.html"

prod-simulation:
       PYTHONPATH=`pwd` PORT="4000" DOMAIN="0.0.0.0" REDIS_URI="redis://localhost:6379" gunicorn --worker-class boooks.upstream.WebsocketsSocketIOWorker boooks.server:application

static:
	bower install
	python manage.py assets build

deploy:
	git sync
	cd deploy && floresta vpcs/boooks.yml --yes --inventory-path="inventory" --ansible -vvvv --tags=refresh -M library -u ubuntu --extra-vars='{"github_token":"$(GITHUB_TOKEN)"}'


ssh:
	cd deploy && floresta vpcs/boooks.yml --ssh=boooks-web
