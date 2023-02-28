import traceback

print('========================================a===========================================')
try:
    print('a123')
    c1
except Exception as e:
    traceback.print_exc()  # 打印try语句中出现的异常
    print('a456')
print('a789')

print('========================================b===========================================')
try:
    print('b123')
    c1
except Exception as e:
    try:
        print('b456')
        c2
    except Exception as e:
        print('b789')
    print('b012')

print('=======================================c============================================')
try:
    print('c123')
    try:
        print('c456')
        c2
    except Exception as e:
        print('c789')
    print('c345')
except Exception as e:
    print('c012')

print('=======================================d============================================')
try:
    print('d123')
    c1
except Exception as e:
    try:
        print('d456')
        c2
    except Exception as e:
        print('d789')
    print('d012')
    print(e)  # 这里会报错

print('=======================================e============================================')
try:
    print('e123')
    c1
except Exception as e:
    try:
        print('e456')
        c2
    except Exception as e:
        print('e789')
        print(e)
    print('e012')