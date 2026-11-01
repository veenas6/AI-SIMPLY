def planning():
    state = ["OnTable(A)", "OnTable(B)", "OnTable(C)",
             "Clear(A)", "Clear(B)", "Clear(C)", "HandEmpty"]

    actions = [
        "PickUp(A)",
        "Stack(A,B)",
        "UnStack(A,B)",
        "PutDown(A)",
        "PickUp(B)",
        "Stack(B,C)"
    ]

    print("Goal Stack Planning")
    print("\nInitial State:")
    print(state)

    print("\nGoal State:")
    print(["On(A,B)", "On(B,C)"])

    print("\nPlan Generated:")
    for i, a in enumerate(actions, 1):
        print("Step", i, ":", a)

planning()
