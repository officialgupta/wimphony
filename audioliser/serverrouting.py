import pdb
from flask import Flask, request,render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from models import db,User,SoundEntry
import random
from hello import create_and_save_wav

class urlnameloc(object):
	def __init__(self, url,name,loc):
		self.url=url
		self.name=name
		self.loc=loc



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
	display = SoundEntry.query.limit(5).all()
	returner=[]
	for record in display:
		x=urlnameloc(record.id,record.name,record.location)
		returner.append(x)
		
	return render_template('indextemplate.html', songlist=returner)
    
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
		userexists = User.query.filter_by().first()
		db.session.add(soundentryrecord)
		db.session.commit()
		create_and_save_wav([soundentryrecord.name],"static/"+str(soundentryrecord.id))
		return soundentryrecord.name
		
		
		

@app.route('/music', methods=['GET', 'POST'])
def music():
	if request.method == 'GET':
		field = request.args.get('field')
		q = request.args.get('q')
		
		if field=="all":
			display = SoundEntry.query.all()
			returner=""
			for record in display:
				returner=returner + "htpp://www.wimphony.com/static/" + str(record.id) +".wav,"
			return returner[:-1]
		elif field=="user":
			userid=Users.query.filter_by(username=q).first()
			if userid is None:
				return "none"
			display = SoundEntry.query.filter_by(user_id=userid)
			returner=""
			for record in display:
				returner=returner + "htpp://www.wimphony.com/static/" + str(record.id) +".wav,"
			return returner[:-1]
		elif field== "one":
			return "htpp://www.wimphony.com/static/" + str(random.choice(SoundEntry.query.all()).id) +".wav"
			
@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename)



if __name__ == "__main__":
	app.run()
