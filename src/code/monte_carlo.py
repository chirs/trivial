
# Determine the point probabilities using monte carlo simulation.

import random
from collections import defaultdict

POINT_VALUES = [0,1,1,2,2,3]


def get_distribution(choose, lst, times=1000):

    d = defaultdict(int)

    for e in range(times):
        r = random.sample(lst, choose)
        d[sum(r)] += 1

    return sorted(d.items())


def simulate_match(correct1, correct2):
    p1 = random.sample(POINT_VALUES, correct1)
    p2 = random.sample(POINT_VALUES, correct2)

    if p1 > p2:
        return 2
    elif p1 == p2:
        return 1
    else:
        return 0


def expected_points(correct1, correct2, samples=10000):
    l = []
    for e in range(samples):
        p = simulate_match(correct1, correct2)
        l.append(p)

    return sum(l) / float(len(l))
    


def main():
    for e in range(0, 6):
        print(get_distribution(e, POINT_VALUES, 100000))
    return None


if __name__ == "__main__":
    main()
    

    
