def run():
    col = int(input('Init_column: '))
    row = int(input('Init_row: '))
    f_col = int(input('Final_column: '))
    f_row = int(input('Final_row: '))

    if col == f_col or row == f_row or abs(col - f_col) == abs(row - f_row):
        print ("YES")
    else:
        print ("NO")

if __name__ == '__main__':
    run()