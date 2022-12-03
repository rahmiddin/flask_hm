from flask.views import MethodView
from database import Session, AdsModel
from flask import jsonify, request
from errors import ApiException


class AdsView(MethodView):
    def get(self, ads_id: int):
        with Session() as session:
            ads = session.query(AdsModel).get(ads_id)
            if ads is None:
               raise ApiException(404, 'user not found')
            return jsonify(
                {'id': ads.id,
                 'heading': ads.heading,
                 'create_date': ads.create_date
                 }
            )

    def post(self):
        ads_data = request.json
        with Session() as session:
            new_ads = AdsModel(**ads_data)
            session.add(new_ads)
            session.commit()
            return jsonify({'id': new_ads.id, 'heading': new_ads.heading})

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


