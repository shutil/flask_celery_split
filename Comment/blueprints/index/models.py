from extensions.Database import db
from dataclasses import dataclass


@dataclass
class Comment(db.Model):
    id:int
    comment_text: str
    post_id: int
    user_id: int
    
    __tablename__='comment'
    id = db.Column(db.BigInteger(),autoincrement=True,primary_key=True)
    comment_text = db.Column(db.Text(),nullable=False)
    post_id = db.Column(db.BigInteger(),nullable=False)
    user_id = db.Column(db.BigInteger(),nullable=False)

    def __repr__(self):
        return f"<Comment id='{self.id}' comment_text='{self.comment_text}' post_id='{self.post_id}' user_id='{self.user_id}'/>"