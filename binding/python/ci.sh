#!/bin/sh

if [ "$CONFIG" = "python3-binding" ]; then
	PIP=pip3
	PYTHON=python3
elif [ "$CONFIG" = "python2-binding" ]; then
	PIP=pip2
	PYTHON=python2
else
	echo "invalid CI config" 2>&1
	exit 1
fi

$PIP install --upgrade pip
$PIP install cython
$PIP install autopxd
$PYTHON setup.py clean
$PYTHON setup.py build_ext --inplace
$PYTHON test.py

set -v +e
$PYTHON test_issue23.py 0
$PYTHON test_issue23.py 1
$PYTHON test_issue23.py 2
$PYTHON test_issue23.py 3
$PYTHON test_issue23.py 4
$PYTHON test_issue23.py 5
$PYTHON test_issue23.py 6
