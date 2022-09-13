def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda kvpt :(-len(kvpt[1]), kvpt[1]))
    result = ''
    for cheese,quantity in sorted_cheese:
        quantity = sorted(quantity, reverse=True)
        result += (cheese + "\n") + ('\n'.join([str(x) for x in quantity]) + '\n')
    return result

