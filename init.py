from flask import Flask, request,jsonify

app= Flask(__name__)
    


@app.route('/video/details',methods=['POST'])
def endpoint_vdoDetails():
    if request.method=='POST':
        validation:dict={
            'video_id':'video_id' in request.json
        }
        if not all(validation.values()):
            return "Bad Request"+str(validation),400
        else: 
            return "Video Details"
        

@app.route('/channel/details',methods=['POST'])
def endpoint_channelDetails():
    if request.method=='POST':
        validation:dict={
            'channel_id':'channel_id' in request.json
        }
        if not all(validation.values()):
            return "Bad Request"+ str(validation),400
        else:
            return "channel Details"
        


@app.route('/video/comments',methods=['POST'])
def endpoint_vdoComments():
    
    if request.method=='POST':
        validation:dict={
            'video_id': 'video_id' in request.json,
            'count':'count' in request.json,
        }
        if not all(validation.values()):
            return "Bad Request\n"+str(validation),400
        else: 
            return "Video comments"


if __name__=='__main__':
    app.run()
    