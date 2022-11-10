def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split('\n')
    ans = len(data[0])
    print(data)
    for i in data:
        
        if ans < len(i):
            ans = len(i)
    return ans
f = open('txt_file/data10.txt').read()
print(main(f))

# Read data from file