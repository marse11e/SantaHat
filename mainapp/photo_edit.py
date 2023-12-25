import replicate
from dotenv import load_dotenv
from .models import PhotoEdit

load_dotenv()


class PhotoEditService:
    def __init__(self, image):
        self.image_src = image

    def photo_edit(self):
        print("1111111111111")
        replicate_url = replicate.run(
			"catio-apps/photoaistudio-generate:35e6cacd8af9023b480ddf4487855f4ae5c203a30b0d05fba1e735753ee5756d",
			input={
				"seed": 1,
				"steps": 8,
				"width": 768,
				"prompt": "[MODEL] wearing Santa hat and white gloves",
				"n_prompt": "",
				"face_image": open(self.image_src, "rb"),
				"pose_image": "https://99px.ru/sstorage/53/2019/08/tmb_267157_901377.jpg",
				"num_samples": 1,
				"face_resemblance": 0.5,
				"pose_resemblance": 0.8,
				"face_expanding_bbox": 0.5,
			}
		)
        print(replicate_url)
        return replicate_url
# input=111111111

# def photo_edit():
#     replicate_url = replicate.run(
#   "catio-apps/photoaistudio-generate:35e6cacd8af9023b480ddf4487855f4ae5c203a30b0d05fba1e735753ee5756d",
#   input={
#     "seed": 1,
#     "steps": 8,
#     "width": 768,
#     "prompt": "[MODEL] wearing Santa hat and white gloves",
#     "n_prompt": "",
#     "face_image": PhotoEdit.image.url,
#     "pose_image": "https://99px.ru/sstorage/53/2019/08/tmb_267157_901377.jpg",
#     "num_samples": 1,
#     "face_resemblance": 0.5,
#     "pose_resemblance": 0.8,
#     "face_expanding_bbox": 0.5
#   }
# )
#     return replicate_url

# new_url = PhotoEdit.objects.create(image_link=photo_edit())
# new_url.save()

# print(photo_edit())
