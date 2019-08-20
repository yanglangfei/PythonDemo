# https://www.lfd.uci.edu/~gohlke/pythonlibs/    pywin32
# https://sourceforge.net/projects/pywin32/files/pywin32/
import pyHook
import os

import pythoncom


def OnKeyboardEvent(event):
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    if not os.path.exists('../file'):
        os.makedirs('../file')
    f = open('../file/key_event.log', mode='a', encoding='utf-8')
    f.write(event.Key+"------"+event.WindowName+'\n')
    f.flush()
    f.close()
    return True


def OnMouseEvent(event):
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Position:', event.Position)
    print('Wheel:', event.Wheel)
    print('Injected:', event.Injected)
    print('---')
    return True


hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.MouseAllButtonsDown = OnMouseEvent
hm.HookKeyboard()
hm.HookMouse()
pythoncom.PumpMessages()
