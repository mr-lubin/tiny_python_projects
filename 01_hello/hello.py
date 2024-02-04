#!/usr/bin/env python3
"""
Author: Lubini
Purpose: Say hello
"""

import argparse

def main():
    """Play despacito"""
    args = get_args()
    print(f'Hello, {args.name}!')

def get_args():
    """Get and parse command line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()

if __name__ == '__main__':
    main()
