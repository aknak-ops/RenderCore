
import os
from PIL import Image

def generate_grid(folder, output="thumb_grid.jpg", thumb_size=(300, 300)):
    thumbs = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png") or file.endswith(".jpg"):
            img = Image.open(os.path.join(folder, file)).resize(thumb_size)
            thumbs.append(img)

    if not thumbs:
        print("No images found.")
        return

    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    grid = Image.new("RGB", (cols * thumb_size[0], rows * thumb_size[1]))

    for i, thumb in enumerate(thumbs):
        x = (i % cols) * thumb_size[0]
        y = (i // cols) * thumb_size[1]
        grid.paste(thumb, (x, y))

    grid.save(output)
    print(f"[OK] Grid saved to {output}")

if __name__ == "__main__":
    generate_grid("renders/Barbell_Bicep_Curl")
