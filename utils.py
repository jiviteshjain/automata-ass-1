from automaton import DFA, NFA

class BitString:
    def __init__(self, size, initial=0):
        self.size = size
        self.data = [0 for i in range(self.size)]
        if initial < 0:
            raise ValueError
        elif initial > 0:
            self.set_num(initial)

    def set_bit(self, pos, val):
        if pos >= self.size or val not in (0, 1):
            raise ValueError
        pos = self.size - pos - 1
        self.data[pos] = val

    def get_bit(self, pos):
        if pos >= self.size:
            raise ValueError
        pos = self.size - pos - 1
        return self.data[pos]

    def get_num(self):
        s = ''.join(map(str, self.data))
        return int(s, 2)

    def set_num(self, num):
        if num >= pow(2, self.size) or num < 0:
            raise ValueError
        s = bin(num).split('b')[1]
        s = ('0' * (self.size - len(s))) + s
        self.data = [int(i) for i in s]


def nfa_to_dfa(nfa):
    dfa = DFA()
    dfa.states = pow(2, nfa.states)
    dfa.letters = nfa.letters
    dfa.start = [nfa.start, ]

    trans = []
    for dfa_state in range(dfa.states):
        for a in dfa.letters:
            bits = BitString(nfa.states, dfa_state)
            in_list = []
            out_set = set()
            for i in range(nfa.states):
                if bits.get_bit(i) == 1:
                    in_list.append(i)
                    if (i, a) in nfa.trans:
                        out_set = out_set | nfa.trans[(i, a)]
            trans.append([list(in_list), a, list(out_set)])

    dfa.trans = trans

    nfa_final = set(nfa.final)  # for fast membership testing
    final = []
    for dfa_state in range(dfa.states):
        bits = BitString(nfa.states, dfa_state)
        append = False
        state_list = []
        for i in range(nfa.states):
            if bits.get_bit(i) == 1:
                state_list.append(i)
                if i in nfa_final:
                    append = True
        if append:
            final.append(state_list)

    
    dfa.final = final

    return dfa
