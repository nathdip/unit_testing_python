def convert_str_to_int(inputString):
    """
    Args:
        inputString: String consisting of numerals only
    Returns:
        int
    """
    inputString = inputString.replace(',', "")
    return int(inputString)


if __name__ == '__main__':
    input = '201,202'
    output = convert_str_to_int(input)
    print(f"The output is {output} and is of type {type(output)}")
