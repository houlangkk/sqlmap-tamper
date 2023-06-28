#!/usr/bin/env python

import re
from urllib import parse

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    return parse.quote('{"id":"'+payload+'"}') if payload else payload
