from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/download", methods=['POST'])
def download():
    request_data = request.get_json()
    link = request_data['link']
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        return {
            "status": "OK",
            "url": youtubeObject.url
        }
    except:
        return {
            "status": "Error",
            "message": 'An error has download video'
        }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)    


"""
POST: http://127.0.0.1:8001/download
{
    "link": "https://www.youtube.com/watch?v=C-uICquhs04&list=RDC-uICquhs04&start_radio=1"
}
"""