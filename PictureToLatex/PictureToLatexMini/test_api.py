import requests
import base64
import os

def test_file_upload():
    # 测试文件上传接口
    url = "http://localhost:8000/api/convert"
    # 使用上一级目录中的测试图片
    image_path = os.path.join('..', 'test_image.jpg')
    files = {'file': open(image_path, 'rb')}
    
    try:
        response = requests.post(url, files=files)
        print("文件上传测试结果:")
        print(response.json())
    except Exception as e:
        print(f"测试失败: {str(e)}")

def test_base64():
    # 测试base64接口
    url = "http://localhost:8000/api/convert_base64"
    
    # 读取图片并转换为base64
    image_path = os.path.join('..', 'test_image.jpg')
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    data = {
        "image": image_data
    }
    
    try:
        response = requests.post(url, json=data)
        print("\nBase64测试结果:")
        print(response.json())
    except Exception as e:
        print(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 确保后端服务已经启动
    print("开始测试API...")
    test_file_upload()
    test_base64() 