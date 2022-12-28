def calc_salt(massa):
    return int(massa) / 10

try:
    print(calc_salt(2000))
    print(calc_salt('2000'))
    print(calc_salt('abc'))
except ValueError as m:
    print(m)
    print(0.0)
