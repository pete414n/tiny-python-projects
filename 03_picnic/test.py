#!/usr/bin/env python3

import os
from subprocess import getstatusoutput, getoutput

prg = './picnic.py'

def test_exists():
    """exists"""

    assert os.path.isfile(prg)

def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

def test_one():
    """one item"""

    out = getoutput(f'{prg} chips')
    assert out.strip() == 'You are bringing chips.'

def test_two():
    """two items"""

    out = getoutput(f'{prg} salad chips')
    assert out.strip() == 'You are bringing salad and chips.'

def test_three():
    """three items"""

    out = getoutput(f'{prg} salad chips cupcakes')
    assert out.strip() == 'You are bringing salad, chips, and cupcakes.'

def sorted():
    """three sorted items"""

    out = getoutput(f'{prg} salad chips cupcakes')
    assert out.strip() == 'You are bringing chips, cupcakes, and salad.'