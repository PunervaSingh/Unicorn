from flask_app import app
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, make_response, abort, current_app, jsonify
from flask_app.forms import RegistrationForm, LoginForm, Add_Mentor_Counsellor_Form, Add_Validator_Form, Add_Legal_Advisor, Add_Project, Add_Funding_Agent, Add_Linkage_Agent, Add_Advertisement_Agent, Add_Position, Add_Open_Work, UpdateAccountForm, ResetPasswordForm, Validate_Project, Mentor_Project, Mentor_Request, Job_Apply, BulkMail, Add_Gift, Brand_Name, Update_Mentor_Detail, Update_Validator_Detail, Update_Linkage_Agent, Update_Advertiser_Detail, Update_Funding_Detail, Update_Legal_Detail, Update_Seeker_Detail, Update_Position_Detail, Update_Project_Detail, Profit_Projection, PostForm, CommentForm, Google_Assistant, Ad_recommend, Accelerator_Form, Event_Form, Add_Volunteer, Test_Form, Challenges
from flask_app.models import Programs, User, MentorCounsellor, Validator, Legal_Advisor, Project, Funding_Agent, Linkage_Agent, Advertisement_Agent, Positions, Open_to_work, Notification, Trending, Gift, Post, Comment, PostLike, CommentLike, Survey, Accelerator, Tasks, Volunteer, Volunteer_test, challenges, Applicants
from flask_login import login_user, current_user, logout_user, login_required
from flask_app import db, bcrypt, admin, mail
from flask_admin.contrib.sqla import ModelView
from flask_app.decorators import admin_required
from flask_mail import Message
from werkzeug.utils import secure_filename
from datetime import datetime
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
import uuid as uuid
import os
from wtforms import Form
import json
# import numpy as np
import pandas as pd
import matplotlib
import sqlite3
from datetime import date
# import seaborn as sns
# import matplotlib.pyplot as plt
import pickle
from pytrends.request import TrendReq
import plotly.express as px
import plotly.io as pio
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from newsapi import NewsApiClient

from urllib.request import urlopen, Request
import re
from bs4 import NavigableString
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
# import sklearn

# to run google assitant,run this command first in terminal - export GOOGLE_CLOUD_PROJECT=project_id

model = pickle.load(open("/Users/punerva/Downloads/Unicorn/flask_app/model.pkl", 'rb'))
success = pickle.load(open("/Users/punerva/Downloads/Unicorn/flask_app/success.pkl", 'rb'))
adata = pd.read_csv("/Users/punerva/Downloads/Unicorn/flask_app/cleaned_ads.csv")

app.config['UPLOAD_FOLDER'] = '/Users/punerva/Downloads/Unicorn/flask_app/static/img'
app.config['POSTS_PER_PAGE'] = 9
app.config['FLASKY_COMMENTS_PER_PAGE'] = 9

newsapi = NewsApiClient(api_key='1fbd54d2120045e38407d63aefde016c')

