import sys
if len(sys.argv) != 3:
    print('usage: cp source_file target_file')
    sys.exit()
source_file, copy_file = sys.argv[1], sys.argv[2]
with open(source_file, 'rb') as original_f, open(copy_file, 'wb') as copy_f:
    for line in original_f:
        copy_f.write(line)