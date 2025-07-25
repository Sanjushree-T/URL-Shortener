import random
import string
from models import Urls

def shorten_url():
    letters = string.ascii_letters
    while True:
        rand_letters = ''.join(random.choices(letters, k=3))
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters
