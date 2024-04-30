from datetime import datetime

import cv2

from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin
from sqlalchemy import desc

from face_recongnition.face_dataset import getfaceDataSet
from face_recongnition.face_training import train_face_recognizer
from sqlchemy_class.database_config import get_session
from sqlchemy_class.user import OfficeUser, OfficeUserInfo, OfficeUserLog

# 启动 flask 配置跨域
app = Flask(__name__)
CORS(app)


def faceRecognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(
        '/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/trainer/trainer.yml')
    cascadePath = "/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    # iniciate id counter
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'qmy', 'Paula', 'Ilza', 'Z', 'W']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        # img = cv2.flip(img, -1) # Flip vertically

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):


                with get_session() as session:
                    user = session.query(OfficeUser).get(id)
                    session.close()
                    id = user.name
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        if id != 'unknown' and id != 0:
            break
        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    return id
    cam.release()


# 获取人脸训练集
@app.route('/face/get')
@cross_origin()
def getFace():
    faceId = request.args.get('faceid')
    result = getfaceDataSet(int(faceId))
    return result


# 训练获取到的数据
@app.route('/face/train')
@cross_origin()
def trainFace():
    result = train_face_recognizer()
    return result


# 验证人脸
@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    data = request.json

    # # 将Base64编码的图像数据存储在变量中
    # base64_data = data.get('image')

    result = faceRecognition()
    print(result)

    return jsonify(result)


# @app.route('/office_users', methods=['GET'])
# def get_office_users():
#     with get_session() as session:
#         users = session.query(OfficeUser).all()
#         session.close()
#         print(users)
#         for user in users:
#             print(user.id)


@app.route('/office_user', methods=['GET'])
def get_office_user():
    user_id = request.args.get('user_id')
    with get_session() as session:
        user = session.query(OfficeUser).get(user_id)
        session.close()
        print(user.id)
        print(user.name)
        print(user.password)
        return jsonify({"id": user.id, "name": user.name, "password": user.password})


@app.route('/office_user', methods=['POST'])
def create_office_user():
    data = request.json
    if 'name' not in data or 'password' not in data:
        return jsonify({"message": "Name and password are required"}), 400
    new_user = OfficeUser(name=data['name'], password=data['password'])
    with get_session() as session:
        session.add(new_user)
        session.commit()
        session.close()
        return jsonify({"message": "User created successfully", "user_id": new_user.id}), 200


@app.route('/office_user/<int:user_id>', methods=['PUT'])
def update_office_user(user_id):
    with get_session() as session:
        user = session.query(OfficeUser).get(user_id)
        if not user:
            session.close()
            return jsonify({"message": "User not found"}), 404
        data = request.json
        if 'name' in data:
            user.name = data['name']
        if 'password' in data:
            user.password = data['password']
        session.commit()
        session.close()
        return jsonify({"message": "User updated successfully"})


@app.route('/office_user/<int:user_id>', methods=['DELETE'])
def delete_office_user(user_id):
    with get_session() as session:
        user = session.query(OfficeUser).get(user_id)
        if not user:
            session.close()
            return jsonify({"message": "User not found"}), 404
        session.delete(user)
        session.commit()
        session.close()
        return jsonify({"message": "User deleted successfully"})


@app.route('/office_users/info', methods=['GET'])
@cross_origin()
def get_office_users_info():
    user_id = request.args.get('user_id')
    with get_session() as session:
        userInfo = session.query(OfficeUserInfo).get(user_id)
        session.close()
        return jsonify({"id": userInfo.user_id, "zone1_light": userInfo.zone1_light,
                        "zone1_fancoil": userInfo.zone1_fancoil, "zone2_light": userInfo.zone2_light,
                        "zone2_fancoil": userInfo.zone2_fancoil, "office_pau": userInfo.office_pau})


@app.route('/office_users/info', methods=['POST'])
@cross_origin()
def update_office_user_info():
    data = request.json
    user_id = data.get('id')
    if not user_id:
        return jsonify({'error': 'Missing user_id'}), 400

    with get_session() as session:
        try:
            user = session.query(OfficeUserInfo).filter_by(user_id=user_id).first()
            if not user:
                return jsonify({'error': 'User not found'}), 404

            # 更新用户信息
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)

            # 更新修改时间
            user.update_time = datetime.now()

            session.commit()
            return jsonify({'message': 'User information updated successfully'}), 200
        except Exception as e:
            session.rollback()
            return jsonify({'error': str(e)}), 500
        finally:
            session.close()


@app.route('/users', methods=['GET'])
@cross_origin()
def get_users():
    with get_session() as session:
        users = session.query(OfficeUser).all()
        session.close()
        userList = []
        for user in users:
            userList.append(user.to_json())

        return jsonify(userList)


@app.route('/users/<int:user_id>', methods=['GET'])
@cross_origin()
def get_user(user_id):
    with get_session() as session:
        user = session.query(OfficeUser).get(user_id)
        session.close()
        if user:
            return jsonify(user.__dict__)
        else:
            return jsonify({'error': '未找到用户'}), 404


@app.route('/users', methods=['POST'])
@cross_origin()
def create_user():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    if not name or not password:
        return jsonify({'error': '用户名和密码为必填项'}), 400
    with get_session() as session:
        user = OfficeUser( name=name, password=password, update_time=datetime.now())
        session.add(user)
        session.commit()
        session.close()
        return jsonify({'message': '用户创建成功'})


@app.route('/users/<int:user_id>', methods=['PUT'])
@cross_origin()
def update_user(user_id):
    data = request.json
    with get_session() as session:
        user = session.query(OfficeUser).get(user_id)
        if not user:
            session.close()
            return jsonify({'error': '未找到用户'}), 404
        user.name = data.get('name', user.name)
        user.password = data.get('password', user.password)
        session.commit()
        session.close()
        return jsonify({'message': '用户更新成功'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
@cross_origin()
def delete_user(user_id):
    with get_session() as session:
        user = session.query(OfficeUser).get(user_id)
        if not user:
            session.close()
            return jsonify({'error': '未找到用户'}), 404
        session.delete(user)
        session.commit()
        session.close()
        return jsonify({'message': '用户删除成功'})


@app.route('/logs', methods=['GET'])
def get_logs():
    # 从请求中获取查询参数
    username = request.args.get('username')
    user_id = request.args.get('id')

    # 构建查询
    with get_session() as session:
        query = session.query(OfficeUserLog, OfficeUser).join(
            OfficeUser, OfficeUserLog.user_id == OfficeUser.id
        ).order_by(desc(OfficeUserLog.start_time_1))

        # 添加条件：按照用户名模糊查询
        if username:
            query = query.filter(OfficeUser.name.ilike(f'%{username}%'))

        # 添加条件：按照用户ID精确查询
        if user_id:
            query = query.filter(OfficeUser.id == int(user_id))

        # 执行查询
        results = query.all()

        # 格式化查询结果
        logs = []
        for log, user in results:
            logs.append({
                'id': log.id,
                'user_id': log.user_id,
                'username': user.name,
                'start_time_1': log.start_time_1.isoformat(),
                'start_time_2': log.start_time_2.isoformat(),
                'end_time_1': log.end_time_1.isoformat(),
                'end_time_2': log.end_time_2.isoformat(),
            })

        return jsonify(logs)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=True)
