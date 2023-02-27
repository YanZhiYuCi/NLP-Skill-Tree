try:
    print('123')
    c1
except Exception as e:
    print('456')
print('789')

print('===================================================================================')
try:
    print('123')
    c1
except Exception as e:
    try:
        print('456')
        c2
    except Exception as e:
        print('789')
    print('012')

print('===================================================================================')
try:
    print('123')
    try:
        print('456')
        c2
    except Exception as e:
        print('789')
    print('345')
except Exception as e:
    print('012')

print('===================================================================================')
try:
    print('123')
    c1
except Exception as e:
    try:
        print('456')
        c2
    except Exception as e:
        print('789')
    print('012')
    print(e)

try:
    print('123')
    c1
except Exception as e:
    try:
        print('456')
        c2
    except Exception as e:
        print('789')
        print(e)
    print('012')