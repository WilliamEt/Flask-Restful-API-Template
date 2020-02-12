# Flask-Restful-API-Template
A template for restful api project with flask
## Install python dependencies
The local dev environment requires installation of Jinja2, flask-sqlalchemy, etc, which can be installed via:
```shell script
pip install -r requirements.txt
```
It's better to build a virtual python environment first.
```shell script
# python3
virtualenv venv -p python3.7
# activate
source venv/bin/activate
```

## Run the template
After installation of dependency package, the template can be run via:
```shell script
(.venv)host>python manage runserver
```
Then open the browser or postman tool, input http://127.0.0.1:5000/api/v1.0/, you will get
```json
{
  "hello": "world"
}
```