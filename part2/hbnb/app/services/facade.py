from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.models.user import User
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo= InMemoryRepository()
        self.review_repo= InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    def get_users(self):
        return self.user_repo.get_all()

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def update_user(self,user_id,user_data):
        user=self.user_repo.get(user_id)
        if not user:
            return None
        for key,value in user_data.items():
            if hasattr(user,key):
                setattr(user,key,value)
        return user
    
    def create_amenity(self, amenity_data):
        amenity= Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity=self.amenity_repo.get(amenity_id)

        if not amenity:
            return None
        for key,value in amenity_data.items():
            if hasattr(amenity,key):
                setattr(amenity,key,value)
        return amenity     
    
    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        
        desc= place_data["description"] if place_data["description"] else ""
        amenities_list= place_data["amenities"]
        owner_instance=self.get_user(place_data["owner_id"])
        place=Place(title=place_data["title"],
                    price=place_data["price"],
                    latitude=place_data["latitude"],
                    longitude=place_data["longitude"],
                    owner=owner_instance,
                    description=desc
                    )
        for amenity_id in amenities_list:
            amenity=self.get_amenity(amenity_id)
            print(amenity)
            if amenity:
                place.add_amenity(amenity)
            else:
                raise ValueError("There is no amenity with id:{amenity_id}")
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place=self.place_repo.get(place_id)
        if not place:
            return None
        return place
        

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        print("in update1")
    # Placeholder for logic to update a place
        place=self.get_place(place_id)
        print(place)
        print("in update1")        
        if place is None:
            print("in here")
            return place
        print("in update2")
        for key,value in place_data.items():
            if hasattr(place,key):
                setattr(place,key,value)
        return place
    

    def create_review(self, review_data):
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        place = self.get_place(review_data['place_id'])
        if place is None:
            raise ValueError("Place Not found")
        user =self.get_user(review_data["user_id"])
        if user is None:
            raise ValueError("User Not found")        
        review= Review(text=review_data["text"],rating=review_data["rating"],user=user,place=place)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        place = self.get_place(place_id)
        if place is None:
            raise ValueError("Place Not found")
        return place.get_reviews()

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
         review=self.get_review(review_id)
         print(review)
         if review is None:
            print("in here")
            return review
         print("in update2")
         for key,value in review_data.items():
            if hasattr(review,key):
                setattr(review,key,value)
         return review

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        self.review_repo.delete(review_id)
        return True