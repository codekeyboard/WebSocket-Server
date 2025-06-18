def sada():
    print("Sada function called")

def kalla(test):
    print(f"Kalla function called with argument: {test}")

def two_types(test, test2=None):
    print(f"Two types function called with arguments: {test}, {test2}")

def kamai(lagaye=0, aye=0, pehly=0):
    profit = aye + pehly - lagaye
    print(f"Kamai function called with lagaye: {lagaye}, aye: {aye}, pehly: {pehly}. Profit: {profit}")

# print(sada())
# print(kalla(234))
# print(two_types(test=234))


kamai(10, pehly=100)
kamai(10, 100, 20)


def jadugar(*args, **kwargs):
    print(args)
    print(kwargs)

jadugar(11, 22, 1122, nalla=33)