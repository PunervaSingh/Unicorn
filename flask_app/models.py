from enum import unique
from datetime import date
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_app import db, login_manager,app
from flask_login import UserMixin
# from sqlalchemy.dialects.postgresql import ARRAY

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean , default= False)
    position = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    profile_pic = db.Column(db.String(), nullable=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    validated = db.Column(db.Boolean , default= False)
    open_to_work = db.Column(db.String(10))
    mentor = db.Column(db.Integer)
    requested = db.Column(db.Boolean , default= False)
    assigned = db.Column(db.Boolean , default= False)
    # village_based = db.Column(db.Boolean , default= False)
    # tier_based = db.Column(db.Boolean , default= False)
    # location = db.Column(db.String(100))

    # project = db.relationship('Projects',backref='user',lazy=True)
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Programs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000))
    country = db.Column(db.String(50), nullable=False)
    industry = db.Column(db.String(10))
    user = db.Column(db.String(10))
    link = db.Column(db.String(200))
    status = db.Column(db.String(200))
    pic = db.Column(db.String(120), nullable=False, default='https://images.unsplash.com/photo-1562654501-a0ccc0fc3fb1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2832&q=80')

    def __repr__(self):
        return f"Program('{self.name}','{self.description}','{self.country}','{self.industry}','{self.user}','{self.link}','{self.status}')"
    

class MentorCounsellor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    year = db.Column(db.Integer, nullable= False)
    project = db.Column(db.Integer)
    cost = db.Column(db.Integer, nullable= False)
    choice = db.Column(db.String(100),nullable=False)
    expertise = db.Column(db.String(100),nullable=False)
    # past_projects = db.Column(ARRAY(str))
    # current_projects = db.Column(ARRAY(str))
    profile = db.Column(db.String(100), unique=True)
    availability = db.Column(db.Integer , default= False)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')

    def __repr__(self):
        return f"Order('{self.user}','{self.year}','{self.cost}','{self.choice}','{self.expertise}','{self.profile}','{self.availability}')"
    

class Validator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    profile = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')

    def __repr__(self):
        return f"Order('{self.user}','{self.profile}','{self.name}','{self.phone}','{self.email}','{self.pic}')"
    
class Legal_Advisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    name = db.Column(db.String(20), nullable=False)
    profile = db.Column(db.String(100), unique=True)
    year = db.Column(db.Integer, nullable= False)
    role = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    awards = db.Column(db.Integer, nullable= False)
    cases = db.Column(db.Integer, nullable= False)
    advised = db.Column(db.Integer, nullable= False)
    union = db.Column(db.Integer, nullable= False)
    description = db.Column(db.String(150), nullable=False)
    request = db.Column(db.Boolean , default= False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')

    def __repr__(self):
        return f"Order('{self.user}','{self.profile}','{self.name}','{self.phone}','{self.email}','{self.pic}')"
    

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    mentor = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    idea = db.Column(db.String(150), nullable=False)
    validated = db.Column(db.Boolean , default= False)
    extra = db.Column(db.String(150))
    category = db.Column(db.String(15), nullable=False)
    industry = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    village = db.Column(db.Boolean , default=False)
    tier = db.Column(db.Boolean , default=False)
    women = db.Column(db.Boolean , default=False)
    rnd = db.Column(db.Integer)
    administration = db.Column(db.Integer)
    marketing = db.Column(db.Integer)
    profit = db.Column(db.Integer)
    pic = db.Column(db.String(120), nullable=False, default='https://images.unsplash.com/photo-1550305080-4e029753abcf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2071&q=80')
    
    def __repr__(self):
        return f"Order('{self.user}','{self.profile}','{self.name}','{self.phone}','{self.email}','{self.pic}','{self.idea}','{self.validated}','{self.extra}','{self.category}','{self.industry}','{self.country}','{self.village}','{self.tier}','{self.women}')"
    
class Funding_Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    name = db.Column(db.String(20), nullable=False)
    profile = db.Column(db.String(100), unique=True)
    country = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    investment = db.Column(db.Integer, nullable= False)
    role = db.Column(db.String(15), nullable=False)
    open_to = db.Column(db.String(20), nullable=False)
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    
    def __repr__(self):
        return f"Order('{self.description}','{self.investment}','{self.role}','{self.open_to}','{self.user}','{self.profile}','{self.name}','{self.phone}','{self.email}','{self.country}')"
    

class Linkage_Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    link = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    service = db.Column(db.String(25), nullable=False)
    open_to = db.Column(db.String(20), nullable=False)
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    
    def __repr__(self):
        return f"Order('{self.description}','{self.state}','{self.service}','{self.open_to}','{self.user}','{self.link}','{self.name}','{self.phone}','{self.email}','{self.country}')"


class Advertisement_Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(30), unique=True)
    country = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    service = db.Column(db.String(25), nullable=False)
    availability = db.Column(db.String(20), nullable=False)
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    
    def __repr__(self):
        return f"Order('{self.state}','{self.service}','{self.user}','{self.name}','{self.phone}','{self.email}','{self.country}')"
    
