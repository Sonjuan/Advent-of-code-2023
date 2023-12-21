from collections import defaultdict, deque
file = open(0).read().splitlines()

adj = defaultdict(list)
state = defaultdict(list)
ttype = defaultdict(str)
pulses = [0, 0]

for line in file :
    left, right = line.split(' -> ')
    right = right.split(', ')

    t, start = left[0], left[1:]
    ttype[start] = t
    for v in right :
        adj[start].append(v)
        state[v].append((start,0))

for k,t in ttype.items() :
    if t == '%' :
        state[k] = [0]

# print(adj)
# print(state)
# print(ttype)

q = deque() 

for i in range (1000) :
    q.append(('roadcaster', 0))
    pulses[0] += 1
    while q :
        u, pulse = q.popleft()
        
        if ttype[u] == '&' :
            for tup in state[u] :
                if tup[-1] == 0 :
                    pulse = 1
                    break
            else :
                pulse = 0

        for v in adj[u] :
            pulses[pulse] += 1
            print(u, pulse)

            if ttype[v] == '%' :
                if pulse == 1 :
                    continue
                state[v][0] = 1 - state[v][0]  # invert state
                q.append((v, state[v][0]))
            
            if ttype[v] == '&' :
                for tup in state[v] :
                    if tup[0] == u :
                        newtup = (u, pulse)
                        state[v].remove(tup)
                        state[v].append(newtup)
                        break
                q.append((v, pulse))

# print(pulses)
print(pulses[0] * pulses[1])