def alpha_beta(node, a, b, max_player):

    if not isinstance(node, list):
        return node

    if max_player:
        value = float('-inf')
        for child in node:
            value = max(value, alpha_beta(child, a, b, False))
            a = max(a, value)
            if a >= b:
                print("Pruning at MAX")
                break
    else:
        value = float('inf')
        for child in node:
            value = min(value, alpha_beta(child, a, b, True))
            b = min(b, value)
            if a >= b:
                print("Pruning at MIN")
                break
    return value

print("Enter game tree:")
tree = eval(input())
result = alpha_beta(tree, float('-inf'), float('inf'), True)
print("Optimal Game Value =", result)
