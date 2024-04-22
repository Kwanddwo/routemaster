# routemaster
```A web app for managing deliveries and calculating routes```

# Activate virtual environment:
source env/Scripts/activate

# Create requirements file:
pip freeze > requirements.txt

# Install requirements:
pip install -r requirements.txt

# Setting the Google maps api key:
export MAPS_API_KEY={key}
or in python: os.environ['MAPS_API_KEY'] = '{key}'
