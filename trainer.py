import json
import random

all_preps = '/Users/grigoryshumsky/PycharmProjects/english_trainer/resourses/all_prep.json'
wrong_answers = '/Users/grigoryshumsky/PycharmProjects/english_trainer/resourses/wrong_answers.json'

file = all_preps
recording = False
recorded_dict = {}

if input("Train mistakes? y/n: ") == 'y':
    file = wrong_answers
else:
    if input("Enable recording? y/n: ") == 'y':
        recording = True

with open(file) as source:
    parsed_source = json.load(source)

for string in random.sample(sorted(parsed_source), len(parsed_source)):
    print(string)
    if input('enter preposition: ') == parsed_source[string]:
        print('Correct! Good!')
        input()
    else:
        print(f'Unfortunately, incorrect.The correct prep is "{parsed_source[string]}"')
        input()
        recorded_dict[string] = parsed_source[string]
if recording:
    with open(wrong_answers, 'w') as recorded_json:
        json.dump(recorded_dict, recorded_json)
