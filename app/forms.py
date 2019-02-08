from flask_wtf import FlaskForm
from wtforms import IntegerField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

mychoices=[(0,'Home Alone'),(1,'Breathe In'), (2 ,'Finding Nemo'), (3 ,'Room'), (4,'Still Alice'),(5,'Gone Girl') ,(6,'Godzilla'),(7,'The Reader'),
        (8,'Anna Karenina'), (9,'The Shawshank Redemption'),(10,'Fight Club'),(11,'The Prodigy'),(12,'The Conjuring'),(13,'The Vow'),
        (14,'The Departed'),(15,'Casablanca'),(16,'Atonement'),(17,'Aquaman'),(18,'Toy Story'),(19,'Notorious'),(20,'Spellbound'),
        (21,'Gone with the Wind'),(22,'The Parent Trap'),(23,'Spectre'),(24,'Psycho'),(25,'The Guns of Navarone'),(26,'Spotlight'),
        (27,'The Godfather'),(28,'Before Sunrise'),(29,'Before Sunset'),(30,'Before Midnight'),(31,'The Social Network'),(32,'Pulp Fiction'),
        (33,'Forrest Gump'),(34,'Sleepless in Seattle'),(35,'Notting Hill'),(36,'Inception'),(37,'The Prestige'),(38,'Goodfellas'),(39,'Interstellar'),
        (40,'La La Land '),(41,'Django Unchained'),(42,'Whiplash'),(43,'The Help'),(44,'American Beauty'),(45,'Vertigo'),(46,'M'),(47,'Gladiator'),
        (48,'Spartacus'),(49,'Troy'),(50,'Jackie'),(51,'Memento'),(52,'Coco'),(53,'Up'),(54,'It'),(55,'Taxi Driver'),(56,'The Martian'),
        (57,'Good Will Hunting'),(58,'Andhadhun'),(59,'Die Hard'),(60,'Heat'),(61,'Ikiru'),(62,'Ran'),(63,'Chinatown'),(64,'A Beautiful Mind'),
        (65,'Anbe Sivam'),(66,'Gandhi'),(67,'Drishyam'),(68,'PK'),(69,'Bohemian Rhapsody'),(70,'Vice'),(71,'Birdman'),(72,'Ferdinand'),
        (73,'A Quiet Place'),(74,'Black Panther'),(75,'Tag'),(76,'Rent'),(77,'After'),(78,'Disobedience'),(79,'Destroyer'),(80,'Columbus'),
        (81,'Bright Star'),(82,'Aviator'),(83,'Avatar'),(84,'Thor'),(85,'Sin'),(86,'Superman'),(87,'Titans'),(88,'Lucy'),(89,'Hamlet'),
        (90,'Adrift'),(91,'Thelma'),(92,'Chicago'),(93,'Paterson'),(94,'Loving Vincent'),(95,'Finding Fanny'),(96,'Mimicry'),(97,'Breathe'),
        (98,'Closer'),(99,'The Holiday'),(100,'The Revenant'),(101,'Ocean Girl')]


class RecoForm(FlaskForm):
    movie1 = SelectField('Movie 1', coerce=int, choices=mychoices)
    ratings1 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie2 = SelectField('Movie 2', coerce=int,choices=mychoices)
    ratings2 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie3 = SelectField('Movie 3', coerce=int,choices=mychoices)
    ratings3 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie4 = SelectField('Movie 4', coerce=int,choices=mychoices)
    ratings4 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie5 = SelectField('Movie 5', coerce=int,choices=mychoices)
    ratings5 = IntegerField('Rating', validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    submit = SubmitField('Submit')

    '''
    ,NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')]
,NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')]
,NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')]
,NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')]
,NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')]
    '''