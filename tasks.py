import sys
from invoke import run, task

@task
def readme(context):
    try:
        run("gh-md-toc --insert README.md && rm -f README.md.*.*")
    except Exception:
        sys.exit(1)

@task
def test(context):
    try:
        run("_ENV=test ./sample_test.sh && python -m unittest sample.py")
    except Exception:
        sys.exit(1)
