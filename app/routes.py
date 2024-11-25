from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/triagem', methods=['POST'])
def triagem():
    data = request.json
    # Processar dados
    return jsonify(data)


@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@main.route('/activities', methods=['POST'])
def create_activity():
    data = request.json
    new_activity = Activity(name=data['name'], type=data['type'], duration=data['duration'], user_id=data['user_id'])
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({"message": "Activity created"}), 201
