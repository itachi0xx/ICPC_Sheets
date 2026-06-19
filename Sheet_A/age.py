n =  int(input())
years =  n // 365
n %= 365
months = n // 30
n %= 30
days = n
print(f"{years} year(s)\n{months} month(s)\n{days} day(s)")