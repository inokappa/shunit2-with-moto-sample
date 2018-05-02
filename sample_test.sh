#!/usr/bin/env bash
# filename: sample_test.sh

. ./sample.sh

oneTimeSetUp() {
  #######################################
  # moto_server の起動, S3 バケットを作成, S3 バケットにオブジェクトを登録
  #######################################

  moto_server s3 > /dev/null 2>&1 &
  echo "foo bar baz" > data1.txt
  aws --endpoint=http://127.0.0.1:5000 s3api create-bucket --bucket=sample-bucket > /dev/null
  aws --endpoint=http://127.0.0.1:5000 s3api put-object --bucket=sample-bucket --key=data1 --body=data1.txt > /dev/null
  rm -f data1.txt
}

oneTimeTearDown() {
  #######################################
  # moto_server の停止
  #######################################

  pid=$(ps aux | grep [m]oto_server | awk '{print $2}')
  kill ${pid}
}


testGetObjects() {
  #######################################
  # get_objects のテスト
  #######################################

  assertEquals "$(get_objects 'sample-bucket' 'data1')" "foo bar baz"
}

. ./shunit2
