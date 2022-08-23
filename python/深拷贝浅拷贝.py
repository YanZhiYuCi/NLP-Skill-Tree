# 当前项目名:machaoyangNLP
# 当前文件名:1 
# 当前集成开发环境:PyCharm	
# 当前用户的登录名:Administrator
# 当前作者:马朝阳
# 当前系统日期:2022/8/23
# 当前系统时间:16:28
a = [1,2,3]
e = a
c = a[:]
d = a[:]
a_id = id(a)
b_id = id(c)
d_id = id(d)
e_id = id(e)
print(a==c)
print(a is c)
b = [a, a]
print(b)
a.append(4)
print(b)