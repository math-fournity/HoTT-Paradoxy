import os

print("Files in /mnt/data:")
if os.path.exists('/mnt/data'):
    for f in os.listdir('/mnt/data'):
        print(f)
else:
    print("/mnt/data does not exist.")

print("\nFiles in current dir:", os.getcwd())
for f in os.listdir('.'):
    print(f)
