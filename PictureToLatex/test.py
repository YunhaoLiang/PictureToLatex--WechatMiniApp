from pix2text import Pix2Text, merge_line_texts

image_fps = {
    'test_image': 'test_image.png'
}

p2t = Pix2Text.from_config()

outs = p2t.recognize_formula(image_fps)

outs2 = p2t.recognize(r'C:\Users\Louis\Desktop\PictureToLatex\test_image.jpg', file_type='text_formula', return_text=True, save_analysis_res='test_image.jpg')  # recognize mixed images
print(outs2)



