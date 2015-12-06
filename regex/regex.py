import re

s = '010-52482114'
pattern = r'^\d{3}\-\d{3,8}$'
result = re.match(pattern, s)
print(result)

result = re.match(pattern, 'hello')
print(result)

p2 = r'^[a-zA-Z\_][0-9a-zA-Z\_]+'
s1 = 'q_zxin'
s2 = '12a'
s3 = '_a2'

result = re.match(p2, s1)
print(p2, '匹配',s1,'  =》 ',result)

result = re.match(p2, s2)
print(p2, '匹配',s2,'  =》 ',result)

result = re.match(p2, s3)
print(p2, '匹配',s3,'  =》 ',result)

p3 = r'py'
p4 = r'p|Py$'

s4 = 'python'
s5 = 'Python'
s6 = 'py'
result = re.match(p4, s4)
print(p3, '匹配',s4,'  =》 ',result)

result = re.match(p4, s5)
print(p3, '匹配',s5,'  =》 ',result)

result = re.match(p4, s5)
print(p4, s6, result)

s7 = 'hello world   haha,,, hi tt'
print(re.split(r'[\s\,]+', s7))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-8456321')
print(m.group(0))
print(m.group(1))
print(m.group(2))

Email = re.compile(r'^([a-zA-Z\-][0-9a-zA-Z\_]*)\@([0-9a-zA-Z\_]+)\.com')
m = Email.match('quinn@163.com')
m = Email.match('quinn@163.com')
m = Email.match('qzxin365@gmail.com')
print(m.group(1))
print(m.group(2))


