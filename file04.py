def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for line in data:
        if line.isdigit():
            ans += []
        else:
            ans += line
f = open('txt_file/data04.txt').read()
print(main(f))
# Read data from file