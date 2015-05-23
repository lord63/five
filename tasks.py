#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task, run


@task
def test():
    run("py.test -v --pep8 --cov=five/test/ five/test/")


@task
def clean():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf five.egg-info")
    print("Cleaned up.")


@task
def publish(test=False):
    if test:
        run("python setup.py register -r testpypi sdist upload -r testpypi")
    else:
        run("python setup.py register -r pypi sdist upload")
