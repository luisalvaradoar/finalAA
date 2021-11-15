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
    
    return res

lista = [1,-1,3,0,8,1,3,4,6,1,11,2,3]
print(abs(min_abs(lista)[0][0] - min_abs(lista)[0][1]))