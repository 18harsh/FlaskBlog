# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:20:55 2020

@author: Harsh
"""


from flaskblog import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)