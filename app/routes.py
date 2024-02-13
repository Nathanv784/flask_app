from flask import request,jsonify
from app import db,app
from app.model import User,Note
# Define routes for CRUD operations on users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(users_list)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "username": user.username, "email": user.email})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify({"message": "User updated successfully"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    try:
        # Delete associated notes first
        Note.query.filter_by(user_id=user_id).delete()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User and associated notes deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})




# Define routes for CRUD operations on notes
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    new_note = Note(user_id=data['user_id'], title=data['title'], content=data['content'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "Note created successfully"}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    notes_list = [{"id": note.id, "user_id": note.user_id, "title": note.title, "content": note.content} for note in notes]
    return jsonify(notes_list)

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note is None:
        return jsonify({"message": "Note does not exist"}), 404
    else:
     return jsonify({"id": note.id, "user_id": note.user_id, "title": note.title, "content": note.content})

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    data = request.json
    note.title = data['title']
    note.content = data['content']
    db.session.commit()
    return jsonify({"message": "Note updated successfully"})

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted successfully"})