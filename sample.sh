#!/usr/bin/env bash -e

function get_objects() {
  #######################################
  # S3 オブジェクトを取得する
  # Globals:
  #   None
  # Arguments:
  #   None
  # Returns:
  #   オブジェクトの内容
  #######################################
 
  bucket=${1}
  key=${2}
  if [ "${_ENV}" == 'test' -o "${_ENV}" == 'debug' ];then
    obj=$(aws --endpoint=http://127.0.0.1:5000/ s3 cp s3://${bucket}/${key} -)
  else
    obj=$(aws s3 cp s3://${bucket}/${key} -)
  fi
  echo $obj
}
