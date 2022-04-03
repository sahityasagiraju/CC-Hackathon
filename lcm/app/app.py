from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class LCM(Resource):
    def get(self, n1, n2):
    	n1 = float(n1)
    	n2 = float(n2)
    	if(n1 > n2):
    		greater = n1
    	else:
    		greater = n2
    	while(True):
    		if((greater % n1 == 0) and (greater % n2 == 0)):
    			lcm = greater
    			break
    		greater += 1
    	return {'ans': lcm}

api.add_resource(LCM, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )
