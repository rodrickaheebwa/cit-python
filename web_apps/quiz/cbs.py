from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from cbs_data import get_cbs_news
from config import configs

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow() 
migrate = Migrate()

app.config.from_object(configs())

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

class CbsNews(db.Model):
    __tablename__ = 'cbs_news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    @classmethod
    def get_all_news(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'description' : self.description,
            'image': self.image
        }

@app.route('/cbs_news')
def cbs_news():
    news_articles = get_cbs_news()
    for news in news_articles:
        row = CbsNews(title = news['title'], link = news['link'], description = news['description'], image = news['image'])
        row.save()
    data = CbsNews.get_all_news()
    return {'data': [news.serialize() for news in data]}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)