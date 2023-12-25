import replicate
from dotenv import load_dotenv
load_dotenv()

from time import time

s = time()

output = replicate.run(
  "catio-apps/photoaistudio-generate:35e6cacd8af9023b480ddf4487855f4ae5c203a30b0d05fba1e735753ee5756d",
  input={
    "seed": 1,
    "steps": 8,
    "width": 768,
    "prompt": "[MODEL] wearing Santa hat",
    "n_prompt": "",
    "face_image": open("a.jpg", "rb"),
    "pose_image": "https://pixel-shot.com/get_image/i-7620755-0.JPG",
    "num_samples": 1,
    "face_resemblance": 0.5,
    "pose_resemblance": 0.8,
    "face_expanding_bbox": 0.5
  }
)

e = time()


print(output)
print(e - s)