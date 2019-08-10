import pyautogui

# 保护措施，避免失控
pyautogui.FAILSAFE = True
# 为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.5
isOn = pyautogui.onScreen(0, 0)
# 确定  0,0 点 是否在屏幕
print(isOn)
#  获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()

print("screen height:{}, screen width:{}".format(screenHeight, screenWidth))
# 2 秒钟 鼠标移动坐标为 (100,100) 的位置(绝对位置)
pyautogui.moveTo(x=100, y=100, duration=2, tween=pyautogui.linear)
#  用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
pyautogui.moveTo(x=500, y=500, duration=2, tween=pyautogui.easeInOutQuad)
# 移动鼠标位置(相对位置)
# pyautogui.moveRel(10, 20)
# 鼠标相对移动 ,向下移动
pyautogui.moveRel(None, 10)
pyautogui.moveRel(xOffset=None, yOffset=10, duration=0.0, tween=pyautogui.linear)
# 拖拽鼠标
pyautogui.dragTo(x=427, y=535, duration=3, button='left')
# 鼠标相对拖拽
pyautogui.dragRel(xOffset=100, yOffset=100, duration=2, button='left', mouseDownUp=False)

# 鼠标左击一次
# x
# y
# clicks 点击次数
# interval点击之间的间隔
# button 'left', 'middle', 'right' 对应鼠标 左 中 右或者取值(1, 2, or 3)
# tween 渐变函数
pyautogui.click(x=1000, y=2100)
# 鼠标当前位置双击
pyautogui.doubleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
# 鼠标当前位置三击
pyautogui.tripleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)

# 右击
pyautogui.rightClick()
# 中击
pyautogui.middleClick()

# 鼠标移动到x=1796, y=778位置按下
pyautogui.mouseDown(x=1796, y=778, button='left')
# 鼠标移动到x=2745, y=778位置松开（与mouseDown组合使用选中）
pyautogui.mouseUp(x=2745, y=778, button='left', duration=5)
# 鼠标当前位置滚轮滚动
pyautogui.scroll()
# 鼠标水平滚动（Linux）
pyautogui.hscroll()
# 鼠标左右滚动（Linux）
pyautogui.vscroll()

# pyautogui.scroll(10, x=100, y=100)
# 键盘输入
pyautogui.typewrite(message='Hello world!', interval=0.5)
pyautogui.keyDown("H")
pyautogui.press("left")
pyautogui.keyUp("H")

pyautogui.hotkey()
pyautogui.alert(text='This is an alert box.', title='Test')
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
pyautogui.prompt("提示")
pwd = pyautogui.password('Enter password (text will be hidden)')

# 截屏
im1 = pyautogui.screenshot()
# 确定点的颜色
color = im1.getpixel((100, 200))
# 截屏保存在当前目录下
im2 = pyautogui.screenshot('my_screenshot.png')
pyautogui.locateOnScreen("my_screenshot.png")
# 截取 矩形框
im = pyautogui.screenshot(region=(0, 0, 300, 400))
# 测量屏幕大小
a = pyautogui.locateOnScreen(im)
# 截图中心点坐标
center = pyautogui.center("my_screenshot.png")
pyautogui.locateCenterOnScreen('calc7key.png')
print(center)
