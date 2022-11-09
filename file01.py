def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = data.split(',')
    ans = []
    for i in data:
        ans.append(int(i))    
    return ans
f = open('txt_file/data01.txt').read()
print(main(f))

