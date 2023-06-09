



class BranchAndBound:
    def __init__(self, W: int, m: int, w: 'list[int]', v: 'list[int]', c: 'list[int]') -> None:
        self.W = W
        self.m = m
        self.w = w
        self.v = v
        self.c = c
        self.n = len(w)
        self.best_value = 0
        self.best_items = []
        self.memo = {}

    def bound(self, k: int, weight: int, value: int, taken: 'list[bool]') -> float:
        if (k, weight) in self.memo:
            return self.memo[(k, weight)]

        if weight >= self.W:
            return 0

        remaining_classes = set(self.c[k:])
        for i in range(k, self.n):
            if self.c[i] in remaining_classes:
                remaining_classes.remove(self.c[i])
                weight += self.w[i]
                value += self.v[i]
                taken[i] = True

        for i in range(k, self.n):
            if not taken[i] and self.c[i] not in remaining_classes:
                frac = min(1, (self.W - weight) / self.w[i])
                weight += frac * self.w[i]
                value += frac * self.v[i]

        self.memo[(k, weight)] = value
        return value

    def knapsack(self, k: int, weight: int, value: int, taken: 'list[bool]'):
        if weight <= self.W and value > self.best_value:
            self.best_value = value
            self.best_items = taken[:]
        if k == self.n:
            return
        
        sorted_items = sorted([(i, self.v[i]/self.w[i]) for i in range(k, self.n)], key=lambda x: -x[1])
        for i, _ in sorted_items:
            if weight + self.w[i] <= self.W:
                taken[i] = True
                self.knapsack(i + 1, weight + self.w[i], value + self.v[i], taken)
                taken[i] = False

            if self.bound(i + 1, weight, value, taken) > self.best_value:
                taken[i] = False
                self.knapsack(i + 1, weight, value, taken)

    def solve(self) -> 'tuple[int, list[int]]':
        taken = [False] * self.n
        self.knapsack(0, 0, 0, taken)
        return str(self.best_value), ', '.join([str(int(i)) for i in self.best_items])

# test_seq = 2
# def write_result(seq: int, value: str, state: str):
#     with open(f"OUTPUT_{seq}.txt", 'w') as f:
#         f.write(value + '\n' + state)
#         print("Write file successfully!")

# with open(f"INPUT_{test_seq}.txt") as f:
#     lines = f.readlines() 
#     W = int(lines[0])
#     m = int(lines[1])
#     w = [int(l) for l in lines[2].strip().split(', ')]
#     v = [int(l) for l in lines[3].strip().split(', ')]
#     c = [int(l) for l in lines[4].strip().split(', ')]
def solve(x):
    with open(f"INPUT_{x}.txt","r") as file:
        lines = file.readlines()

    capacity = int(lines[0])
    numberOfClass = int(lines[1])

    inp = lines[2].split()
    weights = [int(num) for num in inp]

    inp = lines[3].split()
    values = [int(num) for num in inp]

    inp = lines[4].split()
    item_class = [int(num) for num in inp]
    bb = BranchAndBound(capacity, numberOfClass, weights, values, item_class)
    value, state = bb.solve()
    print("Solution: ", state)
    print("value: ", value)
    with open(f"OUTPUT_{x}.txt","w") as file:
        file.write(str(value) + '\n' + str(state))
#write_result(2, value, state)