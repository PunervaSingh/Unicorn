from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app.models import User
from flask_login import current_user
import string
# from flask_pagedown.fields import PageDownField


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    # def validate_phone(self, phone):
    #     try:
    #         p = phonenumbers.parse(phone.data)
    #         if not phonenumbers.is_valid_number(p):
    #             raise ValueError()
    #     except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
    #         raise ValidationError('Invalid phone number')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class UpdateAccountForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Name"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    profile_pic = FileField('Your Profile Photo')
    submit = SubmitField('Update Account details')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            
class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password',
                                     validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update password')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Add_Women_Programs(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=1, max=50)])
    description = StringField('Description',
                           validators=[DataRequired()])
    country = StringField('Country',
                           validators=[DataRequired()])
    industry = StringField('Industry',
                        validators=[DataRequired()])
    user = StringField('User',
                        validators=[DataRequired()])
    link = StringField('Link',
                        validators=[DataRequired()])
    status = StringField('Status',
                        validators=[DataRequired()])
    submit = SubmitField('Add Program')
        

class Add_Mentor_Counsellor_Form(FlaskForm):
    pic = FileField('Your Profile Photo')
    year = IntegerField('Year of Experience',
                        validators=[DataRequired()])
    cost = IntegerField('Cost per Session (In USD)',
                        validators=[DataRequired()])
    choice = StringField('Choice(Mentor/Counsellor)',
                        validators=[DataRequired()])
    expertise = StringField('Area of Expertise',
                        validators=[DataRequired()])
    profile = StringField('LinkedIn Profile Link',
                        validators=[DataRequired()])
    availability = IntegerField('Availability per Month (In hr)',
                        validators=[DataRequired()])
    submit = SubmitField('Submit Application')


class Add_Validator_Form(FlaskForm):
    pic = FileField('Your Profile Photo')
    profile = StringField('LinkedIn Profile Link',
                        validators=[DataRequired()])
    submit = SubmitField('Submit Application')
    

class Add_Legal_Advisor(FlaskForm):
    pic = FileField('Your Profile Photo')
    profile = StringField('LinkedIn Profile Link',
                        validators=[DataRequired()])
    description = StringField('Job Description',
                        validators=[DataRequired()])
    city = StringField('City',
                        validators=[DataRequired()])
    country = StringField('Country',
                        validators=[DataRequired()])
    role = StringField('Role (Legal Advisor)',
                        validators=[DataRequired()])
    awards = IntegerField('Awards',
                        validators=[DataRequired()])
    cases = IntegerField('Cases',
                        validators=[DataRequired()])
    advised = IntegerField('Advised',
                        validators=[DataRequired()])
    union = IntegerField('Union',
                        validators=[DataRequired()])
    year = IntegerField('Year of Experience',
                        validators=[DataRequired()])
    submit = SubmitField('Submit Application')

class Add_Project(FlaskForm):
    pic = FileField('Your Profile Photo')
    profile = StringField('Profile Link',
                        validators=[DataRequired()])
    name = StringField('Brand Name',
                           validators=[DataRequired(), Length(min=1, max=50)])
    idea = StringField('Idea',
                           validators=[DataRequired()])
    country = StringField('Country of origin',
                           validators=[DataRequired()])
    industry = StringField('Industry (IT / Food / etc.)',
                        validators=[DataRequired()])
    extra = StringField('Anything extra to add',
                        validators=[DataRequired()])
    category = StringField('Category (Service / Product)',
                        validators=[DataRequired()])
    women = BooleanField('Women Entrepreneur?')
    tier = BooleanField('Tier I or Tier II background?')
    village = BooleanField('Are you village Based?')
    submit = SubmitField('Propose your idea')

