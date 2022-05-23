def ascii_simbols(num=32, counter=0, rezult=''):
    if num == 128:
        return rezult
    else:
        rezult += f'{num} - {chr(num)} '
        num += 1
        counter += 1
        if counter == 10:
            rezult += '\n'
            counter = 0
        return ascii_simbols(num, counter, rezult)


if __name__ == "__main__":
    print(ascii_simbols())