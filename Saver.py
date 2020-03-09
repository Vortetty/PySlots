import shelve, pickle

def save(name, money, rolls):
    File = shelve.open(name + ".PSLT-SAV")
    File["money"] = money
    File["rolls"] = rolls
    File.close()

def load(name):
    File = shelve.open(name + ".PSLT-SAV")
    money = File["money"]
    rolls = File["rolls"]
    File.close()
    return money,rolls
