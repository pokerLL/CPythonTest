import getpass

prompt = "Please enter your password: "

user = getpass.getuser()		# 自动从环境中获取用户名
passwd1 = getpass.getpass(prompt=prompt)
passwd2 = getpass.getpass(prompt=prompt)

if passwd1 == passwd2:
   print('Yay!')
else:
   print('Boom!')

"""
Please enter your password: 
Please enter your password: 
Yay!
"""
