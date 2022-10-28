def is_leap(year):
    leap = False
    if year in range(1990,100000):
        if year/4 == year//4:
            if year/100 == year // 100:
                print(year/100 and year//100)
                
                if year/400 == year// 400:
                    return True
                else:
                    return leap
            else:
                 return leap   
        else:
            return leap                 
    else:
        print('Try again')
        
year = int(input())
print(is_leap(year))
