from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self,name):
        super().__init__()
        if len(name)>50:
            raise ValueError("Name should be at most 50 characters")
        self.name=name
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }        

