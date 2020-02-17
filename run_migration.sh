#!/bin/bash

if [ -z $1 ]; then
    printf "ERROR: please use as 1st argument the Elastic Search hostname/ip address you want to connect to.\n" 1>&2
    exit 1
fi

if [ -z $2 ]; then
    printf "ERROR: please use as 2nd argument the Elastic Search port you want to connect to.\n" 1>&2
    exit 1
fi

# Resolves in which directory is this file located so it does not matter from which path it is being called
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
export DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
echo "SCRIPT DIR:$DIR"
source activate glados-es
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

export PYTHONPATH=$DIR/src:$PYTHONPATH
echo "Cleaning python cache at $DIR/src"
find $DIR/src | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
python -m glados.ws2es.migration_handler -A -D --production --host $1 --port $2 --ignore-warning 2>./mig_stderr.out
source deactivate glados-es
