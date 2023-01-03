from database import Session, AdsModel, UserModel, Base
from pytest import fixture
import time
from auth import hash_password


@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()


@fixture()
def create_ads():
    with Session() as session:
        new_ads = AdsModel(heading=f'{time.time()}ads', description='example', user_id=1)
        session.add(new_ads)
        session.commit()
        return {
            'id': new_ads.id,
            'heading': new_ads.heading,
            'user_id': new_ads.user_id,
        }


@fixture()
def create_user():
    with Session() as session:
        new_user = UserModel(name=f'{time.time()}user_name',
                             email=f'{time.time()}user_email@bk.ru', password=hash_password('1234'))
        session.add(new_user)
        session.commit()
        return {
            'id': new_user.id,
            'name': new_user.name,
        }
