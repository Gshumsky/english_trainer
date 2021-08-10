import json
import random

with open('/Users/grigoryshumsky/PycharmProjects/english_trainer/resourses/all_prep.json') as source:
    parsed_source = json.load(source)
for string in random.sample(sorted(parsed_source), len(parsed_source)):
    print(string)
    if input('enter preposition: ') == parsed_source[string]:
        print('Correct! Good!')
        input()
    else:
        print(f'Unfortunately, incorrect.The correct prep is "{parsed_source[string]}"')
        input()
