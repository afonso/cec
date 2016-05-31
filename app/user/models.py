from app.extensions import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    comment = db.Column(db.Text(), unique=False)

    def __init__(self, nickname: str, email: str, comment: str) -> None:

        self.nickname = nickname
        self.email = email
        self.comment = comment

    def __repr__(self) -> str:
        return '<User {!r}>'.format(self.nickname)
