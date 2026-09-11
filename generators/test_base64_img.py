import base64, os

def get_base64_image_tag(img_path):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
        return f'<div style="text-align: center; margin: 15px 0;"><img src="data:image/png;base64,{encoded}" style="width: 100%; max-width: 720px; border: 1px solid #102c57; border-radius: 4px;" alt="תשריט ביקורת מתוך המודל"></div>'
    return '<div style="color: #888888; font-style: italic; margin: 10px 0;">[תשריט ביקורת משויך למודל ה-BIM]</div>'

# Test with a sample image
sample_img = '/home/yogi/lod_project/markup_ls_01_lobby_threshold_flooding.png'
tag = get_base64_image_tag(sample_img)
print(f"Sample Base64 Image Tag generated successfully (length: {len(tag)} chars)")
