import networkx as nx
import random 

def jrcs_tps(G, s):
    stack = []
    visited = set()
    _sigma = ""
    stack_len = 0

    visited, stack, _sigma, stack_len  = \
    jrcs_tps_visit(s, G, visited, stack, _sigma)

    _sigma = _sigma[::-1]
    print(_sigma)
    return _sigma


def jrcs_tps_visit(v, G, visited, stack, _sigma, last_n=None):
    if last_n is None or len(stack) != last_n:
        last_n = len(stack)
        stack_printer = '\033[34m'
        for u in stack:
            stack_printer += str(u)
        stack_printer += '\033[0m'
        print(stack_printer)

    stack_printer = '<' + str(v) + '>'

    if v in stack:
        return visited, stack, _sigma, last_n

    if v not in visited:
        stack.insert(0, v)
        for w in G.successors(v):
            if w in visited:
                stack_printer += str('\033[31m' + str(w))
            elif w in stack:
                stack_printer += str('\033[32m' + str(w))
            else:
                stack_printer += str('\033[33m' + str(w))
            stack_printer += '\033[0m'
            visited, stack, _sigma, last_n = jrcs_tps_visit(w, G, visited, stack, _sigma, last_n)
        visited.add(v)
        print(stack_printer)

        _sigma += str(v)
        stack.remove(v)

    return visited, stack, _sigma, last_n


def dag_from_string(string):
    #Bard wrote this
    
    digraph = nx.DiGraph()

    for i in range(1, len(string)):
        digraph.add_edge(string[i - 1], string[i])
        for _ in range(random.randint(0, 10)):
            digraph.add_edge(string[i - 1], random.choice(string))
    
    return digraph



if __name__=="__main__":
    the_iroha = "いろはにほへとちりぬるをわかよたれそつねならむうゐのおくやまけふこえてあさきゆめみしゑひもせす"
    eng_htrgrm = "thebigdwarfonlyjumps"
    jrcs_tps(dag_from_string(eng_htrgrm), 't')
    jrcs_tps(dag_from_string(the_iroha), 'い')