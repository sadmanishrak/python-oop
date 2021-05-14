# Static method example

class Math:
    # this is a static method
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        return("run")

print(Math.add5(5))
print(Math.pr())
