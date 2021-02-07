from flask import Flask, render_template, redirect, request
from model import db, connect_db, Pet
from forms import PetForm
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ghimire@localhost/adoptpets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'adoptpets'

connect_db(app)
db.create_all()


@app.route('/')
def home_page():
    pet_all = Pet.query.all()
    return render_template("home.html", pets=pet_all)


@app.route('/add', methods=['GET', 'POST'])
def add_pets():
    form = PetForm()
    if form.validate_on_submit():
        new = Pet(name=form.name.data, species=form.species.data,
                  photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
        db.session.add(new)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pets.html", form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def edit_pets(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('details.html', form=form)
