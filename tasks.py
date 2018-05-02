import sys
from invoke import run, task

@task
def readme(context):
    try:
        run("gh-md-toc --insert README.md && rm -f README.md.*.*")
    except Exception:
        sys.exit(1)

@task
def shunit(context):
    try:
        run("_ENV=test ./sample_test.sh")
    except Exception:
        sys.exit(1)

@task
def unittest(context):
    try:
        run("python -m unittest sample.py")
    except Exception:
        sys.exit(1)
