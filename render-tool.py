#!/usr/bin/env python

import sys
import yaml
from jinja2 import Environment

def render(template, values):
    with open(value, 'r') as f:
        value_obj = yaml.load(f.read())
    with open(template, 'r') as f:
        template_content = f.read()
    render_content = Environment().from_string(file_content.encode('utf-8')).render(value_obj)
    with open(template, 'w') as f:
        f.write(render_content.encode('utf-8'))

if __name__ == '__main__':
    template_file=sys.argv[0]
    value_file=sys.argv[1]
    render(template_file, value_file)
    pirnt "render %s: success!" % template_file
