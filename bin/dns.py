#!/usr/bin/env python

import argparse
import sys

from dns.lookup import query_and_print_all

def dns():
    parser = argparse.ArgumentParser(description='dns records lookup')
    parser.add_argument('domain', type=str, help='domain name')
    args = parser.parse_args()
    try:
        query_and_print_all(args.domain)
    except ValueError as e:
        print('error:', e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    dns()
