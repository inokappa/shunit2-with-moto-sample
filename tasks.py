import sys
from invoke import run, task

@task
def shunit(context):
    try:
        run("_ENV=test ./sample_test.sh")
    except Exception:
        sys.exit(1)

@task
def unittest(context):
    try:
        run("python -m unittest sample.py -v")
    except Exception:
        sys.exit(1)
