#!/usr/bin/env python3

import yaml
from yamlinclude import YamlIncludeConstructor

YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir='.')

with open('test.yaml') as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:
        print(yaml.dump(doc))
print('\n---')
