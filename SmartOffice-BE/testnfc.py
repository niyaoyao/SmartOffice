from serial import Serial
import serial
import time

# 设置串口参数
baudrate = 115200
port = "/dev/tty.usbserial-210"  # 更改为你的串口号

# 初始化串口
ser = serial.Serial(port, baudrate, timeout=1)

def send_frame(frame):
    # 将帧数据转换为字节
    frame_bytes = bytes.fromhex(frame)
    # 发送数据
    ser.write(frame_bytes)
    # 读取响应
    response = ser.read(255)
    return response

# 打开串口
# ser.open()

# 唤醒模块
wake_up_frame = "555500000000000000000000000000000000FF03FDD414011700"
response = send_frame(wake_up_frame)
print("唤醒模块响应：", response.hex())



# 探测Mifare Classic卡
detect_card_frame = "0000FF04FCD44A0100E100"


time.sleep(1)

response = send_frame(detect_card_frame)
print("探测卡响应：", response.hex())

# 关闭串口
ser.close()
