import unittest
import json
from moto import mock_s3
import boto3

def putObject(contents, key):
    '''生成した JSON データを S3 バケットに put する
    '''

    s3 = boto3.client(service_name='s3')
    s3.put_object(ACL='private',
                  Body=contents,
                  Bucket='holiday-py',
                  Key=key)


class SampleTest(unittest.TestCase):
    @mock_s3
    def test_put_object(self):
        s3 = boto3.resource('s3', region_name='ap-northeast-1')
        s3.create_bucket(Bucket='holiday-py')

        contents = {'2017-01-01': '元日',
                    '2018-12-24': '振替休日',
                    '2019-01-14': '成人の日'}
        putObject(json.dumps(contents), 'data.json')

        data = '{"2017-01-01": "元日", "2018-12-24": "振替休日", "2019-01-14": "成人の日"}'
        body = s3.Object('holiday-py', 'data.json').get()['Body'].read().decode("utf-8")
        sorted_body = {}
        for k, v in sorted(json.loads(body).items(), key=lambda x: x[0]):
            sorted_body[k] = v

        self.assertDictEqual(sorted_body, json.loads(data))
