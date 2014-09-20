import yaml
import os.path


def read_yaml(filename):
    if not os.path.isfile(filename):
        print 'not file'
        return {}

    doc = {}

    with open(filename, 'r') as f:
        doc = yaml.load(f)

    return doc
