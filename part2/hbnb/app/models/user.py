import re
from app.models.base_model import BaseModel
class User(BaseModel):
    def __init__(self,first_name,last_name,email,is_admin=False):
        super().__init__()
        if len(first_name)>50 or len(last_name)>50:
            raise ValueError("Names must be less than 50 char")
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Please enter a valid email")
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.is_admin=is_admin
        self.places=[]
    def to_dict(self):
        return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email}