# TURB-Questions

This is a simple Flask app that uses the TURB API to generate questions from YouTube video captions.

To use the app, first install the necessary dependencies:
```bash
pip install flask flask-cors requests turb
```

Then, run the app:

```bash
python app.py
```

The app will be available at http://localhost:5000.

To generate a question, enter the YouTube video ID and the question in the form. The app will then generate a question based on the video captions.

For example, if you enter the YouTube video ID for "How to Make a Paper Airplane" and the question "What is the best way to fold a paper airplane?", the app will generate the following question:

What is the best way to fold a paper airplane that will fly the farthest?

You can also update the TURB API token by visiting the /update endpoint.

### Start command 
```gunicorn -c gunicorn.conf.py app:app```