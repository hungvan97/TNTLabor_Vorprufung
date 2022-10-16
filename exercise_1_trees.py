def convert_to_tuple(dict_1):
    tupleDict = {**dict_1}
    
    for key, value in tupleDict.items():
        if type(value) is dict:
            tupleDict[key] = convert_to_tuple(dict_1[key])
        else:
            tupleDict[key] = (value, )
            
    return tupleDict

def mergeBaum(dict_1, dict_2):
    mergeDict = {**dict_1}
    
    for key, value in mergeDict.items():
        if type(value) is dict:
            mergeDict[key] = mergeBaum(dict_1[key], dict_2[key])
        else:
            if key in dict_1 and key in dict_2:
                mergeDict[key] = value + (dict_2[key],)

    return mergeDict

def merge_tree_nodes(*trees):
    merged_tree = trees[0]

    for tree in trees:
        if merged_tree == tree:
            merged_tree = convert_to_tuple(merged_tree)
        else:
            merged_tree = mergeBaum(merged_tree, tree)
            
    return merged_tree
