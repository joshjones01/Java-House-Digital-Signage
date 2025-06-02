import os
from PIL import Image

def process_image(input_path, output_path):
    # Load image
    img = Image.open(input_path)

    # Step 1: Rotate 90 degrees
    rotated = img.rotate(90, expand=True)

    # Step 2: Compress width to 1080px (maintain aspect ratio)
    width = 1080
    aspect_ratio = rotated.height / rotated.width
    new_height = int(width * aspect_ratio)
    resized_x = rotated.resize((width, new_height), Image.LANCZOS)

    # Step 3: Stretch height to 1920px (force final size)
    final_image = resized_x.resize((1080, 1920), Image.LANCZOS)

    # Step 4: Save as PNG
    final_image.save(output_path, format='PNG')
    print(f"Saved: {output_path}")

def batch_process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(input_folder, filename)
            output_filename = 'S&R_' + os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)

            process_image(input_path, output_path)

# Example usage:
input_folder = '/Users/josh/Documents/GitHub/Java-House-Digital-Signage/SnR Module/input'     # Replace with your folder path
output_folder = '/Users/josh/Documents/GitHub/Java-House-Digital-Signage/SnR Module/output'   # Folder to save processed images
batch_process_images(input_folder, output_folder)
