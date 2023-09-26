''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from  EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the anger,disgust,joy,
        sadness,fear scores and dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return f'''For the given statement, the system response is
    'anger':{res['anger']},'disgust': {res['disgust']}, 
    'fear': {res['fear']}, 'joy': {res['joy']} and 
    'sadness': {res['sadness']},The dominant emotion is 
    {res['dominant_emotion']}.'''

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
