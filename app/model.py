from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as sor
from app import db 
from datetime import datetime,timezone
# in python db model every row is defined as single object
# db.Model is class inheritance from sqlAlchemy  
class users(db.Model):
    id: sor.Mapped[int] = sor.mapped_column(primary_key=True )
    username : sor.Mapped[str] = sor.mapped_column(sa.String(64) , index=True , unique=True)
    email : sor.Mapped[str] = sor.mapped_column(sa.String(120) , index=True , unique=True)
    password_hash : sor.Mapped[Optional[str]] = sor.mapped_column(sa.String(256))
    # this method is used for log and errors this function returns where the problem is in relation
    posts: sor.WriteOnlyMapped["Post"] = sor.relationship(back_populates="author")
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Post(db.Model):
    id:sor.Mapped[int] = sor.mapped_column(primary_key=True)
    body: sor.Mapped[str] = sor.mapped_column(sa.String(140)) 
    timestamp : sor.Mapped[datetime] = sor.mapped_column(
            index=True , 
    default=lambda:datetime.now(timezone.utc)
    )
    user_id: sor.Mapped[int] = sor.mapped_column(sa.ForeignKey(users.id) , index=True)
    author : sor.Mapped[users] = sor.relationship(back_populates="posts")
    def __repr__(self):
        return "Post{}".format(self.body)