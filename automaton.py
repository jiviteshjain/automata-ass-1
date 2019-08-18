class NFA:
    def __init__(self, nfa_dict):
        self.states = int(nfa_dict['states'])
        self.letters = list(nfa_dict['letters'])  # Ensure deep copies
        self.start = int(nfa_dict['start'])
        self.final = list(nfa_dict['final'])
        self.trans = self.make_trans(nfa_dict['t_func'])

    def make_trans(self, arr):
        # Convert to dictionary for faster random access
        # Keys must be immutable => stored as tuple
        # Values stored as set to help with unions later
        # Format (for each transition):
        #   Key: (state, letter)    [tuple]
        #   Value: {state1, state2, ...}    [set]
        trans = {}
        for triplet in arr:
            trans[tuple(triplet[:2])] = set(triplet[2])
        return trans

class DFA:
    def __init__(self, states=None, letters=None, start=None, final=None, trans=None):
        self.states = states
        self.letters = letters
        self.start = start
        self.final = final
        self.trans = trans

    def to_dict(self):
        return  {
            'states': self.states,
            'letters': self.letters,
            't_func': self.trans,
            'start': self.start,
            'final': self.final,
        }
