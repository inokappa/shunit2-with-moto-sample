# shunit2-with-moto-sample

[![Build Status](https://travis-ci.org/inokappa/shunit2-with-moto-sample.svg?branch=master)](https://travis-ci.org/inokappa/shunit2-with-moto-sample)

<!--ts-->
<!--te-->

## これは

shunit2 と moto[server] を組み合わせて awscli をラップしたシェルスクリプトのユニットテストを行うサンプル的なものです.

## .travis.yml

```yaml
sudo: false
language: python
python:
  - 3.6
before_script:
  - aws configure set default.region ap-northeast-1
  - aws configure set aws_access_key_id ''
  - aws configure set aws_secret_access_key ''
script:
  - invoke shunit
  - invoke unittest
```
