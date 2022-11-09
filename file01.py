def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for i in data:
        i = int(i)
        ans.append(i)    
    return ans
f = open('txt_file/data01.txt').read().split(',')
print(main(f))

