from slowapi import Limiter
from slowapi.util import get_remote_address

# Configure the rate limiter to use the client's IP address
limiter = Limiter(key_func=get_remote_address)