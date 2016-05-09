import os.path
import json
import random


def get_gifts_from_json(json_file):
    """ get list of gifts from json """
    if os.path.isfile(json_file):
        gifts = []
        with open(json_file) as data_file:
            content = json.load(data_file)
            gifts = content['gifts'] if 'gifts' in content else []
    return gifts


def get_random_gift(gifts):
    """ get random gift from list """
    return random.choice(gifts)
