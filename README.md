# Duplicate-Question-Pairs


## Testing on local (Pytest)
```sh
make local-tests
```
or
```sh
make docker-compose
```
## Testing model by providing own input
Execute the following commands on terminal
```sh
docker build -t test .
```
```sh
docker run -it test /bin/bash
```
```sh
cd tests
```
```sh
python run.py
```