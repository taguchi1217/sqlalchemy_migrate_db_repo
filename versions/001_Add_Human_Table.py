from sqlalchemy import *
from migrate import *

meta = MetaData()

human = Table('human' , meta,
                    Column('id',Integer,primary_key=True),
                    Column('firstName',String(32)),
                    Column('familyName',String(32))
                    )

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    human.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    human.drop()
