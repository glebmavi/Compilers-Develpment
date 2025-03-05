from transitions import MachineError
from transitions.extensions import GraphMachine


states = [
    'S',
    'O',
    'U',
    'T',
    'V',
    'W',
]

transitions_list = [
    {'trigger': 'a', 'source': 'S', 'dest': 'O'},
    {'trigger': 'b', 'source': 'S', 'dest': 'T'},
    {'trigger': 'c', 'source': 'S', 'dest': 'O'},

    {'trigger': 'a', 'source': 'O', 'dest': 'S'},
    {'trigger': 'b', 'source': 'O', 'dest': 'U'},
    {'trigger': 'c', 'source': 'O', 'dest': 'S'},

    {'trigger': 'a', 'source': 'U', 'dest': 'O'},
    {'trigger': 'b', 'source': 'U', 'dest': 'W'},
    {'trigger': 'c', 'source': 'U', 'dest': 'O'},

    {'trigger': 'a', 'source': 'T', 'dest': 'S'},
    {'trigger': 'b', 'source': 'T', 'dest': 'V'},
    {'trigger': 'c', 'source': 'T', 'dest': 'S'},

    {'trigger': 'a', 'source': 'V', 'dest': 'W'},
    {'trigger': 'b', 'source': 'V', 'dest': 'W'},
    {'trigger': 'c', 'source': 'V', 'dest': 'W'},

    {'trigger': 'a', 'source': 'W', 'dest': 'V'},
    {'trigger': 'b', 'source': 'W', 'dest': 'V'},
    {'trigger': 'c', 'source': 'W', 'dest': 'V'},
]


class DFA(GraphMachine):
    def __init__(self):
        super(DFA, self).__init__(states=states, transitions=transitions_list, initial='S', auto_transitions=False, graph_engine='graphviz')

    def accepts(self, input_string):
        """
        Attempt to consume the input_string symbol by symbol.
        Return True if we end in W, False otherwise.
        """
        # Reset to the start state (S)
        self.set_state('S')

        for symbol in input_string:
            if symbol not in ['a', 'b', 'c']:
                return False
            try:
                self.trigger(symbol)
            except MachineError:
                return False

        # Accept if (and only if) we end in W
        return self.state == 'W'


if __name__ == "__main__":
    dfa = DFA()
    dfa.get_graph().draw('dfa_transitions.png', prog='dot')
