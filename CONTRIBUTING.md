# Contributing

## Unit-tests

```console
docker build -t reverse-arr:dev . \
  && docker run --rm -it reverse-arr:dev python -m unittest -v main_test
```
