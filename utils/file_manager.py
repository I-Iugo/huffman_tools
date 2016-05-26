def inputContent(path):
    """
    Purpose: Extract byte content from a file
    Description: Open a file in read and byte mode and return its content
    Param: Path of the file to read
    Return: Content of the file
    """
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def output(compressed, filename):
    """
    Purpose: Write a byte content in a file
    Description: Open file in write and byte mode. Then write each item
    of the compressed text in the file
    Param: Compressed text and name of the file to write in
    Return: filename
    """
    f = open(filename, 'w')
    for item in compressed:
        f.write(item)
    f.close()
    return filename
