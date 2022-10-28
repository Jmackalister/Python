num_lin = int(input('Number of lines: '))
par = []
for i in range(num_lin):
    par.append(input('line: '))
par = "".join(par)
num_vow = 0
num_cons = 0
for c in par:
    if c in 'aeiouAEIOU':
        num_vow += 1
    elif c in 'bBcBdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ':
        num_cons += 1
print('Number of vowels:', num_vow)
print('Number of consonant:', num_cons)