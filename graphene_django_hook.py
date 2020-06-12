import argparse
import shlex
import subprocess
import sys
from typing import Optional
from typing import Sequence


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


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--indent', default=None)
    parser.add_argument('--out', default=None)
    parser.add_argument('--schema', default=None)
    parser.add_argument('-v', '--verbosity', default=None)
    parser.add_argument('--managepy-path', default='manage.py')
    parser.add_argument('--settings', default=None)
    args = parser.parse_args(argv)
    
    command = './{} graphql_schema'.format(args.managepy_path)
    
    if args.settings is not None:
        command += ' --settings={}'.format(args.settings)

    if args.indent is not None:
        command += ' --indent={}'.format(args.indent)

    if args.out is not None:
        command += ' --out={}'.format(args.out)

    if args.indent is not None:
        command += ' --schema={}'.format(args.schema)

    if args.verbosity is not None:
        command += ' --verbosity={}'.format(args.verbosity)
    
    command = 'chmod +x {} && {}'.format(args.managepy_path, command)
    return run_command(command)
   
 
if __name__ == '__main__':
    exit(main())
