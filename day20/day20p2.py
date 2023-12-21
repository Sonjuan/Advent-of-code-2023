from collections import defaultdict, deque
import math
file = open(0).read().splitlines()

adj = defaultdict(list)
state = defaultdict(list)
ttype = defaultdict(str)

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

(feed, ) = [k for k, outputs in adj.items() if 'rx' in outputs]
print(feed)

cycle_length = {}
seen = {k : 0 for k, outputs in adj.items() if feed in outputs}
print(seen)

q = deque() 
ans = 0
for _ in range(10000000) :
    ans += 1
    q.append(('roadcaster', 0))
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
            if v == feed and pulse == 1 :
                seen[u] += 1
                if u not in cycle_length :
                    cycle_length[u] = ans
                else :
                    assert ans == seen[u] * cycle_length[u]
                if all(seen.values()) :
                    # print(seen)
                    # print(cycle_length)
                    # exit(0)
                    x = 1
                    for cycle_length in cycle_length.values() :
                        x = x * cycle_length // math.gcd(x, cycle_length)
                    print(x)
                    exit(0)


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