class Positions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer,db.ForeignKey('project.id'), nullable= False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    project_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    job_title = db.Column(db.String(20), nullable=False)
    job_description = db.Column(db.String(250), nullable=False)
    number_open = db.Column(db.Integer, nullable= False)
    duration = db.Column(db.String(20), nullable=False)
    stipend = db.Column(db.Integer, nullable= False)
    paid_unpaid = db.Column(db.String(20), nullable=False)
    inoffice_wfh = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    total_workforce = db.Column(db.Integer)
    female_workforce = db.Column(db.Integer)
    category_workforce = db.Column(db.Integer)
    pic = db.Column(db.String(120), nullable=False, default='https://images.unsplash.com/photo-1550305080-4e029753abcf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2071&q=80')

    def __repr__(self):
        return f"Order('{self.inoffice_wfh}','{self.location}','{self.phone}','{self.email}','{self.user_id}','{self.project_id}','{self.name}','{self.job_title}','{self.job_description}','{self.link}','{self.number_open}','{self.duration}','{self.stipend}','{self.paid_unpaid}')"
    
class Open_to_work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    name = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10))
    linkedin_link = db.Column(db.String(200))
    portfolio_link = db.Column(db.String(200))
    resume_link = db.Column(db.String(200))
    year_of_experience = db.Column(db.Integer, nullable= False)
    about = db.Column(db.String(5000))
    profession = db.Column(db.String(100), nullable=False)
    relocate = db.Column(db.String(15))
    past_experience = db.Column(db.String(200))
    projects = db.Column(db.String(500), nullable=False)
    courses = db.Column(db.String(500))
    pic = db.Column(db.String(120), nullable=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')

    def __repr__(self):
        return f"Program('{self.courses}','{self.projects}','{self.past_experience}','{self.about}','{self.user_id}','{self.gender}','{self.profession}','{self.linkedin_link}','{self.year_of_experience}','{self.resume_link}','{self.portfolio_link}')"
    

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    recipient_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    project_id = db.Column(db.Integer,db.ForeignKey('project.id'))
    message = db.Column(db.String(500), nullable= False)
    category = db.Column(db.String(20), nullable= False)
    gender = db.Column(db.String(20), nullable= False)
    portfolio_link = db.Column(db.String(500))

    def __repr__(self):
        return f"Program('{self.user_id}','{self.recipient_id}','{self.message}')"

class Trending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable= False)
    desc = db.Column(db.String(2500), nullable= False)
    country = db.Column(db.String(100), nullable= False)
    link = db.Column(db.String(500))

    def __repr__(self):
        return f"Program('{self.name}','{self.desc}','{self.country}','{self.link}')"

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(100), nullable= False)
    phone = db.Column(db.String(100), nullable= False) 
    customization = db.Column(db.String(500), nullable= False)
    address = db.Column(db.String(100), nullable= False)
    item = db.Column(db.String(100), nullable= False)
    msg = db.Column(db.String(900), nullable= False)

    def __repr__(self):
        return f"Program('{self.name}','{self.customization}','{self.address}','{self.item}','{self.phone}','{self.email}','{self.msg}')"