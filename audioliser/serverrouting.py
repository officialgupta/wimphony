import pdb
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import db,User,SoundEntry
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'GET':
		
		usernam = request.args.get('user')
		location = request.args.get('location')
		strength = request.args.get('strength')
		name = request.args.get('name')
		
		userexists = User.query.filter_by(username=usernam).first()
		
		if userexists is None:
			userrecord=User(usernam)
			db.session.add(userrecord)
			db.session.commit()
			userexists = User.query.filter_by(username=usernam).first()
			
		identry=userexists.id
			
		
		
		
		soundentryrecord=SoundEntry(identry,location,strength,name)
		db.session.add(soundentryrecord)
		db.session.commit()
		return "success!"
		#TODO lookup user_ID and use that
		
		

@app.route('/music', methods=['GET', 'POST'])
def music():
	if request.method == 'GET':
		field = request.args.get('field')
		q = request.args.get('q')
		
		if field=="all":
			display = SoundEntry.query.all()
			returner=""
			for record in display:
				returner= returner+"<p>"+record.name+"</p> "
			return returner		



if __name__ == "__main__":
	app.run()
