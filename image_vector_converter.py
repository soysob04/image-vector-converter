# Image Vector Converter Notebook

# 1️⃣ Install Dependencies
!apt-get install potrace
!pip install opencv-python pillow cairosvg

# 2️⃣ Upload Image
from google.colab import files
from PIL import Image
import io

uploaded = files.upload()
filename = next(iter(uploaded))
img = Image.open(io.BytesIO(uploaded[filename]))
img.show()

# 3️⃣ Convert to Black & White Bitmap (PBM)
import cv2
img_cv = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(img_cv, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite("bitmap.pbm", thresh)

# 4️⃣ Convert PBM to SVG using Potrace
!potrace bitmap.pbm -s -o output.svg

# 5️⃣ Display SVG
from IPython.display import SVG, display
display(SVG(filename="output.svg"))

# 6️⃣ Convert SVG to PNG and PDF
import cairosvg

cairosvg.svg2png(url='output.svg', write_to='output.png')
cairosvg.svg2pdf(url='output.svg', write_to='output.pdf')

# 7️⃣ Show PNG
img_png = Image.open("output.png")
img_png.show()

# 8️⃣ Download Files
files.download("output.svg")
files.download("output.png")
files.download("output.pdf")

# 9️⃣ Create ZIP File
import shutil
!mkdir project_files
!cp *.ipynb project_files/
!cp *.svg project_files/
!cp *.png project_files/
!cp *.pdf project_files/
shutil.make_archive("image_vector_project", 'zip', "project_files")
files.download("image_vector_project.zip")
