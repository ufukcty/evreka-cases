## Evreka Case

## Case 1 - Navigation Record

### How to run

```bash
    docker-compose up -d
```

### Endpoints

1- Navigation

```bash
/navigation/navigation/
```

2- Vehicle
```bash
/navigation/vehicle/
```

##Cache Methods:

Redis (included Currency Value) TTL : DEFAULT TIMEOUT

## How to run tests

```bash
    python manage.py tests navigation_record
```

## Case 2 - 

### Endpoints

Operation

```bash
/collection/operation/
```

Bin

```bash
/collection/bin/
```

Bin Operation

```bash
/collection/bin-operation/
```

##suggestions

1. Caching and Redis can be used.
2. Cache Timeout can be arranged. (CACHE_TLL' = DEFAULT_TIMEOUT we can change the value instead of using)
3. Timeseries data degrades performance while data grow up. This applies to standard databases. But timeseries-oriented databases (InfluxDB and TimescaleDB) can used. In this way, scalability can be resolved.
4. Fast API can be used instead of Django and Rest Framework.