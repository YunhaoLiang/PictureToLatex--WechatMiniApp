from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pix2text import Pix2Text
import uvicorn
from PIL import Image
import io
import base64
import json
import time
import os

app = FastAPI()

# 配置CORS，允许微信小程序访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境需要替换为小程序的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化Pix2Text
p2t = Pix2Text.from_config()

# 创建输出目录
os.makedirs("output", exist_ok=True)

@app.post("/api/convert")
async def convert_image_to_latex(file: UploadFile = File(...)):
    try:
        # 读取上传的图片
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # 转换图片为LaTeX
        result = p2t.recognize(image, file_type='text_formula', return_text=True)
        
        # 保存结果到文件
        timestamp = int(time.time())
        output_file = f"output/latex_{timestamp}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        
        return {
            "code": 0,
            "msg": "success",
            "data": {
                "latex": result,
                "output_file": output_file
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/convert_base64")
async def convert_base64_to_latex(data: dict = Body(...)):
    try:
        # 检查图片数据是否存在
        if "image" not in data:
            raise HTTPException(status_code=400, detail="Missing image data")
            
        # 从base64字符串解码图片
        try:
            image_data = base64.b64decode(data.get("image"))
            image = Image.open(io.BytesIO(image_data))
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image data: {str(e)}")
        
        # 转换图片为LaTeX
        result = p2t.recognize(image, file_type='text_formula', return_text=True)
        
        # 保存结果到文件
        timestamp = int(time.time())
        output_file = f"output/latex_{timestamp}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        
        return {
            "code": 0,
            "msg": "success",
            "data": {
                "latex": result,
                "output_file": output_file
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "PictureToLatexMini"}

if __name__ == "__main__":
    # 使用8001端口避免冲突
    uvicorn.run(app, host="0.0.0.0", port=8001) 