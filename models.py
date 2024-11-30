from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    # Relación con Post
    posts = db.relationship('Post', back_populates='author', lazy=True)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # Clave foránea apuntando a User.id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relación con User
    author = db.relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post(title={self.title}, content={self.content[:20]}...)>"