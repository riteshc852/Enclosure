from app import app
import sqlalchemy as sa
import sqlalchemy.orm as sor
from app import app, db
from app.model import users, Post
# added shell context for flask shell command
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'sor': sor, 'db': db, 'User': users, 'Post': Post}