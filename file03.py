def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for line in data:
        if line.isdigit():
            ans.append(line)
    return ans
f = open('txt_file/data03.txt').read()
print(main(f))


    
# Read data from file