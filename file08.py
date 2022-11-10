def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split()
    ans = 0
    for i in data:
        if i.isdigit() and ans < int(i):
            ans = int(i)
    return ans
f = open('txt_file/data08.txt').read()
print(main(f))
# Read data from file