# PictureToLatex微信小程序

一款基于AI技术的微信小程序，能够将数学公式图片自动识别并转换为LaTeX代码。

## 项目描述

该项目利用先进的图像识别技术（pix2text库）识别数学公式，提供了两个主要功能接口：
1. 图片文件上传转换接口(/api/convert)
2. Base64编码图片转换接口(/api/convert_base64)

系统使用Python FastAPI构建后端服务，提供RESTful API服务，配合微信小程序前端实现用户友好的界面。

## 技术栈

- 后端：Python, FastAPI, Pix2Text, PyTorch
- 前端：微信小程序

## 项目结构

- `PictureToLatexMini/`：主项目目录
  - `backend.py`：FastAPI后端服务
  - `test_api.py`：API测试文件
  - `wechat_mini_example/`：微信小程序前端示例
- `requirements.txt`：Python依赖包

## 安装与使用

1. 克隆仓库
```bash
git clone https://github.com/您的用户名/PictureToLatex.git
cd PictureToLatex
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行后端服务
```bash
cd PictureToLatexMini
python backend.py
```

4. 配置微信小程序开发环境并导入`wechat_mini_example`目录

## GitHub上传指南

### 初次上传项目到GitHub

1. 创建GitHub仓库
   - 登录GitHub账号
   - 点击右上角"+"图标，选择"New repository"
   - 填写仓库名称（如"PictureToLatex"）和描述
   - 选择公开或私有
   - 点击"Create repository"

2. 初始化本地Git仓库并推送
```bash
# 在项目根目录下
git init
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/您的用户名/PictureToLatex.git
git push -u origin main
```

### 更新项目

```bash
# 添加修改的文件
git add .

# 提交修改
git commit -m "更新说明"

# 推送到GitHub
git push origin main
```

### 忽略文件

创建`.gitignore`文件以忽略不需要上传的文件：

```
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
env/
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/

# 输出文件
output/

# 环境配置
.env

# IDE配置
.idea/
.vscode/
*.swp
*.swo
```

## 许可证

[指定您的许可证类型] 