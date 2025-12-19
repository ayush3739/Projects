from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests,os

load_dotenv('.env')
api_key=os.getenv('api_key')
url = 'https://api.themoviedb.org/3/search/movie'
movie_db_info_url="https://api.themoviedb.org/3/movie"
moviedb_img_url="https://image.tmdb.org/t/p/w500"


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

app = Flask(__name__)


class Ratingform(FlaskForm):
    rating= StringField(label='Your Rating out of 10 for e.g. 7.5')
    review= StringField(label= 'Review')
    done=SubmitField(label='Done')

class add_movie(FlaskForm):
    title= StringField(label='Movie Title')
    submit=SubmitField(label='Add Movie')

app.config['SECRET_KEY'] = 'THisbistest'
Bootstrap5(app)

# CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///movies-collection.db"
db=SQLAlchemy()
db.__init__(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():    
#     db.session.add(second_movie)
#     db.session.commit()



@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html",movies=all_movies)

@app.route('/edit/<int:id>',methods=["GET","POST"])
def update(id):
    form=Ratingform()
    edit_movie=db.session.execute(db.select(Movie).where(Movie.id==id)).scalar()
    if form.validate_on_submit():        
        edit_movie.rating=float(form.rating.data)
        edit_movie.review=form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html',form=form,movie=edit_movie)

@app.route('/delete')
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/add',methods=["GET","POST"])
def add():
    movie=add_movie()
    if movie.validate_on_submit():
        title=movie.title.data
        response=requests.get(url,params={'query':title},headers=headers)
        data=response.json()['results']
        return render_template('select.html',options=data)
    return render_template('add.html',form=movie)

@app.route('/find_movie')
def find_movie():
    movie_api_id=request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{movie_db_info_url}/{movie_api_id}?language=en-US"

        reponse=requests.get(movie_api_url,headers=headers)
        data=reponse.json()

        new_movie=Movie(
            title=data['title'],
            year=data["release_date"].split("-")[0],
            img_url=f"{moviedb_img_url}/{data["poster_path"]}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("update", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
