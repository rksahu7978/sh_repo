def parser():
    import configparser
    conf = configparser.RawConfigParser()
    conf.read("Assets\\Configuration_Data\\Config.properties")
    return conf

def duplicate_removal(arg1):
    no_dup_list = []
    dict1 = {}
    for i in arg1:
        if dict1.get(i):
            continue
        else:
            no_dup_list.append(i)
            dict1[i] = True
    return no_dup_list
