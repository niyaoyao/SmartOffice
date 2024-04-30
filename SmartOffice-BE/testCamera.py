import cv2

def main():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # 循环显示视频帧
    while True:
        # 读取视频帧
        ret, frame = cap.read()

        # 如果没有帧可读，跳出循环
        if not ret:
            print("无法读取视频帧")
            break

        # 显示视频帧
        cv2.imshow('Camera', frame)

        # 按下'q'键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头资源
    cap.release()

    # 关闭所有窗口
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
