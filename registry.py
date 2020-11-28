from ctypes import *
from ctypes import wintypes as w


def regc():
    HKEY = c_void_p
    PHKEY = POINTER(HKEY)
    LPSECURITY_ATTRIBUTES = c_void_p
    REGSAM = w.DWORD
    LSTATUS = w.LONG

    REG_CREATED_NEW_KEY = 0x00000001
    REG_OPENED_EXISTING_KEY = 0x00000002

    ERROR_SUCCESS = 0

    HKEY_CURRENT_USER = c_void_p(0x80000001)
    REG_OPTION_NON_VOLATILE = 0
    KEY_ALL_ACCESS = 0x000F003F

    reg = WinDLL('kernel32')
    reg.RegCreateKeyExW.argtypes = HKEY, w.LPCWSTR, w.DWORD, w.LPWSTR, w.DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, w.LPDWORD
    reg.RegCreateKeyExW.restype = LSTATUS
    print(reg)

    hkey = 'HKEY_CURRENT_USER'
    lsubkey = r'Software\Microsoft\Windows\CurrentVersion\Run\Client'
    reserved = 0
    flag = REG_OPTION_NON_VOLATILE
    samdesired = KEY_ALL_ACCESS
    ipsec = None
    handle = HKEY()
    disp = w.DWORD()

    status = reg.RegCreateKeyExW(HKEY_CURRENT_USER, lsubkey, reserved, None, flag, samdesired, None, byref(handle), byref(disp))
    if status == ERROR_SUCCESS:
        print(f'"{disp=} {handle=}')
