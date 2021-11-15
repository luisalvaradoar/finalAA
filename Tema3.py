def min_abs(arr):
    arr.sort()
    res = []
    
    _min = float('inf')
    for i in range(len(arr) - 1):
        _abs = abs(arr[i + 1] - arr[i])
        if _abs < _min:
            _min = _abs
            res = []
        if _abs == _min:
            res.append([arr[i], arr[i + 1]])
    
    return abs(res[0][0] - res[0][1])
