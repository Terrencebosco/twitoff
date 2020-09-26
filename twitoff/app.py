from flask import Flask

def CreateApp():
    '''create application functions'''
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return 'hello world'
    
    return app              
