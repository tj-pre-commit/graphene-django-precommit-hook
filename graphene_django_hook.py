import argparse
import inspect
import os
import pathlib
import re
import shlex
import subprocess
import sys
from typing import Optional
from typing import Sequence
from typing import Set
from importlib import import_module
from itertools import count


def run_command(command: str) -> int:
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    try:
        outs, errs = process.communicate(timeout=30)
        if outs:
            print(outs.decode('utf8').strip(), file=sys.stdout)
        if errs:
            print(errs, file=sys.stdout)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errs = process.communicate()
        if outs:
            print(outs.decode('utf8').strip(), file=sys.stdout)
        if errs:
            print(errs, file=sys.stdout)
    rc = process.poll()
    return rc


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--python-version', default='3.6')
    parser.add_argument('--settings', default='')
    args = parser.parse_args(argv)
    
    command = 'python{} manage.py graphql_schema'.format(args.python_version)
    
    if args.settings:
        command += ' --settings={}'.format(args.settings)
  
    return run_command(command)
   
 
if __name__ == '__main__':
    exit(main())
