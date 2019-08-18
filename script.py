from automaton import NFA
from utils import BitString, nfa_to_dfa

import json

# READ input.json AND POPULATE nfa_dict
try:
    with open('input.json') as f:
        nfa_dict = json.load(f)
except IOError:
    print('ERROR: Could not find the file input.json. Make sure it\'s kept somewhere close by.')
    exit()

# GET NFA OBJECT AND CONVERT TO DFA
nfa = NFA(nfa_dict)
dfa = nfa_to_dfa(nfa)

# FORMAT OUTPUT AND WRITE
data = dfa.to_dict()
try:
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=2)
except IOError:
    print('ERROR: Could not write to file output.json.\nSo, here\'s the output instead:')
    print(json.dumps(data))


