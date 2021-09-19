import os
from dotenv import load_dotenv
load_dotenv()
my_name= input('who tf are you? ')

print(f"hello {os.getenv('name')}")