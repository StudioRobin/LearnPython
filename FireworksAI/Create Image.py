# pip install 'fireworks-ai'
import fireworks.client
from fireworks.client.image import ImageInference, Answer

# Initialize the ImageInference client
fireworks.client.api_key = "JSpFwkIGCUmGDrWEAkYbLyPlUm545EnxnZ2lLpMHkD4E4N3l"
inference_client = ImageInference(model="playground-v2-1024px-aesthetic")
#SSD-1B, playground-v2-1024px-aesthetic, stable-diffusion-xl-1024-v1-0, japanese-stable-diffusion-xl

# Generate an image using the text_to_image method
answer : Answer = inference_client.text_to_image(
    prompt="An origami-inspired goat with geometric folds in a surreal land: candy-colored trees, a smiling sun with sunbeams, and small 3D-animated children playing under cotton-like clouds. Bright, fantastical lighting enhances the joyful mood.",
    cfg_scale=7,
    height=1024,
    width=1024,
    sampler=None,
    steps=30,
    seed=1,
    safety_check=False,
    output_image_format="JPG",
    # Add additional parameters here
)

if answer.image is None:
  raise RuntimeError(f"No return image, {answer.finish_reason}")
else:
  answer.image.save("output.jpg")