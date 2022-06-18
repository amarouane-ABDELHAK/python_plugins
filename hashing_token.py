"""
Files
"""
from datetime import datetime
import os

def hash_them():
    """Hash the file_name"""
    now = datetime.now()
    captured_time = 60
    for ele in range(0,60, 15):
        if now.minute<ele:
            captured_time = ele
            break
    return f"{now.day}-{now.hour}-{captured_time}"




def create_temp_file():
    """
    cecev
    """
    get_file_name = hash_them()
    token = ""
    tempfile = f'/tmp/{get_file_name}'
    
    if not os.path.isfile(tempfile):

        with open(tempfile, 'w', encoding='utf-8') as f_:
            token = tempfile
            f_.write(token)
        return token
    with open(tempfile, 'r', encoding='utf-8') as f_:
        token = f_.readline()
    return token

f = create_temp_file()
print(f)

