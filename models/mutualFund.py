from db import db

class MutualFundModel( db.Model ):
    __tablename__ = "mutualFunds"

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 200 ) )

    def __init__( self, name ):
        self.name = name

    def json( self ):
        return { 'name': self.name }

    def saveToDb( self ):
        db.session.add( self )
        db.session.commit()

    def deleteFromDb( self ):
        db.session.delete( self )
        db.session.commit()

    @classmethod
    def findByName(cls, name):
        return cls.query.filter_by( name=name ).first()
