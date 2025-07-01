def print_formatted(number):

    # without prefix `0o173`
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        # print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].rjust(width)} {bin(i)[2:].rjust(width)}")






number = 17
print_formatted(number)