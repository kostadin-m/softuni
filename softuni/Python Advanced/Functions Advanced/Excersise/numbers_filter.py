def even_odd_filter(**kwargs):
    filtered = {}
    sorted_nums = sorted(kwargs.items(), key=lambda kvpt :(-len(kvpt[1]), kvpt[1]))
    
    for pair in sorted_nums:
        parity = 0 if pair[0] == 'even' else 1
        filtered[pair[0]] = [int(x) for x in pair[1] if x % 2 == parity]
    
    return filtered