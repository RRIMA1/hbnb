from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        review_data=api.payload
        try:
            review=facade.create_review(review_data)
        except(ValueError) as e:
            return{'error':str(e)},400
        print("1-----")
        place=facade.get_place(review_data["place_id"])
        print("2-----")
        place.add_review(review)
        print("3-----")

        return review.to_dict()

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        reviews_list= facade.get_all_reviews()
        return [review.to_dict() for review in reviews_list],200 

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review=facade.get_review(review_id)
        if not review:
            return {"error":"review not found"},200
        return review.to_dict(),200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        review_data=api.payload
        review=facade.update_review(review_id,review_data)
        if review is None:
            return{"error":"review doesn't exist"}
        return review.to_dict(),200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        deleted=facade.delete_review(review_id)
        if deleted:
            return{"msg":"deleted"},200
        
@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        place=facade.get_place(place_id)
        if not place:
            return{"error":"Place not found"},404        
        return [review.to_dict() for review in place.get_reviews()],200