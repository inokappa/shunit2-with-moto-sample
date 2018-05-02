# CodeBuild + ECR を構築する CloudFormation テンプレート

## なにこれ

CodeBuild + ECR を構築する CloudFormation テンプレート.

## 最初に手動なりで作っておくもの

* CodeBuild と Github の連携

## このテンプレートで作成されるもの

### CodeBuild

* Parameters.CodeBuildProjectNeme に指定した名前のプロジェクトが作成される

### ECR

* Parameters.CodeBuildProjectNeme に指定した名前のリポジトリが作成される
* CodeBuild からコンテナイメージを pull する為の, 以下のようなアクセス許可が設定される

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPushPull",
            "Effect": "Allow",
            "Principal": {
                "Service": "codebuild.amazonaws.com"
            },
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability"
            ]
        }
    ]
}
```

### IAM Role

* CodeBuild に付与する IAM Role が作成される

## スタックを作った後にやること

### ECR

* Docker イメージの作成
* 作成したイメージを ECR に push

```sh
docker build -t shunit2-with-moto-sample .
docker tag shunit2-with-moto-sample:latest 012345678912.dkr.ecr.ap-northeast-1.amazonaws.com/shunit2-with-moto-sample:latest
docker push 012345678912.dkr.ecr.ap-northeast-1.amazonaws.com/shunit2-with-moto-sample:latest
```

## デプロイスクリプトの使い方

### create stack

```sh
./deploy.sh ${AWS_PROFILE} shunit2-with-moto-sample create
```

### update stack

```sh
./deploy.sh ${AWS_PROFILE} shunit2-with-moto-sample update
```

### delete stack

```sh
./deploy.sh ${AWS_PROFILE} shunit2-with-moto-sample delete
```

### validate template

```sh
./deploy.sh ${AWS_PROFILE} shunit2-with-moto-sample validate
```
