from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self,text,rating,place,user):
        super().__init__()
        self.text=text
        if not isinstance(rating,int):
            raise TypeError("rating should be an int")
        elif 0>rating or rating>5:
            raise ValueError("rating should be between 0 and 5")
        self.rating=rating
        if  not isinstance(user,User):
            raise TypeError("user should be an instance of User")
        self.user=user    
        if  not isinstance(place,Place):
            raise TypeError("place should be an instance of Place")
        self.place=place    
                        
    def to_dict(self):
        return {
            "id":self.id,
            "text": self.text,
            "rating":self.rating,
            "owner":self.user.id,
            "place":self.place.id#can be modified to return only id
        }

