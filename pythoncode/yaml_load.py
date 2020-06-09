# -*- coding: utf-8 -*-
import yaml

print(yaml.load(open("homework2.yml", encoding='utf-8'), Loader=yaml.FullLoader))
