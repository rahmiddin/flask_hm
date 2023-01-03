from flask.views import MethodView
from database import Session, AdsModel, UserModel
from flask import jsonify, request
from errors import ApiException
from auth import hash_password


class AdsView(MethodView):
    def get(self, ads_id: int):
        with Session() as session:
            ads = session.query(AdsModel).get(ads_id)
            if ads is None:
               raise ApiException(404, 'ads not found')
            return jsonify(
                {'id': ads.id,
                 'heading': ads.heading,
                 'create_date': ads.create_date,
                 }
            )

    def post(self):
            ads_data = request.json
            with Session() as session:
                new_ads = AdsModel(**ads_data)
                session.add(new_ads)
                session.commit()
                return jsonify({'id': new_ads.id, 'heading': new_ads.heading, 'user_id': new_ads.user_id})

    def patch(self, ads_id: int):
        ads_data = request.json
        with Session() as session:
            ads = session.query(AdsModel).get(ads_id)
            for field, value in ads_data.items():
                setattr(ads, field, value)
            session.add(ads)
            session.commit()
            return jsonify({'id': ads.id})

    def delete(self, ads_id: int):
        with Session() as session:
            ads = session.query(AdsModel).get(ads_id)
            session.delete(ads)
            session.commit()
            return jsonify({'status': 'deleted'})


class UserView(MethodView):
    def post(self):
        user_data = request.json
        user_data['password'] = hash_password(user_data['password'])
        with Session() as session:
            new_user = UserModel(**user_data)
            session.add(new_user)
            session.commit()
            return jsonify({'id': new_user.id, 'name': new_user.name})

    def get(self, user_id: int):
        with Session() as session:
            user = session.query(UserModel).get(user_id)
            if user is None:
               raise ApiException(404, 'user not found')
            return jsonify(
                {'id': user.id,
                 'name': user.name,
                 }
            )


def login():
    login_data = request.json
    with Session() as session:
        user = {
            session.query(UserModel).filter(UserModel.name == login_data["name"]).first()
        }
        if user is None or not user.check_password()