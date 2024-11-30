from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    #posts = db.relationship('Post', backref='user_id', lazy=True)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relación inversa: cada post está relacionado con un único usuario
    #user = db.relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post(title={self.title}, content={self.content[:20]}...)>"