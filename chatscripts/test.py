import yfscript

def objToStr(obj):
    string = ""
    for key in obj:
        string+= key + ": " + obj[key] + '\n'
    return string

print(objToStr(yfscript.get_ticker_data('AAPL')))
