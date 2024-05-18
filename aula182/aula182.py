# secrets gera números aleatorios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=8)))

random = secrets.SystemRandom()

random_ = random.randint(10, 30)
print(random_)
# print(secrets.randbelow(100))
# print(secrets.choice([10]))
