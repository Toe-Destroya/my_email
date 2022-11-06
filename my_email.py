import yagmail
import sys
#custom email creator

print('Congratulations on getting hired at ToeDestroya industries! We will now create your work email.')
name = input('What is your first name?: ')
namel = input('What is your last name?: ')

print (f"{name + namel}@Toes.com")

user = 'toedestroya@gmail.com'

try:
    with open ('app-pass') as f:
        for num, line in enumerate(f): 
            if num == 0:
                passw = line 
except:
    print ('Add your gmail app password to a file named api"API-key"')
    sys.exit()

password = passw 

to = 'toedestroya@gmail.com'

subject = 'Email Creation'
content = (f'Dev Team, please create and email account for {name + namel}@toe.com' )
    
with yagmail.SMTP(user, password) as yag:
    yag.send(to, subject, content)
    print('sent')
