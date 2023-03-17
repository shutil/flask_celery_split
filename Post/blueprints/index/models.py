from extensions.Database import db
from dataclasses import dataclass


@dataclass
class Post(db.Model):
    id:int
    post_text: str
    user_id: int
    
    __tablename__='post'
    id = db.Column(db.BigInteger(),autoincrement=True,primary_key=True)
    post_text = db.Column(db.Text(),nullable=False)
    user_id = db.Column(db.BigInteger(),nullable=False)

    def __repr__(self):
        return f"<Post id='{self.id}' post_text='{self.post_text}' user_id='{self.user_id}'/>"