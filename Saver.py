import json

def save(name, data):
    # now write output to a file
    savefile = open(name+".PSLT-SAV", "w+")
    savefile.write(json.dumps(data))
    savefile.close()

def load(name):
    loadfile = open(name + ".PSLT-SAV", "r+")
    data = json.load(loadfile)
    loadfile.close()
    return data
