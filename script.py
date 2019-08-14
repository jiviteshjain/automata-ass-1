from automaton import NFA
from utils import BitString

import json
import sys


        


# READ input.json AND POPULATE nfa_dict
try:
    with open('input.json') as f:
        nfa_dict = json.load(f)
except IOError:
    print('ERROR: Could not find the file input.json. Make sure it\'s kept somewhere close by.')
    sys.exit()

nfa = NFA(nfa_dict)
print(nfa)


