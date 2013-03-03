"""
Store paths to scripts and run them from Alfred-2.

paths are stored as tab-separated list in file in
'~/Library/Caches/com.runningwithcrayons.Alfred-2/Workflow Data/ScriptRunner/selection
"""
from alfredlist import AlfredItemsList
import os

# you can customize icons of scripts, to do that put
# png image with the same name as script in direcorty icons_path
icons_path = 'icons/'

extension_interpreter = {
    'py': 'python',
    'rb': 'ruby',
    'pl': 'perl',
    'applescript': 'osascript',
}

dir_path = '~/Library/Caches/com.runningwithcrayons.Alfred-2/Workflow Data/ScriptRunner/'
dir_path = os.path.expanduser(dir_path)
# create directory if it doesn't exist
if not os.path.isdir(dir_path):
    os.mkdir(dir_path)
full_path = dir_path + 'selection'
# create `selection` file if it doesn't exist
try:
    open(full_path, 'r')
except IOError:
    open(full_path, 'w').close()


def change_list(items, change_f):
    # load items from file
    previous = set()
    with open(full_path, 'r') as f:
        text = f.read()
        if text:
            previous = set(text.split('\t'))

    # change items from file using change_f function
    if isinstance(items, str):
        items = set(items.split('\t'))
    new = change_f(previous, items)

    with open(full_path, 'w') as f:
        f.write('\t'.join(new))


def add(items):
    change_list(items, lambda p, i: p.union(i))


def remove(items):
    change_list(items, lambda p, i: p - set(i))


def clear():
    with open(full_path, 'w') as f:
        f.write('')


def xml(arg=''):
    splitted = arg.split(' ')
    path_filter = splitted[0]
    args = ' '.join(splitted[1:])
    items = set()
    with open(full_path, 'r') as f:
        text = f.read()
        if text:
            items = set(text.split('\t'))
    if not items:
        return  # alfred will display "Please wait" subtext

    al = AlfredItemsList()
    # add selected files
    for item in items:
        if path_filter in item:
            al.append(
                arg=interpreter_of_item(item) + ' ' + item + ' ' + args,  # full command to run
                title=item.split('/')[-1],
                subtitle=interpreter_of_item(item) + ' ' + item + ' ' + args,
                icon=icon(item),
                uid=item
            )
    return al


def interpreter_of_item(script_path):
    extension = script_path.split('.')[-1]
    return extension_interpreter[extension.lower()]


def to_list():
    with open(full_path, 'r') as f:
        return f.read().split('\t')


import os.path


def icon(path):
    name = os.path.splitext(os.path.basename(path))[0]
    eventual = icons_path + name + '.png'
    if os.path.exists(eventual):
        return eventual[0:-4]
    else:
        return interpreter_of_item(path)
