import graphviz
from transitions import MachineError
from transitions.extensions import GraphMachine

states = [
    'P',
    'Q',
    'R',
    'S',
    'T',
]

transitions_list = [
    {'trigger': 'a', 'source': 'P', 'dest': 'Q'},

    {'trigger': 'a', 'source': 'Q', 'dest': 'R'},
    {'trigger': 'b', 'source': 'Q', 'dest': 'S'},
    {'trigger': 'c', 'source': 'Q', 'dest': 'T'},

    {'trigger': 'b', 'source': 'R', 'dest': 'Q'},
    {'trigger': 'c', 'source': 'S', 'dest': 'Q'},
]


# Simulate regex a((ab)|(bc))*c
class DFA(GraphMachine):
    def __init__(self):
        super(DFA, self).__init__(states=states, transitions=transitions_list, initial='S', auto_transitions=False, graph_engine='graphviz')

    def accepts(self, input_string):
        """
        Attempt to consume the input_string symbol by symbol.
        Return True if we end in W, False otherwise.
        """
        # Start state
        self.set_state('P')

        for symbol in input_string:
            if symbol not in ['a', 'b', 'c']:
                return False
            try:
                self.trigger(symbol)
            except MachineError:
                return False

        # End state
        return self.state == 'T'


if __name__ == "__main__":
    dfa = DFA()
    dfa.get_graph().draw('dfa_transitions.png', prog='dot')
