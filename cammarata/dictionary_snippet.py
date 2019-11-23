import os

# print(os.__dict__)

# help(os.path)

os_dict = os.__dict__

for k, v in os_dict.items():
    print(k)
