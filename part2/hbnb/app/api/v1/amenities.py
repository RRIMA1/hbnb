from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data= api.payload
        try:
            new_amenity=facade.create_amenity(amenity_data)
        except(ValueError) as e:
            return{'error':str(e)},400
        return new_amenity.to_dict()


    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenityList= facade.get_all_amenities()
        return[ amenity.to_dict() for amenity in amenityList]

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        print("-----")
        amenity= facade.amenity_repo.get(amenity_id)
        print("-----")
        if amenity:
            return amenity.to_dict(),200
        print("-----")
        return {'error':'Amenity not found'}
    
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data=api.payload
        print(amenity_data)
        amenity=facade.update_amenity(amenity_id,amenity_data)
        if not amenity:
            return {'error':"Amenity not found"},404
        return amenity.to_dict(),200