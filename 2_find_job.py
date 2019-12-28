import sys
def main():
    lines = sys.stdin.readlines()
    lines = [l.strip().split() for l in lines if l.strip()]
    n, m = int(lines[0][0]), int(lines[0][1])
    res = [0] * (n + m)
    abilities = list(map(int, lines[-1]))
    maps = dict()
    for index, l in enumerate(lines[1:-1]):
        d, s = int(l[0]), int(l[1])
        maps[d] = s
        res[index] = d
    for index, ability in enumerate(abilities):
        res[index + n] = ability
        if ability not in maps:
            maps[ability] = 0
    res.sort()
    maxSalary = 0
    for index in range(n + m):
        maxSalary = max(maxSalary, maps[res[index]])
        maps[res[index]] = maxSalary
    for index in range(m):
        print(maps[abilities[index]])
if __name__ == '__main__':
    main()