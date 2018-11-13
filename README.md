Backend Engineer Coding Challenge For TwoSense.ai

### Local Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Local Run
```
FLASK_APP=server.py flask run
```

### Docker Setup
```
docker build . -t twosense
```

### Docker Run
```
docker-compose up
```

### Access
```
http://localhost:5000/api/data?start_date=2018-10-01&end_date=2018-11-01
```
