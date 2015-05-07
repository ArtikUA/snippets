import os
import time
import glob

print(os.getcwd())

print(os.path.split('/pagefile.sys'))

metadata = os.stat('/pagefile.sys')
print(metadata)

to_readable = lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x))

time_created = to_readable(metadata.st_ctime)
time_modified = to_readable(metadata.st_mtime)
time_opened = to_readable(metadata.st_atime)

print("Created: %s" % time_created)
print("Modified: %s" % time_modified)
print("Opened: %s" % time_opened)

print([(os.path.realpath(f), to_readable(os.stat(f).st_ctime)) for f in glob.glob('*.py') if os.stat(f).st_size > 500])