@app.route('/', methods=('GET', 'POST'))
@app.route('/home/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        if(current_user.position=='StartUp'):
            mentor_id = request.form.get('mentor')
            project_id = request.form.get('project')
            print(mentor_id)
            print(project_id)
            project = Project.query.get_or_404(project_id)
            user = User.query.get_or_404(current_user.id)
            mentor_requested = User.query.get_or_404(mentor_id)
            project.mentor = mentor_id
            user.mentor = mentor_id
            user.assigned = True
            mentor_requested.requested = False
            db.session.commit()

            # Mail
            msg = Message("(Trial Run) Unicorn: Acceptance of your mentorship request",
            sender="phoenix.we9574@gmail.com",
            recipients=["punerva045btcsai20@igdtuw.ac.in"])
            # recipients=[mentor_requested.email])

            msg.body = '''Your request for mentoring project of the user(%s) was accepted. Visit your profile page to know more.
            '''%(current_user.name)
            mail.send(msg)
            return redirect(url_for('idea_validation'))
        else:
            user_id = request.form.get('mentor')
            project_id = request.form.get('project')
            current_user.assigned=True
            user = User.query.get_or_404(user_id)
            user.mentor=current_user.id
            project = Project.query.get_or_404(project_id)
            project.mentor=current_user.id
            user.requested = False
            db.session.commit()

            # Mail
            msg = Message("(Trial Run) Unicorn: Acceptance of your mentorship request",
            sender="phoenix.we9574@gmail.com",
            recipients="phoenix.we9574@gmail.com")
            # recipients=[user.email])

            msg.body = '''Your request for mentor - %s was accepted. Visit your profile page to know more.
            '''%(current_user.name)
            mail.send(msg)

            return redirect(url_for('idea_validation'))
    if current_user.is_authenticated:
        notification = Notification.query.all()
        return render_template("home.html", notification=notification)
    return render_template("home.html")

@app.route('/options')
@login_required
def options():
    return render_template("options.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.position:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('options'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, phone=form.phone.data, address=form.address.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():    
    if current_user.is_authenticated:
        if current_user.position:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('options'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('profile', user_id=current_user.id)) if user.position else redirect(url_for('options'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/admin", methods=['GET', 'POST'])
@login_required
@admin_required
def adminfunc():
    pass
class myModelView(ModelView):
    # edit_template = 'edit_user.html'
    # create_template = 'create_user.html'
    list_template = 'list_user.html'
    def is_accessible(self):
        return (current_user.is_admin==True)
    
admin.add_view(myModelView(User,db.session))
admin.add_view(myModelView(Programs,db.session))
admin.add_view(myModelView(MentorCounsellor,db.session))
admin.add_view(myModelView(Validator,db.session))
admin.add_view(myModelView(Legal_Advisor,db.session))
admin.add_view(myModelView(Project,db.session))
admin.add_view(myModelView(Funding_Agent,db.session))
admin.add_view(myModelView(Linkage_Agent,db.session))
admin.add_view(myModelView(Advertisement_Agent,db.session))
admin.add_view(myModelView(Positions,db.session))
admin.add_view(myModelView(Open_to_work,db.session))
admin.add_view(myModelView(Trending,db.session))

@app.route('/women_entrepreneur', methods=['GET', 'POST'])
@login_required
def women_entrepreneur():
    origin = request.args.get('country')
    indus_type = request.args.get('industry')
    user_type = request.args.get('user')
    # s = request.args.get('staus')
    q = request.form.getlist('options')
    if q:
        if q==['Ongoing']:
            # projects = Project.query.filter(Project.women)
            programs = Programs.query.filter(Programs.status=='Ongoing')
        else:
            programs = Programs.query.filter(Programs.status=='Completed')
    elif origin:
        programs = Programs.query.filter(Programs.country.contains(origin))
    elif indus_type:
        programs = Programs.query.filter(Programs.industry.contains(indus_type))
    elif user_type:
        programs = Programs.query.filter(Programs.user.contains(user_type))
    else:
        programs=Programs.query.all()
    return render_template("women_entrepreneur.html", programs=programs)

@app.route('/idea_generation', methods=['GET', 'POST'])
@login_required
def idea_generation():
    form = Add_Project() 
    if form.validate_on_submit():
        project = Project(
            user = current_user.id, 
            email = current_user.email,
            name = form.name.data,
            phone = current_user.phone, 
            idea = form.idea.data,
            profile = form.profile.data,
            extra = form.extra.data,
            category = form.category.data,
            industry = form.industry.data,
            country = form.country.data,
            village = form.village.data,
            tier = form.tier.data,
            women = form.women.data,
        )

        project.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(project.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        project.pic = pic_name


        db.session.add(project)
        current_user.position = 'StartUp'
        db.session.commit()
        return redirect(url_for('idea_validation'))
    return render_template("idea_generation.html", form=form)

@app.route('/idea_validation', methods=['GET', 'POST'])
@login_required
def idea_validation():
    indus_type = request.form.get('industry')
    project_type = request.form.getlist('project_type')
    origin = request.form.get('origin')
    validation_status = request.form.getlist('validation_status')
    if indus_type and project_type and origin and validation_status:
        if project_type==['Product'] and validation_status==['Validated']:
            projects = Project.query.filter(Project.category=='Product' and Project.validated==1 and Project.industry.contains(indus_type) and Project.country.contains(origin))
        elif project_type==['Product'] and validation_status==['NotValidated']:
            projects = Project.query.filter(Project.category=='Product' and Project.validated==0 and Project.industry.contains(indus_type) and Project.country.contains(origin))
        elif project_type==['Service'] and validation_status==['Validated']:
            projects = Project.query.filter(Project.category=='Service' and Project.validated==1 and Project.industry.contains(indus_type) and Project.country.contains(origin))
        else:
            projects = Project.query.filter(Project.category=='Service' and Project.validated==0 and Project.industry.contains(indus_type) and Project.country.contains(origin))
    if indus_type:
        projects = Project.query.filter(Project.industry.contains(indus_type))
    elif project_type:
        if project_type==['Product']:
            projects = Project.query.filter(Project.category=='Product')
        elif project_type==['Service']:
            projects = Project.query.filter(Project.category=='Service')
    elif origin:
        projects = Project.query.filter(Project.country.contains(origin))
    elif validation_status:
        if validation_status==['Validated']:
            projects = Project.query.filter(Project.validated==1)
        else:
            projects = Project.query.filter(Project.validated==0)
    else:
        projects = Project.query.all()
    return render_template("idea_validation.html", projects=projects)

@app.route('/individual_idea/<int:project_id>', methods=['GET', 'POST'])
@login_required
def individual_idea(project_id):
    project = Project.query.get_or_404(project_id)
    # mentor = MentorCounsellor.query.get_or_404(current_user.id)
    if current_user.position == 'Validator':
        form = Validate_Project() 
        if form.validate_on_submit():
            project.validated=1
            db.session.commit()
            return redirect(url_for('idea_validation'))
        return render_template("individual_idea.html", project=project, form=form)
    if current_user.position == 'Mentor':
        form = Mentor_Project() 
        if form.validate_on_submit():
            notification = Notification(
                user_id = current_user.id, 
                recipient_id = project.user,
                project_id = project.id,
                message = f'''A mentor wants to mentor your startup idea. Click on the following link to visit his/her profile: '''
            )
            db.session.add(notification)
            current_user.requested = 1
            db.session.commit()

            # Mail
            msg = Message("Unicorn: Mentor's request on your StartUp",
            sender="phoenix.we9574@gmail.com",
            recipients=["phoenix.we9574@gmail.com"])
            # recipients=[project.email])

            msg.body = '''A mentor wants to mentor your startup idea. 
            Below are the details of the mentor:
                    
            Name of member: %s
            Email address: %s
            Contact No: %s
            '''%(current_user.name, current_user.email, current_user.phone)
            mail.send(msg)

            return redirect(url_for('idea_validation'))
        return render_template("individual_idea.html", project=project, form=form)
    return render_template("individual_idea.html", project=project)

@app.route('/mentorship_counsellor', methods=['GET', 'POST'])
@login_required
def mentorship_counsellor():
    q = request.form.getlist('options')
    if q==['mentor']:
        mentors = MentorCounsellor.query.filter(MentorCounsellor.choice=='Mentor')
    elif q==['counsellor']:
        mentors = MentorCounsellor.query.filter(MentorCounsellor.choice=='Counsellor') 
    else:
        mentors = MentorCounsellor.query.all()
    users = User.query.all()
    projects = Project.query.all()
    form = Mentor_Request() 
    if form.validate_on_submit():
        notification = Notification(
            user_id = current_user._get_current_object(), 
            recipient_id = request.form['text'],
            project_id = request.form['txt'],
            message = f'''A startUp wants you to be their mentor. Click on the following link to visit project link: '''
        )
        db.session.add(notification)
        current_user.requested = 1
        db.session.commit()

        # Mail
        msg = Message("Unicorn: StartUp requesting for your mentorship",
        sender="phoenix.we9574@gmail.com",
        recipients=["phoenix.we9574@gmail.com"])

        msg.body = '''A startUp wants you to be their mentor. 
        Click on the following link to visit project link:
                
        Project Link: http://127.0.0.1:5000/profile/%s
        '''%(request.form['txt'])
        mail.send(msg)

        return redirect(url_for('home'))
    return render_template("mentor_counsellor.html", mentors=mentors, projects=projects, form=form, users=users)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/books', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/mentorship_counsellor_apply', methods=['GET', 'POST'])
@login_required
def mentorship_counsellor_apply():
    form = Add_Mentor_Counsellor_Form() 
    if form.validate_on_submit():
        # image_f = save_picture(form.image_file.data)
        mentor = MentorCounsellor(
            pic = current_user.profile_pic, 
            name = current_user.name,
            email = current_user.email,
            phone = current_user.phone, 
            user = current_user.id, 
            year = form.year.data,
            cost = form.cost.data,
            profile = form.profile.data,
            availability = form.availability.data,
            expertise = form.expertise.data,
            choice = form.choice.data
        )

        mentor.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(mentor.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        mentor.pic = pic_name

        db.session.add(mentor)
        current_user.position = form.choice.data
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('mentorship_counsellor_apply'))
    return render_template("mentor_counsellor_apply.html", form=form)

@app.route('/validator_apply', methods=['GET', 'POST'])
@login_required
def validator_apply():
    form = Add_Validator_Form() 
    if form.validate_on_submit():
        # image_f = save_picture(form.image_file.data)
        validator = Validator(
            pic = current_user.profile_pic, 
            name = current_user.name,
            email = current_user.email,
            phone = current_user.phone, 
            user = current_user.id, 
            profile = form.profile.data
        )

        validator.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(validator.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        validator.pic = pic_name

        db.session.add(validator)
        current_user.position = 'Validator'
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('validator_apply'))
    return render_template("validator_apply.html", form=form)

@app.route('/legal_advisor_apply', methods=['GET', 'POST'])
@login_required
def legal_advisor_apply():
    form = Add_Legal_Advisor() 
    if form.validate_on_submit():
        advisor = Legal_Advisor(
            pic = current_user.profile_pic, 
            name = current_user.name,
            email = current_user.email,
            phone = current_user.phone, 
            user = current_user.id, 
            profile = form.profile.data,
            description = form.description.data,
            city = form.city.data,
            country = form.country.data,
            role = form.role.data,
            awards = form.awards.data,
            cases = form.cases.data,
            advised = form.advised.data,
            union = form.union.data,
            year = form.year.data,
        )

        advisor.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(advisor.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        advisor.pic = pic_name

        db.session.add(advisor)
        current_user.position = 'Legal Advisor'
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('legal_issues'))
    return render_template("legal_advisor_apply.html", form=form)

@app.route('/legal_issues')
@login_required
def legal_issues():
    advisors = Legal_Advisor.query.all()
    return render_template("legal_issues.html", advisors=advisors)

@app.route('/tierI_tierII_villages', methods=['GET', 'POST'])
@login_required
def tierI_tierII_villages():
    q = request.form.getlist('options')
    if q==['women']:
        projects = Project.query.filter(Project.women)
    elif q==['tier']:
        projects = Project.query.filter(Project.tier)
    elif q==['village']:
        projects = Project.query.filter(Project.village)
    else:
        projects = Project.query.filter(Project.village==True or Project.women==True or Project.tier==True)
    return render_template("tierI_village.html", projects=projects)

@app.route('/raw_material')
@login_required
def raw_material():
    return render_template("raw_material.html")

@app.route('/linkage_agent_apply', methods=['GET', 'POST'])
@login_required
def linkage_agent_apply():
    form = Add_Linkage_Agent() 
    if form.validate_on_submit():
        advisor = Linkage_Agent(
            user = current_user.id, 
            name = form.name.data,
            email = form.email.data,
            phone = form.phone.data, 
            link = form.link.data,
            description = form.description.data,
            country = form.country.data,
            state = form.state.data,
            service = form.service.data,
            open_to = form.open_to.data,
            pic = current_user.profile_pic, 
        )

        advisor.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(advisor.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        advisor.pic = pic_name

        db.session.add(advisor)
        current_user.position = 'Linkage Agent'
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('linkage_agent'))
    return render_template("linkage_agent_apply.html", form=form)

@app.route('/linkage_agent', methods=['GET', 'POST'])
@login_required
def linkage_agent():
    places = request.args.get('places')
    if places:
        agents = Linkage_Agent.query.filter(Linkage_Agent.country.contains(places) |
        Linkage_Agent.state.contains(places))
    else:
        agents = Linkage_Agent.query.all()
    return render_template("linkage_agent.html", agents=agents)

@app.route('/team_building_hiring', methods=['GET', 'POST'])
@login_required
def team_building_hiring():
    form = Job_Apply() 
    q = request.form.getlist('options')
    if q==['people']:
        open = Open_to_work.query.all()
        return render_template("team_hiring.html", open=open, form=form)
    elif q==['startups']:
        positions = Positions.query.all()
        return render_template("team_hiring.html", positions=positions, form=form)
    else:
        positions = Positions.query.all()
    if form.validate_on_submit():
        notification = Notification(
            recipient_id = request.form['text'],
            user_id = request.form['txt'],
            portfolio_link = form.portfolio_link.data,
            category = form.category.data,
            gender = form.gender.data,
            message = '''A person applied for job position provided by you. Details are as follows: 
            Category: %s
            Gender: %s
            Click on the following links to visit portfolio and profile pages of the individual: '''%(form.category.data, form.gender.data)
        )
        db.session.add(notification)
        db.session.commit()

        # Mail
        msg = Message("Unicorn: Applicant on your job application",
        sender="phoenix.we9574@gmail.com",
        recipients=["phoenix.we9574@gmail.com"])

        msg.body = '''A person applied for job position provided by you. Details are as follows: 
            Category: %s
            Gender: %s
        Visit Unicorn site to see profile or click on the following links to visit portfolio of the individual:
                
        Portfolio Link: %s
        '''%(form.category.data, form.gender.data, form.portfolio_link.data)
        mail.send(msg)
        return redirect(url_for('home'))
    return render_template("team_hiring.html", positions=positions, form=form)

@app.route('/advertisement_agent_apply', methods=['GET', 'POST'])
@login_required
def advertisement_agent_apply():
    form = Add_Advertisement_Agent() 
    if form.validate_on_submit():
        advertiser = Advertisement_Agent(
            user = current_user.id, 
            name = current_user.name,
            email = current_user.email,
            phone = current_user.phone, 
            city = form.city.data,
            country = form.country.data,
            state = form.state.data,
            service = form.service.data,
            availability = form.availability.data,
            pic = current_user.profile_pic, 
        )

        advertiser.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(advertiser.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        advertiser.pic = pic_name

        db.session.add(advertiser)
        current_user.position = 'Advertisement Agent'
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('advertisement'))
    return render_template("advertisement_agent_apply.html", form=form)

@app.route('/advertisement', methods=['GET', 'POST'])
@login_required
def advertisement():
    places = request.args.get('places')
    if places:
        advertisers = Advertisement_Agent.query.filter(Advertisement_Agent.country.contains(places) |
        Advertisement_Agent.state.contains(places) | Advertisement_Agent.city.contains(places))
    else:
        advertisers = Advertisement_Agent.query.all()
    return render_template("advertisement.html", advertisers=advertisers)

@app.route('/funding_agent_apply', methods=['GET', 'POST'])
@login_required
def funding_agent_apply():
    form = Add_Funding_Agent() 
    if form.validate_on_submit():
        advisor = Funding_Agent(
            name = current_user.name,
            email = current_user.email,
            phone = current_user.phone, 
            user = current_user.id, 
            profile = form.profile.data,
            description = form.description.data,
            country = form.country.data,
            role = form.role.data,
            investment = form.investment.data,
            open_to = form.open_to.data,
            pic = current_user.profile_pic, 
        )

        advisor.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(advisor.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        advisor.pic = pic_name

        db.session.add(advisor)
        current_user.position = 'Funding Agent'
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('sponsorship_investment'))
    return render_template("funding_agent_apply.html", form=form)

@app.route('/sponsorship_investment')
@login_required
def sponsorship_investment():
    investors = Funding_Agent.query.all()
    return render_template("sponsorship_investment.html", investors=investors)

@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    if(current_user.position=='StartUp'):
        positions = Positions.query.all()
        projects = Project.query.all()
        return render_template("profile.html", user=user, positions=positions, projects=projects)
    elif(current_user.position=='Mentor' or current_user.position=='Counsellor'):
        mentors = MentorCounsellor.query.all()
        return render_template("profile.html", user=user , mentors=mentors)
    elif(current_user.position=='Validator' ):
        validator = Validator.query.all()
        return render_template("profile.html", user=user , validator=validator)
    elif(current_user.position=='Legal Advisor' ):
        legals = Legal_Advisor.query.all()
        return render_template("profile.html", user=user , legals=legals)
    elif(current_user.position=='Funding Agent' ):
        fundings = Funding_Agent.query.all()
        return render_template("profile.html", user=user , fundings=fundings)
    elif(current_user.position=='Linkage Agent' ):
        linkages = Linkage_Agent.query.all()
        return render_template("profile.html", user=user , linkages=linkages)
    elif(current_user.position=='Advertisement Agent' ):
        advertisers = Advertisement_Agent.query.all()
        return render_template("profile.html", user=user , advertisers=advertisers)
    elif(current_user.position=='Job Seeker' ):
        seekers = Open_to_work.query.all()
        return render_template("profile.html", user=user , seekers=seekers)
    return render_template("profile.html", user=user)

@app.route('/update_details', methods=['GET', 'POST'])
@login_required
def update_details():
    form1 = UpdateAccountForm()
    if form1.validate_on_submit():
        current_user.name = form1.name.data
        current_user.phone = form1.phone.data
        current_user.address = form1.address.data
        current_user.email = form1.email.data
        current_user.profile_pic = request.files['profile_pic']
        # Grab Image Name
        pic_filename = secure_filename(current_user.profile_pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['profile_pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        current_user.profile_pic = pic_name
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your account has been updated!', 'success') 
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form1.name.data = current_user.name
        form1.email.data = current_user.email
        form1.phone.data = current_user.phone
        form1.address.data = current_user.address
    
    return render_template("update_details.html", account_form=form1)

@app.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    form2 = ResetPasswordForm()
    if form2.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form2.old_password.data):
            current_user.password = bcrypt.generate_password_hash(form2.new_password.data).decode('utf-8')
            db.session.commit()
            flash('Password Changed', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Old Password not changed', 'danger')
    return render_template("update_password.html", password_form =form2)

@app.route('/available_positions_apply', methods=['GET', 'POST'])
@login_required
def available_positions_apply():
    projects = Project.query.filter_by(user = current_user.id)
    for project in projects:
        proj_id = project.id
        proj_name = project.name
    form = Add_Position() 
    if form.validate_on_submit():
        position = Positions(
            user_id = current_user.id,
            total_workforce = form.total_workforce.data,
            female_workforce = form.female_workforce.data,
            category_workforce = form.category_workforce.data,
            project_name = proj_name,
            job_title = form.job_title.data,
            job_description = form.job_description.data,
            number_open = form.number_open.data,
            phone = form.phone.data,
            email = form.email.data,
            project_id = proj_id,
            paid_unpaid = form.paid_unpaid.data,
            duration = form.duration.data,
            stipend = form.stipend.data,
            inoffice_wfh = form.inoffice_wfh.data,
            location = form.location.data
        )
        db.session.add(position)
        db.session.commit()
        return redirect(url_for('team_building_hiring'))
    return render_template("available_positions_apply.html", projects=projects, form=form)

@app.route('/open_to_work', methods=['GET', 'POST'])
@login_required
def open_to_work():
    form = Add_Open_Work() 
    if form.validate_on_submit():
        open = Open_to_work(
            user_id = current_user.id,
            name = current_user.name,
            email = current_user.email,
            phone = current_user.phone, 
            gender = form.gender.data,
            profession = form.profession.data,
            linkedin_link = form.linkedin_link.data,
            year_of_experience = form.year_of_experience.data,
            resume_link = form.resume_link.data,
            portfolio_link = form.portfolio_link.data,
            about = form.about.data,
            past_experience = form.past_experience.data,
            projects = form.projects.data,
            courses = form.courses.data,
            relocate = form.relocate.data,
            pic = current_user.profile_pic, 
        )

        open.pic = request.files['pic']
        # Grab Image Name
        pic_filename = secure_filename(open.pic.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image
        file = request.files['pic']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        # Change it to string to save to db
        open.pic = pic_name

        db.session.add(open)
        current_user.open_to_work = 'Open'
        current_user.position = 'Job Seeker'
        current_user.profile_pic = pic_name
        db.session.commit()
        return redirect(url_for('team_building_hiring'))
    return render_template("open_to_work.html", form=form)

@app.route("/bulk_mail", methods=['GET', 'POST'])
def bulk_mail():
    form = BulkMail()
    
    if form.validate_on_submit():
        msg = Message("Promotional Mail Service by Unicorn",
            sender="phoenix.we9574@gmail.com",
            recipients=["punerva21@gmail.com","phoenix.we9574@gmail.com"])

        msg.body = '''Hey Unicornes,
        A new member has joined our family, connect ad help them in their journey:
                  
        Name of member: %s
        Email address: %s
        Message from them: %s
        '''%(form.name.data,form.email.data,form.mail_body.data)
        mail.send(msg)
        return redirect(url_for('home'))

    return render_template('bulk_mail.html',title='Bulk Mail Service',form=form)

@app.route("/free_resources")
def free_resources():
    return render_template('free_resources.html')

@app.route("/success_stories")
def success_stories():
    return render_template('success_stories.html')

@app.route("/motivational_corner")
def motivational_corner():
    return render_template('motivational_corner.html')

@app.route("/gifting_service")
def gifting_service():
    return render_template('gifting_service.html')

@app.route("/faq_tnc")
def faq_tnc():
    return render_template('faq_tnc.html')

@app.route("/special_offers")
def special_offers():
    return render_template('special_offers.html')

@app.route("/partners")
def partners():
    return render_template('partners.html')

@app.route("/guide")
def guide():
    return render_template('guide.html')

@app.route("/trending_startups", methods=['GET', 'POST'])
def trending_startups():
    origin = request.args.get('country')
    if origin:
        trendings = Trending.query.filter(Trending.country.contains(origin))
    else:
        trendings = Trending.query.all()
    return render_template('trending_startups.html', trendings=trendings)

@app.route("/google_assistant", methods=['GET', 'POST'])
def google_assistant():
    form = Google_Assistant()
    if form.validate_on_submit():
        # uncomment the following code to run google assistant, for better result use headphones.
        # subprocess.run(['googlesamples-assistant-pushtotalk'], capture_output=True, text=True)
        return render_template('google_assistant.html', form=form)
    return render_template('google_assistant.html', form=form)

@app.route("/brand_name", methods=['GET', 'POST'])
def brand_name():
    form = Brand_Name()
    if form.validate_on_submit():
        input = form.input.data
        import requests

        API_URL = "https://api-inference.huggingface.co/models/abdelhalim/Rec_Business_Names"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": input,
        })
        print(output)
        output = output[0]["generated_text"]

        r = requests.post(
            "https://api.deepai.org/api/logo-generator",
            data={
                "text": input,
            },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        output_img = r.json()
        output_img = output_img['output_url']
        print(output_img)

        return render_template('brand_name.html', output=output, form=form, output_img=output_img)
    return render_template('brand_name.html', form=form)

@app.route("/gifting", methods=['GET', 'POST'])
def gifting():
    form = Add_Gift() 
    if form.validate_on_submit():
        gift = Gift(
            name = form.name.data,
            email = form.email.data,
            phone = form.phone.data, 
            item = form.item.data,
            address = form.address.data,
            msg = form.msg.data,
            customization = form.customization.data
        )
        db.session.add(gift)
        db.session.commit()

        # Mail
        msg = Message("Unicorn: Gift order successfully placed",
        sender="phoenix.we9574@gmail.com",
        recipients=[form.email.data])
        # recipients="phoenix.we9574@gmail.com")

        msg.body = '''%s, Your gifting order have been successfully placed. 
        Gift details are as follows:
        Item: %s
        Customization: %s
        Message to be sent along with gift: %s
        Address of the receiver: %s

        Further details will be shared on your phone number: %s
        '''%(form.name.data, form.item.data, form.customization.data, form.msg.data, form.address.data, form.phone.data)
        mail.send(msg)
        
        return redirect(url_for('home'))
    return render_template('gifting.html', form=form)

@app.route("/market_analysis")
def market_analysis():
    return render_template('market_analysis.html')

@app.route("/about")
def about():
    mentors = User.query.filter(User.position=='Mentor' or User.position=='Counsellor').count()
    validator = User.query.filter(User.position=='Validator').count()
    legal = User.query.filter(User.position=='Legal Advisor').count()
    startup = User.query.filter(User.position=='StartUp').count()
    funding = User.query.filter(User.position=='Funding Agent').count()
    linkage = User.query.filter(User.position=='Linkage Agent').count()
    ad = User.query.filter(User.position=='Advertisement Agent').count()
    job = User.query.filter(User.position=='Job Seeker').count()
    return render_template('about.html', mentors=mentors, validator=validator, legal=legal, startup=startup, funding=funding, linkage=linkage, ad=ad, job=job)

@app.route('/add_item', methods=['POST'])
def add_item():
    task = request.form['task']
    t = Tasks(
        list_item = task,
        user = current_user.id
    )
    db.session.add(t)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/delete_item/<int:index>')
def delete_item(index):
    Tasks.query.filter_by(id=index).delete()
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route("/accelerator")
def accelerator():
    company = request.args.get('company')
    if company:
        accelerators = Accelerator.query.filter(Accelerator.company.contains(company))
    else:
        accelerators = Accelerator.query.all()
    return render_template('accelerator.html', accelerators=accelerators)

@app.route("/accelerator_apply", methods=['GET', 'POST'])
def accelerator_apply():
    form = Accelerator_Form() 
    if form.validate_on_submit():
        accelerator = Accelerator(
            name = form.name.data,
            email = form.email.data,
            company = form.company.data, 
            program_name = form.program_name.data,
            program_desc = form.program_desc.data,
            link = form.link.data,
            location = form.location.data,
            open_to = form.open_to.data,
            resources = form.resources.data
        )
        db.session.add(accelerator)
        db.session.commit()
        
        return redirect(url_for('accelerator'))
    return render_template('accelerator_apply.html', form=form)

@app.route("/dashboard")
def dashboard():
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # creds.refresh(Request())
            print()
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/punerva/Desktop/Unicorn/flask_app/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'

    event_list = ''
    event_list += '<p>Getting the upcoming 5 events:-<p><ol>'
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                         maxResults=5, singleEvents=True,
    #                                         orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if not events:
    #     print('No upcoming events found.')
    #     return
    
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     event_list += '<li>'
    #     event_list += start
    #     event_list += ' '
    #     event_list += event['summary']
    #     event_list += '</li>'
    #     print(start, event['summary'])

    # event_list += '</ol></p>'
    tasks = Tasks.query.all()
    surveys = Survey.query.filter_by(user = current_user.id)

    tests = Volunteer_test.query.filter_by(user_id = current_user.id)
    companies = {}
    return render_template('dashboard.html', surveys=surveys, tasks=tasks, tests=tests, companies=companies)
    # return render_template('dashboard.html', surveys=surveys, tasks=tasks, event_list=event_list, tests=tests, companies=companies)

# Community Page
@app.route('/community', methods=['GET', 'POST'])
def community():
    user = User.query.all()
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            text=form.text.data,
            header=form.header.data,
            views=0,
            user_id=current_user.id,
            profile_pic = current_user.profile_pic,
            timestamp = datetime.now()
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('community'))
    ques = request.args.get('ques')
    if ques:
        query = Post.query.filter(Post.header.contains(ques) | Post.text.contains(ques))
    else:
        query = Post.query
    pagination = query.order_by(Post.timestamp.desc()).paginate(
                per_page=current_app.config['POSTS_PER_PAGE'],error_out=False)
    posts = pagination.items

    return render_template('community.html', form=form, posts=posts, pagination=pagination, user=user)

# Post page
@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    user = User.query.all()
    post_upvote=PostLike.query.filter_by(post_id=id).count()
    post.views += 1
    db.session.commit()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text = form.body.data,
                            post_id = id,
                            author_id = current_user.id,
                            profile_pic = current_user.profile_pic,
                            timestamp = datetime.now()
                        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been published.')
        return redirect(url_for('community', id=post.id))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // \
            current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
        page=page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)

    comments = pagination.items
    
    return render_template('post.html', posts=[post], form=form,
                           comments=comments, pagination=pagination, post_upvote=post_upvote,
                           user=user)

# Edit Post page
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        if form.submit.data:
                post.text = form.text.data
                post.header = form.header.data
                db.session.add(post)
                db.session.commit()
                flash('The post has been updated.')
                return redirect(url_for('post', id=post.id))
        elif form.delete.data:
                Post.query.filter_by(id=post.id).delete()
                db.session.commit()
                flash('The post has been Deleted.')
                return redirect(url_for('community'))
    form.text.data = post.text
    form.header.data = post.header
    return render_template('edit_post.html', form=form)

@app.route('/like-post/<int:post_id>/<action>')
@login_required
def like_post_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)

@app.route('/like-comment/<int:comment_id>/<action>')
@login_required
def like_comment_action(comment_id, action):
    comment = Comment.query.filter_by(id=comment_id).first_or_404()
    if action == 'like':
        current_user.like_comment(comment)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_comment(comment)
        db.session.commit()
    return redirect(request.referrer)

# Edit Comment page
@app.route('/edit-comment/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_comment(id):
    comment = Comment.query.get_or_404(id)
    if current_user != comment.author :
        abort(403)
    form = CommentForm()
    if form.validate_on_submit():
        if form.submit.data:
                comment.text = form.body.data
                db.session.add(comment)
                db.session.commit()
                flash('The Answer has been updated.')
                return redirect(url_for('.post', id=comment.post_id))
        elif form.delete.data:
                Comment.query.filter_by(id=comment.id).delete()
                db.session.commit()
                flash('The Answer has been Deleted.')
                return redirect(url_for('.post', id=comment.post_id))
    
    form.body.data = comment.text
    return render_template('edit_comment.html', form=form)

@app.route('/mentor_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def mentor_profile(user_id):
    mentor = MentorCounsellor.query.get_or_404(user_id)
    form = Update_Mentor_Detail() 
    if form.validate_on_submit():
        mentor.year = form.year.data,
        mentor.cost = form.cost.data,
        mentor.profile = form.profile.data,
        mentor.availability = form.availability.data,
        mentor.expertise = form.expertise.data
        mentor.year = int(mentor.year[0])
        mentor.cost = int(mentor.cost[0])
        mentor.profile = str(mentor.profile[0])
        mentor.availability = int(mentor.availability[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("mentor_profile.html", mentor=mentor, form=form)

@app.route('/validator_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def validator_profile(user_id):
    validator = Validator.query.get_or_404(user_id)
    form = Update_Validator_Detail() 
    if form.validate_on_submit():
        validator.profile = form.profile.data,
        validator.profile = str(validator.profile[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("validator_profile.html", validator=validator, form=form)

@app.route('/linkage_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def linkage_profile(user_id):
    agent = Linkage_Agent.query.get_or_404(user_id)
    form = Update_Linkage_Agent() 
    if form.validate_on_submit():
        agent.name = form.name.data,
        agent.email = form.email.data,
        agent.phone = form.phone.data, 
        agent.link = form.link.data,
        agent.description = form.description.data,
        agent.country = form.country.data,
        agent.state = form.state.data,
        agent.service = form.service.data,
        agent.open_to = form.open_to.data,
        agent.name = str(agent.name[0])
        agent.email = str(agent.email[0])
        agent.phone = str(agent.phone[0])
        agent.link = str(agent.link[0])
        agent.description = str(agent.description[0])
        agent.country = str(agent.country[0])
        agent.state = str(agent.state[0])
        agent.service = str(agent.service[0])
        agent.open_to = str(agent.open_to[0])
        db.session.commit()
        return redirect(url_for('linkage_agent'))
    return render_template("linkage_profile.html", agent=agent, form=form)

@app.route('/advertiser_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def advertiser_profile(user_id):
    advertiser = Advertisement_Agent.query.get_or_404(user_id)
    form = Update_Advertiser_Detail() 
    if form.validate_on_submit():
        advertiser.city = form.city.data,
        advertiser.country = form.country.data,
        advertiser.state = form.state.data,
        advertiser.service = form.service.data,
        advertiser.availability = form.availability.data,
        advertiser.city = str(advertiser.city[0])
        advertiser.country = str(advertiser.country[0])
        advertiser.state = str(advertiser.state[0])
        advertiser.service = str(advertiser.service[0])
        advertiser.availability = str(advertiser.availability[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("advertiser_profile.html", advertiser=advertiser, form=form)

@app.route('/funding_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def funding_profile(user_id):
    funding = Funding_Agent.query.get_or_404(user_id)
    form = Update_Funding_Detail() 
    if form.validate_on_submit():
        funding.profile = form.profile.data,
        funding.description = form.description.data,
        funding.country = form.country.data,
        funding.role = form.role.data,
        funding.investment = form.investment.data,
        funding.open_to = form.open_to.data,
        funding.profile = str(funding.profile[0])
        funding.description = str(funding.description[0])
        funding.country = str(funding.country[0])
        funding.role = str(funding.role[0])
        funding.investment = int(funding.investment[0])
        funding.open_to = str(funding.open_to[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("funding_profile.html", funding=funding, form=form)

@app.route('/legal_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def legal_profile(user_id):
    legal = Legal_Advisor.query.get_or_404(user_id)
    form = Update_Legal_Detail() 
    if form.validate_on_submit():
        legal.profile = form.profile.data,
        legal.description = form.description.data,
        legal.city = form.city.data,
        legal.country = form.country.data,
        legal.role = form.role.data,
        legal.awards = form.awards.data,
        legal.cases = form.cases.data,
        legal.advised = form.advised.data,
        legal.union = form.union.data,
        legal.year = form.year.data,
        legal.profile = str(legal.profile[0])
        legal.description = str(legal.description[0])
        legal.city = str(legal.city[0])
        legal.country = str(legal.country[0])
        legal.role = str(legal.role[0])
        legal.awards = str(legal.awards[0])
        legal.cases = str(legal.cases[0])
        legal.advised = str(legal.advised[0])
        legal.union = str(legal.union[0])
        legal.year = str(legal.year[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("legal_profile.html", legal=legal, form=form)

@app.route('/open_to_work_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def open_to_work_profile(user_id):
    person = Open_to_work.query.get_or_404(user_id)
    form = Update_Seeker_Detail() 
    if form.validate_on_submit():
        person.gender = form.gender.data,
        person.profession = form.profession.data,
        person.linkedin_link = form.linkedin_link.data,
        person.year_of_experience = form.year_of_experience.data,
        person.resume_link = form.resume_link.data,
        person.portfolio_link = form.portfolio_link.data,
        person.about = form.about.data,
        person.past_experience = form.past_experience.data,
        person.projects = form.projects.data,
        person.courses = form.courses.data,
        person.relocate = form.relocate.data,
        person.gender = str(person.gender[0])
        person.profession = str(person.profession[0])
        person.linkedin_link = str(person.linkedin_link[0])
        person.year_of_experience = int(person.year_of_experience[0])
        person.resume_link = str(person.resume_link[0])
        person.portfolio_link = str(person.portfolio_link[0])
        person.about = str(person.about[0])
        person.past_experience = str(person.past_experience[0])
        person.projects = str(person.projects[0])
        person.courses = str(person.courses[0])
        person.relocate = str(person.relocate[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("open_to_work_profile.html", person=person, form=form)

@app.route('/positions_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def positions_profile(user_id):
    position = Positions.query.get_or_404(user_id)
    form = Update_Position_Detail() 
    if form.validate_on_submit():
        position.job_title = form.job_title.data,
        position.job_description = form.job_description.data,
        position.number_open = form.number_open.data,
        position.phone = form.phone.data,
        position.email = form.email.data,
        position.paid_unpaid = form.paid_unpaid.data,
        position.duration = form.duration.data,
        position.stipend = form.stipend.data,
        position.inoffice_wfh = form.inoffice_wfh.data,
        position.location = form.location.data
        position.job_title = str(position.job_title[0])
        position.job_description = str(position.job_description[0])
        position.number_open = int(position.number_open[0])
        position.phone = str(position.phone[0])
        position.email = str(position.email[0])
        position.paid_unpaid = str(position.paid_unpaid[0])
        position.duration = str(position.duration[0])
        position.stipend = int(position.stipend[0])
        position.inoffice_wfh = str(position.inoffice_wfh[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("positions_profile.html", position=position, form=form)

@app.route('/project_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def project_profile(user_id):
    project = Project.query.get_or_404(user_id)
    form = Update_Project_Detail() 
    if form.validate_on_submit():
        project.idea = form.idea.data,
        project.profile = form.profile.data,
        project.extra = form.extra.data,
        project.category = form.category.data,
        project.industry = form.industry.data,
        project.country = form.country.data,
        project.idea = str(project.idea[0])
        project.profile = str(project.profile[0])
        project.extra = str(project.extra[0])
        project.category = str(project.category[0])
        project.industry = str(project.industry[0])
        project.country = str(project.country[0])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("project_profile.html", project=project, form=form)

@app.route('/profit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def profit(project_id):
    project = Project.query.get_or_404(project_id)
    form = Profit_Projection()
    answer = ""
    if form.validate_on_submit():
        project.administration = form.administration.data,
        project.rnd = form.rnd.data,
        project.marketing = form.marketing.data,
        project.profit = form.profit.data,
        project.rnd = int(project.rnd[0])
        project.administration = int(project.administration[0])
        project.marketing = int(project.marketing[0])
        project.profit = int(project.profit[0])
        db.session.commit()
        relationship = project.rnd
        milestone = project.marketing
        istop500 = project.profit
        prediction = success.predict([[relationship, milestone, istop500]])

        if prediction == 0:
            answer += "Your chances of failing is quite high!!"
        else:
            answer += "According to our prediction, you have high chances of succeeding"

        return render_template("profit.html", answer = answer, form = form)
    return render_template("profit.html", project=project, form=form)


@app.route("/profit_prediction", methods = ['GET', 'POST'])
def profit_prediction():
    if request.method == 'POST':
        RnD = float(request.form['RnD'])
        administration = float(request.form['administration'])
        marketing = float(request.form['marketing'])
        prediction = model.predict([[RnD, administration, marketing]])
        output = round(prediction[0], 2)
        if output < 0:
            return render_template('profit_prediction.html', prediction_texts="Sorry you are on loss")
        else:
            return render_template('profit_prediction.html', prediction_text="The total profit comes out to be ${:.2f}".format((output)))
    else:
        return render_template('profit_prediction.html')


@app.route("/ad_recommend", methods = ['GET', 'POST'])
def ad_recommend():
    form = Ad_recommend()
    if form.validate_on_submit():
        input = form.input.data
        input = input.lower()
        output = ""
        def find(dec,k):
            r=[]
            for i in dec.index:
                if k in dec['Meta Description 1'][i]:
                    r.append(dec['Original Url'][i])
            return r

        result=set(find(adata, input)) 
        print(result)

        for i in result:
            output += "<a target = '_blank' href = '" + i + "'>" + i +  "</a> <br>"
            print(" Url Link ",i)
        return render_template('ad_recommend.html', form=form, output = output)
    return render_template('ad_recommend.html', form=form)

class DynamicForm(Form):
    pass

@app.route('/dynamic_form', methods=['GET', 'POST'])
def dynamic_form():
    if request.method == 'POST':
        survey_len = len(Survey.query.all())
        survey = Survey(
            sheet = survey_len + 1,
            user = current_user.id,
            survey_name = request.form['survey_name'],
            startup = request.form['startup'],
            required = request.form['required']
        )
        db.session.add(survey)
        db.session.commit()

        # Access form data
        form_data = {}
        for key in request.form:
            form_data[key] = request.form.getlist(key)
        # Process the form data as needed
        # print(form_data['field_label'])
        
        
        SERVICE_ACCOUNT_FILE = '/Users/punerva/Desktop/Unicorn/flask_app/keys.json'

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        credentials = None

        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID of spreadsheet.
        SAMPLE_SPREADSHEET_ID = '1Mh-v5r-1AHfnbLbR6Q0QPePVSLf1EGZUNCCvN3QB-w8'

        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API
        sheet = service.spreadsheets()

        aoa = []

        aoa.append(form_data['field_label'])
        print(aoa)

        survey_len = survey_len + 1
        req = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                    range=f'Sheet{survey_len}!A1', valueInputOption="USER_ENTERED", 
                                    insertDataOption="INSERT_ROWS", body={"values": aoa}).execute()

        print(req)

        companies = {}
        return render_template('dashboard.html', companies=companies)
    return render_template('dynamic_form.html')


@app.route('/google_sheet/<int:sheet_no>', methods=['GET', 'POST'])
def google_sheet(sheet_no):
    SERVICE_ACCOUNT_FILE = '/Users/punerva/Desktop/Unicorn/flask_app/keys.json'

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    credentials = None

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1Mh-v5r-1AHfnbLbR6Q0QPePVSLf1EGZUNCCvN3QB-w8'

    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=f'Sheet{sheet_no}!A1:Z10').execute()

    print(result['values'])
    question = result['values'][0]
    result['values'] = result['values']
    # print(request)
    surveys = Survey.query.filter_by(user = current_user.id)
    return render_template('google_sheet.html', result=result, surveys=surveys, sheet_no=sheet_no, question=question)

@app.route("/survey")
def survey():
    surveys = Survey.query.all()
    return render_template('survey.html', surveys=surveys)

@app.route("/take_survey/<int:sheet_no>", methods=['GET', 'POST'])
def take_survey(sheet_no):
    surveys = Survey.query.all()
    if request.method == 'POST':
        # Access form data
        form_data = {}
        for key in request.form:
            form_data[key] = request.form.getlist(key)

        for survey in surveys:
            if survey.sheet==sheet_no:
                survey.done += 1

        db.session.commit()

        SERVICE_ACCOUNT_FILE = '/Users/punerva/Desktop/Unicorn/flask_app/keys.json'

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        credentials = None

        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID of spreadsheet.
        SAMPLE_SPREADSHEET_ID = '1Mh-v5r-1AHfnbLbR6Q0QPePVSLf1EGZUNCCvN3QB-w8'

        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API
        sheet = service.spreadsheets()

        aoa = []

        aoa.append(form_data['field_label'])

        req = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                    range=f'Sheet{sheet_no}!A1', valueInputOption="USER_ENTERED", 
                                    insertDataOption="INSERT_ROWS", body={"values": aoa}).execute()

        print(req)
        return render_template('survey.html', surveys=surveys)
    
    SERVICE_ACCOUNT_FILE = '/Users/punerva/Desktop/Unicorn/flask_app/keys.json'

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    credentials = None

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1Mh-v5r-1AHfnbLbR6Q0QPePVSLf1EGZUNCCvN3QB-w8'

    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=f'Sheet{sheet_no}!A1:Z1').execute()

    print(result['values'])
    # print(request)
    return render_template('take_survey.html', result=result, surveys=surveys, sheet_no=sheet_no)

@app.route('/trends', methods=['GET', 'POST'])
def trends():
    if request.method == 'POST':
        keyword = request.form['keyword']

        #get the google trends scraper
        from pytrends.request import TrendReq
        #add my parameters 
        trend = TrendReq(hl='en-US', tz=360)
        #keyword list
        kw_list=[]
        kw_list.append(keyword)

        #create payload
        trend.build_payload(kw_list,timeframe='2021-01-01 2022-01-01')

        #create a dataframe of google trends
        data = trend.interest_over_time()
        print(data.head())
        fig = px.line(data,x=data.index, y=kw_list,title=kw_list[0])


        templates_dir = os.path.join(os.path.dirname('/Users/punerva/Desktop/Unicorn/flask_app/'), 'templates')
        chart_html_path = os.path.join(templates_dir, 'google_trends_chart.html')
        print(chart_html_path)
        pio.write_html(fig, chart_html_path)
        
        '''Interest by region'''
        ibr = trend.interest_by_region()
        #looking at rows where all values are not equal to 0
        ibr = ibr[(ibr != 0).all(1)]

        #drop all rows that have null values in all columns
        ibr.dropna(how='all',axis=0, inplace=True)

        print(ibr.head())
        fig2 = px.line(ibr,x=ibr.index, y=kw_list,title=kw_list[0])
        chart_html_path2 = os.path.join(templates_dir, 'google_trends_chart_ibr.html')
        print(chart_html_path2)
        pio.write_html(fig2, chart_html_path2)

        '''realtime Trends'''
        rt = trend.trending_searches(pn='united_states')
        print(rt.head(10))

        '''related queries'''
        rq = trend.related_queries()
        rq = rq[kw_list[0]]['top']
        print(rq)

        print(rq.head(10))

        return render_template('trends.html', ibr=ibr, rt=rt, rq=rq, regiondf=data, state=True)
    ibr = pd.DataFrame()
    rt = pd.DataFrame()
    rq = pd.DataFrame()
    data = pd.DataFrame()
    return render_template('trends.html', ibr=ibr, rt=rt, rq=rq, regiondf=data, state=False)

@app.route("/events", methods=['GET', 'POST'])
def events():
    form = Event_Form()
    if form.validate_on_submit():
        print(form.data)

        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '/Users/punerva/Desktop/Unicorn/flask_app/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': form.summary.data,
            'location': form.location.data,
            'description': form.description.data,
            'start': {
                'dateTime': form.start_dateTime.data,
                'timeZone': form.start_timeZone.data,
            },
            'end': {
                'dateTime': form.end_dateTime.data,
                'timeZone': form.end_timeZone.data,
            },
            # 'attendees': [
            #     {'email': form.attendees_one.data},
            # ],
            'attendees': [
                {'email': 'punerva21@gmail.com'}
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60}
                ],
            },
            }

        event = service.events().insert(calendarId='primary', body=event).execute()

        # Mail
        msg = Message("Unicorn: calendar Event",
        sender="phoenix.we9574@gmail.com",
        # recipients=[form.attendees_one.data, form.attendees_two.data])
        recipients=["punerva21@gmail.com"])

        msg.body = '''You have been added to a calendar event. Details for the same are given below:-
        - Event Subject: %s,
        - Event location: %s,
        - Event Description: %s,
        - Event Date: %s,
        - Event calendar link: %s
        '''%(form.summary.data, form.location.data, form.description.data, form.start_dateTime.data, event.get('htmlLink'))
        mail.send(msg)
        # print ('Event created: %s' % (event.get('htmlLink')))

        return redirect(url_for('dashboard'))
    return render_template('events.html', form=form)


def get_sources_and_domains():
    all_sources = newsapi.get_sources()['sources']
    sources = []
    domains = []
    for e in all_sources:
        id = e['id']
        domain = e['url'].replace("http://", "")
        domain = domain.replace("https://", "")
        domain = domain.replace("www.", "")
        slash = domain.find('/')
        if slash != -1:
            domain = domain[:slash]
        sources.append(id)
        domains.append(domain)
    sources = ", ".join(sources)
    domains = ", ".join(domains)
    return sources, domains
  
@app.route("/news", methods=['GET', 'POST'])
def news():
    if request.method == "POST":
        sources, domains = get_sources_and_domains()
        keyword = request.form["keyword"]
        related_news = newsapi.get_everything(q=keyword,
                                      sources=sources,
                                      domains=domains,
                                      language='en',
                                      sort_by='relevancy')
        no_of_articles = related_news['totalResults']
        if no_of_articles > 100:
            no_of_articles = 100
        all_articles = newsapi.get_everything(q=keyword,
                                      sources=sources,
                                      domains=domains,
                                      language='en',
                                      sort_by='relevancy',
                                      page_size = no_of_articles)['articles']
        return render_template("news.html", all_articles = all_articles, 
                               keyword=keyword)
    else:
        top_headlines = newsapi.get_everything(q='Acquisition',
                                      sources='Lifehacker.com, Engadget, Wired',
                                      domains='bbc.co.uk, techcrunch.com, engadget.com',
                                      language='en',
                                      sort_by='relevancy')
        total_results = top_headlines['totalResults']
        if total_results > 100:
            total_results = 100
        all_headlines = newsapi.get_everything(q='Acquisition',
                                      sources='Lifehacker.com, Engadget, Wired',
                                      domains='bbc.co.uk, techcrunch.com, engadget.com',
                                      language='en',
                                      sort_by='relevancy')['articles']
        return render_template("news.html", all_headlines = all_headlines)

@app.route("/volunteer")
def volunteer():
    origin = request.args.get('location')
    indus_type = request.args.get('industry')
    # age_range = request.form.getlist('options')
    if origin:
        volunteers = Volunteer.query.filter((Volunteer.location.contains(origin)) & (Volunteer.industry.contains(indus_type)))
    else:
        volunteers = Volunteer.query.all()
    return render_template('volunteer.html', volunteers=volunteers)

@app.route("/volunteer_apply", methods=['GET', 'POST'])
def volunteer_apply():
    form = Add_Volunteer()
    if form.validate_on_submit():
        volunteer = Volunteer(
            name = form.name.data,
            email = form.email.data,
            location = form.location.data,
            industry = form.industry.data,
            phone = form.phone.data,
            age_range = form.age_range.data,
        )
        db.session.add(volunteer)
        db.session.commit()
        return redirect(url_for('volunteer'))
    return render_template('volunteer_apply.html', form=form)


@app.route("/save_csv", methods=['POST'])
def save_csv():
    if request.method == 'POST':
        conn = sqlite3.connect('/Users/punerva/Desktop/Unicorn/instance/site.db', isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM volunteer", conn)
        db_df.to_csv('database.csv', index=False)
        return redirect(url_for('volunteer'))
    return redirect(url_for('volunteer'))

@app.route("/product_test")
def product_test():
    tests = Volunteer_test.query.all()
    return render_template('product_test.html', tests=tests)

@app.route("/challenge", methods=['GET', 'POST'])
def challenge():
    form = Challenges()
    if form.validate_on_submit():
        print(form)
        cha = challenges(
            challenge_name = form.challenge_name.data,
            challenge_desc = form.challenge_desc.data,
            eligibility = form.eligibility.data,
            company_name = form.company_name.data,
            location = form.location.data,
            theme = form.theme.data,
            relevant_industry = form.relevant_industry.data,
            Incentives = form.incentives.data,
            email = form.email.data,
            timeline = form.timeline.data
        )
        db.session.add(cha)
        db.session.commit()
        return redirect(url_for('challenges_for_startups'))
    return render_template('challenge.html', form=form)

@app.route("/challenges_for_startups", methods=['GET', 'POST'])
def challenges_for_startups():
    chas = challenges.query.all()
    return render_template('challenges_for_startups.html', chas = chas)

@app.route("/apply_for_challenges/<int:challenge_id>", methods=['GET', 'POST'])
def apply_for_challenges(challenge_id):
    chas = challenges.query.filter_by(id=challenge_id).first()
    if request.method == 'POST':
        email = request.form['text']
        applicant = Applicants(
            email = email,
            challenge_id = challenge_id
        )
        db.session.add(applicant)
        db.session.commit()
        return redirect(url_for('challenges_for_startups'))
    return render_template('apply_for_challenges.html', chas = chas)

@app.route("/product_test_individual/<int:test_id>", methods=['POST'])
def product_test_individual(test_id):
    if request.method == 'POST':
        email = request.form['text']
        t_id = request.form['txt']
        t_id = int(t_id[0])
        test = Volunteer_test.query.filter_by(id=t_id).first()
        test.reg_list += email
        test.reg_list += ', '
        test.total_reg += 1
        # if test.total_reg > 10 and test.premium_account==True:
        #     db.session.commit()
        # else:
        #     test.status = false
        db.session.commit()
        return redirect(url_for('product_test'))
    return redirect(url_for('product_test'))

@app.route("/test_apply", methods=['GET', 'POST'])
def test_apply():
    form = Test_Form()
    if form.validate_on_submit():
        test = Volunteer_test(
            name = form.name.data,
            email = form.email.data,
            startup_name = form.startup_name.data,
            location = form.location.data,
            industry = form.industry.data,
            age_range = form.age_range.data,
            test_details = form.test_details.data,
            credits_given = form.credits_given.data,
            link = form.link.data,
            reg_list = '',
            total_reg = 0,
            start_date = date.today(),
            user_id = current_user.id,
        )
        db.session.add(test)
        db.session.commit()

        # emails =  Volunteer.query.with_entities(Volunteer.email).all()
        # recipients_list = '"'
        # for email in emails:
        #     recipients_list += email[0]
        #     recipients_list += '","'

        # recipients_list = recipients_list[:-2]

        # # Mail
        # msg = Message("Unicorn: New Product Test Available",
        # sender="phoenix.we9574@gmail.com",
        # recipients=["phoenix.we9574@gmail.com"])
        # # recipients=[recipients_list])

        # msg.body = '''A new product test has been added in our database. Details for the same are given below:-
        # - Startup name: %s,
        # - Industry: %s,
        # - Test Details: %s,
        # - Link: %s
        # Take test now to get free credits upto $500, free Netflix Subscription and many more exciting gifts.
        # '''%(form.startup_name.data, form.industry.data, form.test_details.data, form.link.data)
        # mail.send(msg)

        return redirect(url_for('product_test'))
    return render_template('test_apply.html', form=form)

@app.route("/stop_test", methods=['POST'])
def stop_test():
    if request.method == 'POST':
        t_id = request.form['txt']
        t_id = int(t_id[0])
        test = Volunteer_test.query.filter_by(id=t_id).first()
        test.status = 1
        db.session.commit()
        return redirect(url_for('product_test'))
    return redirect(url_for('product_test'))

@app.route("/open_credits", methods=['POST'])
def open_credits():
    if request.method == 'POST':
        t_id = request.form['txt']
        t_id = int(t_id[0])
        test = Volunteer_test.query.filter_by(id=t_id).first()
        registered = test.reg_list
        registered = registered[0:-2]
        x = registered.split(", ")
        # Mail
        msg = Message("Your free credits from Unicorn are here",
        sender="phoenix.we9574@gmail.com",
        recipients=["punerva045btcsai20@igdtuw.ac.in"])
        # recipients=x)

        msg.body = '''Your are eligible to free credits from Unicorn. Visit the link below to redeem them.
        - Link: http://127.0.0.1:5000/dashboard
        '''
        mail.send(msg)
        return redirect(url_for('dashboard'))
    return redirect(url_for('dashboard'))

@app.route("/send_test_bulk", methods=['POST'])
def send_test_bulk():
    if request.method == 'POST':
        subject = request.form['txt']
        body = request.form['text']
        t_id = request.form['textt']
        t_id = int(t_id[0])
        test = Volunteer_test.query.filter_by(id=t_id).first()
        registered = test.reg_list
        registered = registered[0:-2]
        x = registered.split(", ")
        # Mail
        msg = Message(subject,
        sender="phoenix.we9574@gmail.com",
        recipients=["punerva045btcsai20@igdtuw.ac.in"])
        # recipients=x)

        msg.body = body
        mail.send(msg)
        return redirect(url_for('dashboard'))
    return redirect(url_for('dashboard'))


@app.route("/competitors", methods=['GET','POST'])
def competitors():
    if request.method == 'POST':
        industry = request.form['txt']
        query = "top 10 " + industry + " " + "companies list moneyworks4me.com "
        from serpapi import GoogleSearch

        params = {
        "engine": "google",
        "q": query,
        "api_key": "API_KEY"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results["organic_results"]

        url = organic_results[0]['link']

        req = Request(url)
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
        content = urlopen(req).read()

        source = urlopen(req).read()
        # Make a soup 
        soup = BeautifulSoup(source, 'html.parser')

        page_title = soup.head.title.text

        data = soup.find("div", {"id": "stock-data"})

        if(data == None):
            data = soup.find("div", {"class": "listintg-table"})
        
        if(len(data.find_all("div", {"class": "company-ellipses"})) != 0):
            list_of_stocks = data.find_all("div", {"class": "company-ellipses"})

        else:
            list_of_stocks = data.find_all("div", {"class": "pr-0 comp-name"})

        companies = {}
        companies_links = {}
        state = 0
        for stock in list_of_stocks:
            if state==10:
                break
            #companies_name.append(stock.text)
            company_name = stock.text.replace("\n", "")
            company_name = company_name.strip()
            #print(stock.text)
            link = stock.find("a")
            #companies_links.append(link.get('href'))
            cl = 'https://www.moneyworks4me.com/'
            company_link = link.get('href')
            company_link = cl + company_link
            companies[company_name] = company_link
            state += 1

        print(companies)

        news_query = "latest news related to " + industry 
        from serpapi import GoogleSearch

        params = {
        "engine": "google",
        "q": news_query,
        "api_key": "API_KEY"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results["organic_results"]

        recent_news = '<ul>'
        for item in organic_results:
            recent_news += '<li><a target="_blank" href="'
            recent_news += item['link']
            recent_news += '">'
            recent_news += item['snippet']
            recent_news += '</a></li>'
            recent_news += '<br>'

        recent_news += '</ul>'
        
        return render_template('competitors.html', companies=companies, recent_news=recent_news)
    
    companies = {}
    recent_news = ''
    return render_template('competitors.html', companies=companies, recent_news=recent_news)

@app.route("/projection", methods=['GET','POST'])
def projection():
    return render_template('projection.html')

@app.route("/basic_method", methods=['POST'])
def basic_method():
    if request.method == 'POST':
        funding_amount = int(request.form['txt'])
        equity_dilution = int(request.form['text'])
        basic_val = (funding_amount / equity_dilution) * 100
        
        return render_template('projection.html', basic_val=basic_val)

@app.route("/equity_dilution", methods=['POST'])
def equity_dilution():
    if request.method == 'POST':
        funding_amount = float(request.form['txt'])
        expected_val = float(request.form['text'])
        equity_dilution = (funding_amount / expected_val) * 100
        
        return render_template('projection.html', equity_dilution=equity_dilution)
    
@app.route("/revenue_triple", methods=['POST'])
def revenue_triple():
    if request.method == 'POST':
        df = pd.read_csv('/Users/punerva/Desktop/Unicorn/IT_Data.csv', encoding= 'unicode_escape')
        df['Multiplication_factor'] = df['Market_Cap']/df['Revenue']
        avg_mul_fac = df['Multiplication_factor'].mean()
        arr = float(request.form['txt'])
        mf = float(request.form['text'])
        val_avg = arr * avg_mul_fac
        val = arr * mf
        
        return render_template('projection.html', val_avg=val_avg, val=val)
    
@app.route("/berkus_method", methods=['POST'])
def berkus_method():
    if request.method == 'POST':
        idea = float(request.form['idea'])
        prototype = float(request.form['prototype'])
        founders = float(request.form['founders'])
        team = float(request.form['team'])
        traction = float(request.form['traction'])
        strategic = float(request.form['strategic'])
        revenue = float(request.form['revenue'])
        berkus = idea + prototype + founders + team + traction + strategic + revenue
        
        return render_template('projection.html', berkus=berkus)