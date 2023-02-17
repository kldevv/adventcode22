'''
Advent of Code 2022
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
'''

import sys
from collections import defaultdict

def main():
    pf = defaultdict(list)
    degree = {}
    sizes = {}
    cur_dir = ['/']
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        fl = f.readlines()
        i = 0
        while i < len(fl):
            cmds = fl[i].split()
            if cmds[1] == 'cd':
                if cmds[2] == '..':
                    cur_dir.pop()
                elif cmds[2] == '/':
                    cur_dir.clear()
                    cur_dir.append('/')
                else:
                    cur_dir.append(cmds[2])
            elif cmds[1] == 'ls':
                i += 1
                full_res_path = str(cur_dir)
                sizes[full_res_path] = 0
                degree[full_res_path] = 0
                # record file size ---
                while i < len(fl) and fl[i][0] != '$':
                    size, name = fl[i].split()
                    if size == 'dir':
                        degree[full_res_path] += 1
                        pf[str(cur_dir + [name])].append(full_res_path)
                    else:
                        sizes[full_res_path] += int(size)
                    i += 1
                # ------------------
                i -= 1
            i += 1
        
    q = [k for k, v in degree.items() if v == 0]
    for folder in q:
        for parent_folder in pf[folder]:
            sizes[parent_folder] += sizes[folder]
            degree[parent_folder] -= 1
            if degree[parent_folder] == 0:
                q.append(parent_folder)
    
    space_to_free = 30000000 - (70000000 - sizes[str(['/'])])
    out = sizes[str(['/'])]

    for s in sizes.values():
        if s >= space_to_free:
            out = min(out, s)

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{out}\n')

if __name__ == "__main__":
    main()