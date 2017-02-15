def nestEggFixed(salary, save, growthRate, years):
    cashFlow = []
    if years == 0:
        return cashFlow
    f = salary * save * 0.01
    cashFlow.append(f)
    for i in range(1, int(years)):
        f = f * (1 + 0.01 * growthRate) + salary * save * 0.01
        cashFlow.append(f)
    return cashFlow


def testNestEggFixed():
    print nestEggFixed(1000, 10, 5, 3)
    print nestEggFixed(1000, 10, 5, 0)
    print nestEggFixed(1000, 10, 5, 1)


def nestEggVariable(salary, save, growthRates):
    cashFlow = []
    if len(growthRates) == 0:
        return cashFlow
    f = salary * save * 0.01
    cashFlow.append(f)
    for i in range(1, len(growthRates)):
        f = f * (1 + 0.01 * growthRates[i]) + salary * save * 0.01
        cashFlow.append(f)
    return cashFlow


def testNestEggVariable():
    print nestEggVariable(1000, 10, [])
    print nestEggVariable(1000, 10, [5])
    print nestEggVariable(1000, 10, [5, 5, 5])
    print nestEggVariable(1000, 10, [1, 3, 5])


# testNestEggVariable()


def postRetirement(savings, growthRates, expenses):
    cashFlow = []
    f = savings * (1 + 0.01 * growthRates[0]) - expenses
    cashFlow.append(f)
    for i in range(1, len(growthRates)):
        f = f * (1 + 0.01 * growthRates[i]) - expenses
        cashFlow.append(f)
    return cashFlow


def testPostRetirement():
    print postRetirement(10000, [0, 0, 0, 0, 0], 2000)
    print postRetirement(10000, [5, 5, 5, 5, 5], 2000)
    print postRetirement(10000, [1], 200)
    print postRetirement(10000, [1, 3, 5], 300)
    print postRetirement(20000, [1, 1, 1, 1, 1, 1, 1, 1], 2500)


# testPostRetirement()


def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
    if len(preRetireGrowthRates) == 0:
        return "No savings"
    savings = salary * save * 0.01
    for i in range(1, len(preRetireGrowthRates)):
        savings = savings * (1 + 0.01 * preRetireGrowthRates[i]) + salary * save * 0.01

    bal = savings
    high = savings
    low = 0
    while abs(bal) > epsilon:  # abs(negative bal) > epsilon?
        expenses = low + (high - low) / 2.0
        bal = savings * (1 + 0.01 * postRetireGrowthRates[0]) - expenses
        for i in range(1, len(postRetireGrowthRates)):
            bal = bal * (1 + 0.01 * postRetireGrowthRates[i]) - expenses
        if bal < 0:
            high = expenses
        elif bal > 0:
            low = expenses
        else:
            return expenses
    return expenses


def testFindMaxExpenses():
    salary = 1000
    save = 10
    preRetireGrowthRates = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.


testFindMaxExpenses()
