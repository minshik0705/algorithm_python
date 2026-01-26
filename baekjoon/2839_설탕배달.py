def solve():
    import sys
    n = int(sys.stdin.readline().strip())

    five = n // 5
    while five >= 0:
        rest = n - 5 * five
        if rest % 3 == 0:
            three = rest // 3
            print(five + three)
            return
        five -= 1
    print(-1)

if __name__ == "__main__":
    solve()