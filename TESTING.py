import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def final_id():
    ID1 = id_generator(4, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ID2 = random.randint(10000,99999)
    return f"{ID1}-{ID2}"

final_id()
