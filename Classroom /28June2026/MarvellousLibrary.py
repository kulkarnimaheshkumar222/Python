def filterX(task, elements):
    result = list()

    for element in elements:
        value = task(element) 
        if value:
            result.append(element)
    return result

def mapX(task,elements):
    result = list()

    for element in elements:
        value = task(element) 
        result.append(value)
    return result

def reduceX(task, elements):
    result = 0

    for element in elements:
        result = task(result, element)
    return result