from database import engine, Base, Session, AdsModel
from pytest import fixture
import time


@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()


@fixture()
def create_ads():
    with Session() as session:
        new_ads = AdsModel(heading=f'{time.time()}ads')
        session.add(new_ads)
        session.commit()
        return {
            'id': new_ads.id,
            'heading': new_ads.heading
        }