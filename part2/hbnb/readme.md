# HBNB Part 2
## Description
In the second part of the Hbnb project we have implemented the Business logic of our application using python and Flask. It allows us to manage the entities chosen in part 1 (Users,Places,Amenities and Reviews).

### Installation

1. **Clone the repository**
   ```bash
   git clone repo_url.git
   cd holbertonschool-hbnb/part2/hbnb
   ```

2. **Set up virtual environment** 
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
##  Dependencies

```txt
flask
flask-restx
```   
   
## Project Structure 
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── test.py
├── readme.md 
```
## Api Endpoints

#### /api/v1/users
- GET /users: list users
- POST /users: create user
- PUT /users/\<id>: update user

#### /api/v1/places
- GET /places: list places
- POST /places: create place
- PUT /places/\<id>: create place

#### /api/v1/amenities
- GET /amenities: list amenities
- POST /amenities: create amenity
- PUT /amenities/\<id>: update amenity

#### /api/v1/reviews
- GET /reviews: list reviews
- POST /reviews: create review
- PUT /reviews/\<id>: update review
- DELETE /reviews/\<id>: delete review

#### /api/v1/places/<place_id>/reviews
- Get all reviews for a specific place

## Code example
``` python
    def to_dict(self):
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
```

## Testing
You can use the test.py file to test the creation of users for example. To test the Api endpoints you can use SwaggerUI on http://127.0.0.1:5001/api/v1/
**Test example:**
``` json

{
  "first_name": "string",
  "last_name": "string",
  "email": "string"
}
returns error invalid email
```
``` json
{
  "first_name": "string",
  "last_name": "string",
  "email": "name.last_name@gmail.com"
}
returns user created successfully 
```
**Or it can be tested using curl**

```bash
curl -X 'POST' \
  'http://127.0.0.1:5001/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "string",
  "last_name": "string",
  "email": "name.last_name@gmail.com"
}'
```
