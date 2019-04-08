from app import db
from app.model import User

print('Admin setup:')

username = str(input('Username: '))
password = str(input('Password: '))
password_confirmation = str(input('Password (repeat): '))

if (password == '') or (password != password_confirmation):
    print('Passwords don\'t match or no password entered. Run setup again')
    quit()

u = User(username=username, admin=True)
u.set_password(password)

db.session.add(u)
db.session.commit()

print('Admin user created')
