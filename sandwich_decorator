def addSandwich(myFunc):
    def addSandwichOutside(*args, **kwargs):
        return myFunc(*args, **kwargs) + " sandwich"
    return addSandwichOutside

@addSandwich
def printHam(x = "ham"):
    return x

print(printHam())
