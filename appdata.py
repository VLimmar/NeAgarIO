import sqlalchemy as sql
import sqlalchemy.orm as orm


base = orm.declarative_base()
session = orm.sessionmaker()


class Data(base):
    __tablename__ = "Balls"
    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(16))
    score = sql.Column(sql.Integer)


engine = sql.create_engine("sqlite:///Data_file.db")
base.metadata.create_all(engine)