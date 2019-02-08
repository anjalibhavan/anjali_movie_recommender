import os
#<!--<li display='inline'>{{ row.Index, row['name'] }}<img src="{{row['poster']}}" style="width:40px;height:40px;"> </li>-->

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'