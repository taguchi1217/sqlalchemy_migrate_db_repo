from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    human = Table('human', meta, autoload=True)
    age_col = Column('age', Integer)
    age_col.create(human)

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    human = Table('human', meta, autoload=True)
    human.c.age.drop()
