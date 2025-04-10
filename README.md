# PictureToLatex--WechatMiniApp
Image-to-LaTeX formula converter powered by OCR technology. This project includes a WeChat Mini Program frontend and Python backend, allowing users to take photos or select images of mathematical formulas and convert them into editable LaTeX code.

## Project Description

This project uses advanced image recognition technology (pix2text library) to identify mathematical formulas, providing two main functional interfaces:
1. Image file upload conversion interface (/api/convert)
2. Base64 encoded image conversion interface (/api/convert_base64)

The system uses Python FastAPI to build the backend service, providing RESTful API services, coupled with a WeChat Mini Program frontend to implement a user-friendly interface.

## Technology Stack

- **Backend**: Python, FastAPI, Pix2Text, PyTorch
- **Frontend**: WeChat Mini Program

## Project Structure

```
PictureToLatex/
├── PictureToLatexMini/         # Main project directory
│   ├── backend.py              # FastAPI backend service
│   ├── test_api.py             # API test file
│   └── wechat_mini_example/    # WeChat Mini Program frontend example
├── output/                     # Output files directory
├── formula.jpg                 # Test sample image
├── test.py                     # Test script
└── requirements.txt            # Python dependencies
```

## Features

- Photo Recognition: Directly capture math formulas for recognition
- Image Upload: Select formula images from photo album
- High-Precision Recognition: Support for complex mathematical formulas
- Instant Conversion: Quickly convert images to LaTeX code
- Result Editing: Support for fine-tuning recognition results

## Installation and Usage

### Backend Deployment

1. Clone the repository
```bash
git clone https://github.com/your-username/PictureToLatex--WechatMiniApp.git
cd PictureToLatex--WechatMiniApp/PictureToLatex
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the backend service
```bash
cd PictureToLatexMini
python backend.py
```

### WeChat Mini Program Deployment

1. Open WeChat Developer Tools
2. Import the project (PictureToLatexMini/wechat_mini_example directory)
3. Configure the server address (pointing to your deployed backend service)
4. Compile and run

## API Documentation

### 1. Image File Upload Conversion Interface

- **URL**: `/api/convert`
- **Method**: POST
- **Request Body**: multipart/form-data format image file
- **Response**: LaTeX code in JSON format

### 2. Base64 Encoded Image Conversion Interface

- **URL**: `/api/convert_base64`
- **Method**: POST
- **Request Body**: Base64 encoded image data in JSON format
- **Response**: LaTeX code in JSON format

## Contribution Guidelines

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
