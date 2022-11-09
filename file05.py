def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    n,k = 0,0
    for i in data:
        if i.isdigit():
            n += 1
        else:
            k += 1
    ans = [n,k]
    return ans
f = open('txt_file/data05.txt').read()
print(main(f))
# Read data from file