class Add_Funding_Agent(FlaskForm):
    pic = FileField('Your Profile Photo')
    profile = StringField('LinkedIn Profile Link',
                        validators=[DataRequired()])
    description = StringField('Job Description',
                        validators=[DataRequired()])
    country = StringField('Country',
                        validators=[DataRequired()])
    role = StringField('Current Role',
                        validators=[DataRequired()])
    investment = IntegerField('No of investments done',
                        validators=[DataRequired()])
    open_to = StringField('Open: WorldWide / Within Country',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


class Add_Linkage_Agent(FlaskForm):
    pic = FileField('Your Profile Photo')
    name = StringField('Company Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Contact No.', validators=[DataRequired()])
    email = StringField('Email Id',
                        validators=[DataRequired(), Email()])
    link = StringField('Site Link',
                        validators=[DataRequired()])
    description = StringField('Company Description',
                        validators=[DataRequired()])
    country = StringField('Country',
                        validators=[DataRequired()])
    state = StringField('Available in which state',
                        validators=[DataRequired()])
    service = StringField('Service that you provide',
                        validators=[DataRequired()])
    open_to = StringField('Open: National / International',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

class Add_Advertisement_Agent(FlaskForm):
    pic = FileField('Your Profile Photo')
    service = StringField('Service that you provide',
                        validators=[DataRequired()])
    city = StringField('City',
                        validators=[DataRequired()])
    state = StringField('State',
                        validators=[DataRequired()])
    country = StringField('Country',
                        validators=[DataRequired()])
    availability = StringField('Available throughout: City / State / Country',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

class Add_Position(FlaskForm):
    email = StringField('Email Id',
                        validators=[DataRequired(), Email()])
    phone = StringField('Contact No.', validators=[DataRequired()])
    job_title = StringField('Job Title',
                        validators=[DataRequired()])
    job_description = StringField('Job Description',
                        validators=[DataRequired()])
    number_open = IntegerField('Number of positions available',
                        validators=[DataRequired()])
    duration = StringField('Duration',
                        validators=[DataRequired()])
    stipend = IntegerField('Stipend',
                        validators=[DataRequired()])
    paid_unpaid = StringField('Paid / Unpaid',
                        validators=[DataRequired()])
    inoffice_wfh = StringField('Inoffice / Work from Home',
                        validators=[DataRequired()])
    location = StringField('Location',
                        validators=[DataRequired()])
    total_workforce = IntegerField('Total Workforce', validators=[DataRequired()])
    female_workforce = IntegerField('Female Workforce', validators=[DataRequired()])
    category_workforce = IntegerField('Category Workforce', validators=[DataRequired()])
    submit = SubmitField('Submit Positions')

class Add_Open_Work(FlaskForm):
    pic = FileField('Your Profile Photo')
    profession = StringField('Profession / Area of expertise', validators=[DataRequired()])
    linkedin_link = StringField('Profile Link',
                        validators=[DataRequired()])
    resume_link = StringField('Resume Link',
                        validators=[DataRequired()])
    portfolio_link = StringField('Portfolio Link',
                        validators=[DataRequired()])
    about = StringField('About you',
                        validators=[DataRequired()])
    past_experience = StringField('Past experiences in brief',
                        validators=[DataRequired()])
    year_of_experience = IntegerField('Year of Experience',
                        validators=[DataRequired()])
    projects = StringField('Projects',
                        validators=[DataRequired()]) 
    gender = StringField('Gender (Female / Male)',
                        validators=[DataRequired()])
    courses = StringField('Courses completed',
                        validators=[DataRequired()])
    relocate = StringField('Willing to relocate: Yes / No',
                        validators=[DataRequired()])
    submit = SubmitField('Submit Application')

class Validate_Project(FlaskForm):
    submit = SubmitField('Validate Project')

class Mentor_Project(FlaskForm):
    submit = SubmitField('Start Mentoring')

class Job_Apply(FlaskForm):
    portfolio_link = StringField('Portfolio Link',
                        validators=[DataRequired()], render_kw={"placeholder": "Portfolio Link"})
    category = StringField('Category: SC/ST/OBC/General',
                        validators=[DataRequired()], render_kw={"placeholder": "Category: SC/ST/OBC/General"})
    gender = StringField('Gender',
                        validators=[DataRequired()], render_kw={"placeholder": "Gender"})
    submit = SubmitField('Apply Now')

class Mentor_Request(FlaskForm):
    # mentor_id = IntegerField('Mentor Id', validators=[DataRequired()])
    submit = SubmitField('Book Now')

class BulkMail(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Name"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    mail_body = StringField('Body',
                           validators=[DataRequired(), Length(min=2)], render_kw={"placeholder": "Message"})
    submit = SubmitField('Send Mails')

class Add_Gift(FlaskForm):
    item = StringField('Item to be gifted',
                        validators=[DataRequired()], render_kw={"placeholder": "Item to be gifted"}) 
    customization = StringField('Customization on the item',
                        validators=[DataRequired()], render_kw={"placeholder": "Customization on the item"}) 
    address = StringField('Address of the receiver',
                        validators=[DataRequired()], render_kw={"placeholder": "Address of the receiver"})
    phone = StringField('Your phone number',
                        validators=[DataRequired()], render_kw={"placeholder": "Your phone number"})
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Your Name"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email Id"})
    msg = StringField('Message to be sent with the gift',
                           validators=[DataRequired(), Length(min=2)], render_kw={"placeholder": "Message to be sent with the gift"})
    submit = SubmitField('Send Gift')

class Brand_Name(FlaskForm):
    input = StringField('Input a phrase regarding your startup',
                        validators=[DataRequired()])
    submit = SubmitField('Generate Brand Name')

class Update_Mentor_Detail(FlaskForm):
    year = IntegerField('Year of Experience')
    cost = IntegerField('Cost per Session (In USD)')
    expertise = StringField('Area of Expertise')
    profile = StringField('LinkedIn Profile Link')
    availability = IntegerField('Availability per Month (In hr)')
    submit = SubmitField('Update Details')

class Update_Validator_Detail(FlaskForm):
    profile = StringField('LinkedIn Profile Link')
    submit = SubmitField('Update Details')

class Update_Linkage_Agent(FlaskForm):
    name = StringField('Company Name')
    phone = StringField('Contact No.')
    email = StringField('Email Id')
    link = StringField('Site Link')
    description = StringField('Company Description')
    country = StringField('Country')
    state = StringField('Available in which state')
    service = StringField('Service that you provide')
    open_to = StringField('Open: National / International')
    submit = SubmitField('Update Details')

class Update_Advertiser_Detail(FlaskForm):
    service = StringField('Service that you provide')
    city = StringField('City')
    state = StringField('State')
    country = StringField('Country')
    availability = StringField('Available throughout: City / State / Country')
    submit = SubmitField('Update Details')

class Update_Funding_Detail(FlaskForm):
    profile = StringField('LinkedIn Profile Link')
    description = StringField('Job Description')
    country = StringField('Country')
    role = StringField('Current Role')
    investment = IntegerField('No of investments done')
    open_to = StringField('Open: WorldWide / Within Country')
    submit = SubmitField('Update Details')

class Update_Legal_Detail(FlaskForm):
    profile = StringField('LinkedIn Profile Link')
    description = StringField('Job Description')
    city = StringField('City')
    country = StringField('Country')
    role = StringField('Role (Legal Advisor)')
    awards = IntegerField('Awards')
    cases = IntegerField('Cases')
    advised = IntegerField('Advised')
    union = IntegerField('Union')
    year = IntegerField('Year of Experience')
    submit = SubmitField('Update Details')

class Update_Seeker_Detail(FlaskForm):
    profession = StringField('Profession / Area of expertise')
    linkedin_link = StringField('Profile Link')
    resume_link = StringField('Resume Link')
    portfolio_link = StringField('Portfolio Link')
    about = StringField('About you')
    past_experience = StringField('Past experiences in brief')
    year_of_experience = IntegerField('Year of Experience')
    projects = StringField('Projects') 
    gender = StringField('Gender (Female / Male)')
    courses = StringField('Courses completed')
    relocate = StringField('Willing to relocate: Yes / No')
    submit = SubmitField('Update Details')

class Update_Position_Detail(FlaskForm):
    email = StringField('Email Id')
    phone = StringField('Contact No.')
    job_title = StringField('Job Title')
    job_description = StringField('Job Description')
    number_open = IntegerField('Number of positions available')
    duration = StringField('Duration')
    stipend = IntegerField('Stipend')
    paid_unpaid = StringField('Paid / Unpaid')
    inoffice_wfh = StringField('Inoffice / Work from Home')
    location = StringField('Location')
    submit = SubmitField('Update Position Details')

class Update_Project_Detail(FlaskForm):
    profile = StringField('Profile Link')
    idea = StringField('Idea')
    country = StringField('Country of origin')
    industry = StringField('Industry (IT / Food / etc.)')
    extra = StringField('Anything extra to add')
    category = StringField('Category (Service / Product)')
    submit = SubmitField('Update Project Detail')

class Profit_Projection(FlaskForm):
    rnd = IntegerField('Research and Development')
    marketing = IntegerField('Marketing')
    profit = IntegerField('Profit')
    administration = IntegerField('Administration')
    submit = SubmitField('Produce Profit Projection')

class PostForm(FlaskForm):
    header = StringField("Write header here", validators=[DataRequired()])
    text = StringField("Write your query here", validators=[DataRequired()])
    delete =  SubmitField("Delete")
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    body = StringField('Enter your answer', validators=[DataRequired()])
    delete =  SubmitField("Delete")
    submit = SubmitField('Submit')