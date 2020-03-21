from flask_restful import Resource, reqparse
from models.goal import GoalModel

class Goal(Resource):
    def get( self, name ):
        goal = GoalModel.findByName( name )
        if goal:
            return goal.json()
        return( { 'msg':
                  'Sorry, {} goal is not present. Please consider adding it.'.format(name) }, 404 )

    def post( self, name ):
        goal = GoalModel.findByName( name )
        if goal:
            return { "msg": "{} goal already exists." }
        goal = GoalModel( name )
        try:
            goal.saveToDb()
            return goal.json()
        except:
            return { "message": "An error occured inserting the goal" }, 500
