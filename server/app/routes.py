from flask import request, jsonify, Blueprint
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from .models import User, Word, MasteredWord
from . import db

api = Blueprint('api', __name__)

# Login/Logout/Register


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify(message="Invalid username or password"), 401


@login_required
@api.route('/logout')
def logout():
    logout_user()
    return jsonify(message="Logged out")


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return jsonify(message="Username already taken"), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User created successfully"), 201

# Word-related routes


@api.route('/add_word', methods=['POST'])
def add_word():
    data = request.get_json()
    word = data['word']
    definition = data['definition']
    example_sentence = data.get('example_sentence')

    new_word = Word(word=word, definition=definition,
                    example_sentence=example_sentence)
    db.session.add(new_word)
    db.session.commit()

    return jsonify(message="Word added successfully"), 201


@api.route('/get_word/<int:word_id>', methods=['GET'])
def get_word(word_id):
    word = Word.query.get(word_id)
    if word:
        return jsonify(id=word.id, word=word.word, definition=word.definition, example_sentence=word.example_sentence)
    else:
        return jsonify(message="Word not found"), 404


@api.route('/add_mastered_word', methods=['POST'])
@login_required
def add_mastered_word():
    data = request.get_json()
    user_id = data['user_id']
    word_id = data['word_id']

    new_mastered_word = MasteredWord(user_id=user_id, word_id=word_id)
    db.session.add(new_mastered_word)
    db.session.commit()

    return jsonify(message="Mastered word added successfully"), 201

# OpenAI-related route


@api.route('/test_openai_with_custom_prompt', methods=['POST'])
def test_openai_with_custom_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=1.5,
        )

        generated_text = response.choices[0].text.strip()
        return jsonify({"generated_text": generated_text})
    except Exception as e:
        print(e)
        return {"message": "Error connecting to OpenAI API"}, 500
