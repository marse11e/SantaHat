import replicate
from dotenv import load_dotenv
from .models import PhotoEdit

load_dotenv()


class PhotoEditService:
    def __init__(self, image_id):
        self.image_id = image_id

    def get_image(self):
        image = PhotoEdit.objects.get(id=self.image_id)
        self.image_src = image.image.path
        return self.image_src
    
    def photo_edit(self):
        replicate_url = replicate.run(
			"catio-apps/photoaistudio-generate:35e6cacd8af9023b480ddf4487855f4ae5c203a30b0d05fba1e735753ee5756d",
			input={
				"seed": 1,
				"steps": 8,
				"width": 768,
				"prompt": "[MODEL] wearing Santa hat and white gloves",
				"n_prompt": "",
				"face_image": open(self.get_image(), "rb"),
				"pose_image": "https://99px.ru/sstorage/53/2019/08/tmb_267157_901377.jpg",
				"num_samples": 1,
				"face_resemblance": 0.5,
				"pose_resemblance": 0.8,
				"face_expanding_bbox": 0.5,
			}
		)
        return replicate_url[0]
