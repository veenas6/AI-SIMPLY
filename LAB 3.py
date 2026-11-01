def hanoi(n, src, aux, dst):
    if n == 1:
        print("Move disk 1 from", src, "to", dst)
        return
    hanoi(n-1, src, dst, aux)
    print("Move disk", n, "from", src, "to", dst)
    hanoi(n-1, aux, src, dst)

n = int(input("Enter number of disks: "))
print("Tower of Hanoi")
hanoi(n, "Source", "Auxiliary", "Destination")
print("Total Moves:", 2**n - 1)
