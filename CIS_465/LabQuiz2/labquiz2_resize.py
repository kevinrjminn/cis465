
from PIL import Image
img = Image.open('CSU_Logo.jpg')
new_img = img.resize((500,500), Image.ANTIALIAS)
quality_val = 90
new_img.save("CSU.jpg", "JPEG", quality=quality_val)
