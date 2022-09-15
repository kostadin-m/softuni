from collections import deque

def math_operations(*args, **kwargs):
    nums = deque(args)
    result = ''
    while nums:
        kwargs['a'] += nums.popleft() 
        if not nums:
            break
        kwargs['s'] -= nums.popleft()
        if not nums:
            break
        divisor = nums.popleft()
        if divisor != 0:
            kwargs['d'] /= divisor
        if not nums:
            break
        kwargs['m'] *= nums.popleft()
    
    for key,value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result += f'{key}: {value:.1f}\n'
    return result
