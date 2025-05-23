#!/usr/bin/python3
import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_pagination

# Try to iterate through the paginated results and print users
try:
    for page in lazy_paginator(100):  # Fetch 100 users per page
        for user in page:             # Iterate over each user in the current page
            print(user)
except BrokenPipeError:
    sys.stderr.close()  # Gracefully handle a broken pipe if piping to commands like `head`
