def get_num_words(content):
    return len(content.split())

def count_chars(content):
    allchars = {}
    for i in content:
        if i.lower() not in allchars:
            allchars[i.lower()] =1
        else:
            if i.lower() in allchars:
                allchars[i.lower()] += 1
    return allchars

def sortdict(dictionary):
    final_arr = []
    for key in dictionary:
        allcounts = dict()
        allcounts["key"] = key
        #print(f'getting dictionary[key] to value: {key} : {dictionary[key]} ')
        allcounts["val"]=dictionary[key]
        final_arr.append(allcounts)
    final_arr.sort(reverse=True, key=sort_on)
    return final_arr

def sort_on(dict):
    return dict["val"]
        