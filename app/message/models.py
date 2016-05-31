from app.extensions import db


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('messages', lazy='dynamic')
    )

    def __init__(self, content: str, user: models.User) -> None:

        self.content = content
        self.user = user

    def __repr__(self) -> str:
        return '<Message {} From: {}>'.format(self.id, self.user.nickname)
