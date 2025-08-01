from app.models.base_model import BaseModel
from app.models.user import User
from app.services import facade


class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, description=" "):
        super().__init__()
        if len(title)>100:
            raise ValueError("Title length should be 100 charachters or less")
        self.title = title
        self.description = description
        if not isinstance(price,float) and not isinstance(price,int):
            raise TypeError("Price should be a number")
        if price<0:
            raise ValueError("Price should be greater than 0")   
        self.price = float(price)
        if latitude<-90.0 or latitude>90.0:
            raise ValueError("Latitude should be between -90.0 and 90.0 degrees")
        if longitude<-180.0 or longitude>180.0:
            raise ValueError("Longitude should be between -180.0 and 180.0 degrees")
        self.latitude = latitude
        self.longitude = longitude
       
        if  not owner:
            raise TypeError("owner should be an instance of User")    
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    def get_reviews(self):
        return self.reviews    

    def to_dict(self):
        print("in todict")
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "price":self.price,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "owner":self.owner.to_dict(),
            "amenities":[amenity.to_dict() for amenity in self.amenities],
            "reviews":[review.to_dict() for review in self.reviews]

        }
        