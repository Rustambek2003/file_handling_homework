def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = data.split()
    ans = []
    for i in data:
        ans.append(len(i))
    return ans
f = open('txt_file/data06.txt').read()
print(main(f))
