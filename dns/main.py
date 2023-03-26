#!/usr/bin/env python

import argparse
import sys
from .dns import dns

def main():
    parser = argparse.ArgumentParser(description='dns records lookup')
    parser.add_argument('domain', type=str, help='domain name')
    args = parser.parse_args()
    try:
        dns(args.domain)
    except ValueError as e:
        print('error:', e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
