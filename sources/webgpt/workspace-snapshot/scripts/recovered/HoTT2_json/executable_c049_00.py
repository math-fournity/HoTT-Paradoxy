import subprocess

# Let's bypass the path search and directly write to the files using Python, assuming we are inside the data directory structure, or find them globally.
cmd_find = subprocess.run(['find', '/mnt/data', '-name', '*认知闭包*.md'], capture_output=True, text=True)
print("Found closure files:", cmd_find.stdout)

cmd_find_mem = subprocess.run(['find', '/mnt/data', '-name', 'MEMORY.md'], capture_output=True, text=True)
print("Found memory files:", cmd_find_mem.stdout)
