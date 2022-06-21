import json
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, jwt_required, JWTManager

api = Flask(__name__)

api.config["JWT_SECRET_KEY"] = "fksgjdfgkjsnfdgk"
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(api)

@api.after_request
def refresh_expiring_jwts(response):
    response.cache_control.private = True
    response.cache_control.public = False
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            print("creating new token")
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

@api.route('/token', methods=["POST"])
def create_token():
    #todo: checar si quitar el none hace algo
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "mail" or password != "test":
        print(email, password)
        return {"msg": "Wrong email or password"}, 401

    # el token se esta creando con el email dentro
    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

@api.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    return response

@api.route('/profile')
@jwt_required()
def my_profile():
    response_body = {
        "name": "Santiago",
        "about": "soy sho",
        "email" :f"{get_jwt_identity()}",
    }
    jsonify(response_body)

    return response_body
if __name__ == '__main__':
    api.run(debug = True)
