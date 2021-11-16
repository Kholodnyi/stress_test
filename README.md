# Stress testing
Example web server with simple api prepared for stress testing.

### Requirements:
 - Python >3.8
 - [docker](https://docs.docker.com/get-docker/) >20.10.7
 - [docker-compose](https://docs.docker.com/compose/install/) >2.1.0

### Setup
Firstly, need to clone the git repository. In cloned directory create config files:
 - `env.django_web_app` with next content:
    ```
    SECRET_KEY="your-very-long-secret-key"
    DB_USER="simple_web_user"
    DB_NAME="simple_web_db"
    DB_PASSWORD="change_me"
    DB_PORT="5432"
    DB_HOST="postgresql"
    ```
 - `env.postgres` with next content:
    ```
    POSTGRES_PASSWORD="change_me"
    ```
And SQL initial script:
 - `postgres_init.sql` (values should be the same as for `env.django_web_app`): 
    ```sql
    CREATE USER simple_web_user WITH PASSWORD 'change_me';
    CREATE DATABASE simple_web_db;
    GRANT ALL PRIVILEGES ON DATABASE simple_web_db TO simple_web_user;
    ```
 
### Run on Linux
To run a web server simply execute `run.sh` file:
```shell
sudo sh run.sh
```
or do it by staring docker-compose manually:
```shell
sudo docker-compose down
sudo docker-compose up -d
```

For initial data generation, need to install python libraries from `requirements.txt` with next command (inside activated environment):
```shell
pip install -r requirements.txt 
```

And then run `generate.py`:
```shell
python3 generate.py
```

Script generate data in DB and create two files: `urls1.txt` and `urls2.txt` 

### Stress testing with Siege

Install [Siege](https://www.joedog.org/siege-manual/#) and follow the instructions for load testing and benchmarking web server


### Example testing results
#### Selecting values from database 
 - `siege -d1 -c500 -t15s --file=urls1.txt`

    ```
    Transactions:                   2958 hits
    Availability:                 100.00 %
    Elapsed time:                  14.49 secs
    Data transferred:              28.32 MB
    Response time:                  0.39 secs
    Transaction rate:             204.14 trans/sec
    Throughput:                     1.95 MB/sec
    Concurrency:                   79.92
    Successful transactions:        2958
    Failed transactions:               0
    Longest transaction:           14.46
    Shortest transaction:           0.00
    ```                                     
 

 - `siege -d1 -c1000 -t15s --file=urls1.txt`

    ```
    Transactions:                   3079 hits
    Availability:                  99.71 %
    Elapsed time:                  14.71 secs
    Data transferred:              31.10 MB
    Response time:                  0.97 secs
    Transaction rate:             209.31 trans/sec
    Throughput:                     2.11 MB/sec
    Concurrency:                  203.01
    Successful transactions:        3079
    Failed transactions:               9
    Longest transaction:           14.59
    Shortest transaction:           0.00
    ```                                     
 
 - `siege -d1 -c1500 -t15s --file=urls1.txt`

    ```
    Transactions:                   3013 hits
    Availability:                  97.60 %
    Elapsed time:                  14.96 secs
    Data transferred:              28.84 MB
    Response time:                  1.28 secs
    Transaction rate:             201.40 trans/sec
    Throughput:                     1.93 MB/sec
    Concurrency:                  256.88
    Successful transactions:        3013
    Failed transactions:              74
    Longest transaction:           14.81
    Shortest transaction:           0.00
    ```                                     
   
#### Inserting values into database
 - `siege -d1 -c500 -t15s --file=urls2.txt`

    ```
    Transactions:                   3476 hits
    Availability:                 100.00 %
    Elapsed time:                  14.26 secs
    Data transferred:               0.33 MB
    Response time:                  0.46 secs
    Transaction rate:             243.76 trans/sec
    Throughput:                     0.02 MB/sec
    Concurrency:                  112.09
    Successful transactions:        3476
    Failed transactions:               0
    Longest transaction:            9.88
    Shortest transaction:           0.00
    ```     

 - `siege -d1 -c1000 -t15s --file=urls2.txt`

    ```
    Transactions:                   2837 hits
    Availability:                  99.68 %
    Elapsed time:                  14.02 secs
    Data transferred:               2.06 MB
    Response time:                  1.57 secs
    Transaction rate:             202.35 trans/sec
    Throughput:                     0.15 MB/sec
    Concurrency:                  318.62
    Successful transactions:        2837
    Failed transactions:               9
    Longest transaction:           11.64
    Shortest transaction:           0.01
    ```       

 - `siege -d1 -c1500 -t15s --file=urls2.txt`

    ```
    Transactions:                   2608 hits
    Availability:                  71.79 %
    Elapsed time:                  14.64 secs
    Data transferred:               5.01 MB
    Response time:                  1.44 secs
    Transaction rate:             178.14 trans/sec
    Throughput:                     0.34 MB/sec
    Concurrency:                  257.37
    Successful transactions:        2608
    Failed transactions:            1025
    Longest transaction:           13.82
    Shortest transaction:           0.00
    ```       