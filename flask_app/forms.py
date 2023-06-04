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
    name = StringField('Update your name',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Update your name"})
    email = StringField('Update your email Id',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Update your email Id"})
    
    phone = StringField('Update your phone no.', validators=[DataRequired()])
    address = StringField('Update your current residential address', validators=[DataRequired()])
    profile_pic = FileField('Update your profile photo')
    submit = SubmitField('Update Account details')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            
class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('Enter your old password', validators=[DataRequired()])
    new_password = PasswordField('Enter your new password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Re-Enter your new password',
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


class Add_Volunteer(FlaskForm):
    name = StringField('Enter your name',
                           validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Enter your email Id',
                           validators=[DataRequired()])
    location = StringField('Enter your location(North America, South America, Europe, South Asia, Africa, East Asia, Middle East, others)',
                           validators=[DataRequired()])
    industry = StringField('Enter your preferred industry(Tech / Non-Tech)',
                        validators=[DataRequired()])
    phone = StringField('Enter your phone no.',
                        validators=[DataRequired()])
    age_range = StringField('Enter the range your age lies in(below 18, 18-40, 40 above)',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
        

class Add_Mentor_Counsellor_Form(FlaskForm):
    pic = FileField('Select Your Profile Photo')
    year = IntegerField('Enter Your Year of Experience',
                        validators=[DataRequired()])
    cost = IntegerField('Enter Your Preffered Cost per Session (In USD)',
                        validators=[DataRequired()])
    choice = StringField('Enter Your Choice(Mentor/Counsellor)',
                        validators=[DataRequired()])
    expertise = StringField('Enter Your Area of Expertise',
                        validators=[DataRequired()])
    profile = StringField('Enter Your LinkedIn Profile Link',
                        validators=[DataRequired()])
    availability = IntegerField('Enter Your Availability per Month (In hr)',
                        validators=[DataRequired()])
    submit = SubmitField('Submit Application')


class Add_Validator_Form(FlaskForm):
    pic = FileField('Select your profile photo')
    profile = StringField('Enter your linkedIn profile link',
                        validators=[DataRequired()])
    submit = SubmitField('Submit Application')
    

class Add_Legal_Advisor(FlaskForm):
    pic = FileField('Enter Your Profile Photo')
    profile = StringField('Enter Your LinkedIn Profile Link',
                        validators=[DataRequired()])
    description = StringField('Enter your current Job Description',
                        validators=[DataRequired()])
    city = StringField('Enter your current City',
                        validators=[DataRequired()])
    country = StringField('Enter your current Country',
                        validators=[DataRequired()])
    role = StringField('Enter your curent role (Legal Advisor)',
                        validators=[DataRequired()])
    awards = IntegerField('Enter the no of awards you have received',
                        validators=[DataRequired()])
    cases = IntegerField('Enter the no. of cases taken by you',
                        validators=[DataRequired()])
    advised = IntegerField('Enter the no. of advises provided by you',
                        validators=[DataRequired()])
    union = IntegerField('Enter the no. of Unions',
                        validators=[DataRequired()])
    year = IntegerField('Enter your Year of Experience',
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
    pic = FileField('Select Your Profile Photo')
    profile = StringField('Enter Your LinkedIn Profile Link',
                        validators=[DataRequired()])
    description = StringField('Enter Your Current Job Description',
                        validators=[DataRequired()])
    country = StringField('Enter Your Country of Residence',
                        validators=[DataRequired()])
    role = StringField('Enter Your Current Role',
                        validators=[DataRequired()])
    investment = IntegerField('No of investments done by you?',
                        validators=[DataRequired()])
    open_to = StringField('Funding Open to Audience: WorldWide / Within Country',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


class Add_Linkage_Agent(FlaskForm):
    pic = FileField('Select your profile photo')
    name = StringField('Enter your company name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Enter your contact no.', validators=[DataRequired()])
    email = StringField('Enter your email Id',
                        validators=[DataRequired(), Email()])
    link = StringField('Enter your site link',
                        validators=[DataRequired()])
    description = StringField('Enter your company description',
                        validators=[DataRequired()])
    country = StringField('Enter your current country of residence',
                        validators=[DataRequired()])
    state = StringField('Available in which state(write name of particular state or all)',
                        validators=[DataRequired()])
    service = StringField('Enter the services that you provide',
                        validators=[DataRequired()])
    open_to = StringField('Open for: National / International',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

class Add_Advertisement_Agent(FlaskForm):
    pic = FileField('Select Your Profile Photo')
    service = StringField('Enter the service that you provide',
                        validators=[DataRequired()])
    city = StringField('Enter your current City',
                        validators=[DataRequired()])
    state = StringField('Enter your current State',
                        validators=[DataRequired()])
    country = StringField('Enter your country of residence',
                        validators=[DataRequired()])
    availability = StringField('Availability: within City / within State / within Country',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

class Add_Position(FlaskForm):
    email = StringField('Enter your complete Email Id',
                        validators=[DataRequired(), Email()])
    phone = StringField('Enter your Contact No.', validators=[DataRequired()])
    job_title = StringField('Enter the job title',
                        validators=[DataRequired()])
    job_description = StringField('Enter the job description',
                        validators=[DataRequired()])
    number_open = IntegerField('Number of positions available',
                        validators=[DataRequired()])
    duration = StringField('what is the total Duration?(In Months)',
                        validators=[DataRequired()])
    stipend = IntegerField('Enter stipend per month',
                        validators=[DataRequired()])
    paid_unpaid = StringField('Is it Paid / Unpaid?',
                        validators=[DataRequired()])
    inoffice_wfh = StringField('Will it be inoffice / Work from Home?',
                        validators=[DataRequired()])
    location = StringField('What will be the location(Online if WFH)',
                        validators=[DataRequired()])
    total_workforce = IntegerField('What is your current total workforce', validators=[DataRequired()])
    female_workforce = IntegerField('How many female employees are there?', validators=[DataRequired()])
    category_workforce = IntegerField('How many category Workforce is present currently?', validators=[DataRequired()])
    submit = SubmitField('Submit Positions')

class Add_Open_Work(FlaskForm):
    pic = FileField('Select Your Profile Photo')
    profession = StringField('Enter Your Profession / Area of expertise', validators=[DataRequired()])
    linkedin_link = StringField('Enter Your Profile Link',
                        validators=[DataRequired()])
    resume_link = StringField('Enter Your Resume Link',
                        validators=[DataRequired()])
    portfolio_link = StringField('Enter Your Portfolio Link',
                        validators=[DataRequired()])
    about = StringField('Write About you',
                        validators=[DataRequired()])
    past_experience = StringField('Enter Your Past experiences in brief',
                        validators=[DataRequired()])
    year_of_experience = IntegerField('Enter Your Year of Experience',
                        validators=[DataRequired()])
    projects = StringField('Enter Your Projects',
                        validators=[DataRequired()]) 
    gender = StringField('Enter Your Gender (Female / Male)',
                        validators=[DataRequired()])
    courses = StringField('Enter Your Courses completed',
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
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Enter your Name"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Emter your Email id that you wan to share with everyone"})
    mail_body = StringField('Body',
                           validators=[DataRequired(), Length(min=2)], render_kw={"placeholder": "Share this message with others"})
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
    year = IntegerField('Update Your Year of Experience')
    cost = IntegerField('Update Cost per Session (In USD)')
    expertise = StringField('Update Your Area of Expertise')
    profile = StringField('Update Your LinkedIn Profile Link')
    availability = IntegerField('Update Your Availability per Month (In hr)')
    submit = SubmitField('Update Details')

class Update_Validator_Detail(FlaskForm):
    profile = StringField('Update your linkedIn profile link')
    submit = SubmitField('Update Details')

class Update_Linkage_Agent(FlaskForm):
    name = StringField('Update your company name')
    phone = StringField('Update your contact no.')
    email = StringField('Update your email Id')
    link = StringField('Update your site link')
    description = StringField('Update your company description')
    country = StringField('Update your current country of residence')
    state = StringField('Update available in which state')
    service = StringField('Update info of services that you provide')
    open_to = StringField('Open: National / International')
    submit = SubmitField('Update Details')

class Update_Advertiser_Detail(FlaskForm):
    service = StringField('Service that you provide')
    city = StringField('Update your current city')
    state = StringField('Update your current state')
    country = StringField('Update your current country')
    availability = StringField('Availablility: within City / within State / within Country')
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
    profile = StringField('Update your linkedIn profile link')
    description = StringField('Update your job description')
    city = StringField('Update your current city')
    country = StringField('Update your current country')
    role = StringField('Update your current role (Legal Advisor)')
    awards = IntegerField('Update your no. of awards')
    cases = IntegerField('Updaet your no. of cases')
    advised = IntegerField('Update your no. of advised')
    union = IntegerField('Update the no. of union')
    year = IntegerField('Update your year of experience')
    submit = SubmitField('Update Details')

class Update_Seeker_Detail(FlaskForm):
    profession = StringField('Update Your Profession / Area of expertise')
    linkedin_link = StringField('Update Profile Link')
    resume_link = StringField('Update Resume Link')
    portfolio_link = StringField('Update Portfolio Link')
    about = StringField('Update About you')
    past_experience = StringField('Update Past experiences in brief')
    year_of_experience = IntegerField('Update Year of Experience')
    projects = StringField('Update Projects') 
    gender = StringField('Update Gender (Female / Male)')
    courses = StringField('Update Courses completed')
    relocate = StringField('Willing to relocate: Yes / No')
    submit = SubmitField('Update Details')

class Update_Position_Detail(FlaskForm):
    email = StringField('Update Your Email Id')
    phone = StringField('Update Your Contact No.')
    job_title = StringField('Update Your Job Title')
    job_description = StringField('Update Your Job Description')
    number_open = IntegerField('Update Your Number of positions available')
    duration = StringField('Update Your Duration')
    stipend = IntegerField('Update Your Stipend')
    paid_unpaid = StringField('Update Option: Paid / Unpaid')
    inoffice_wfh = StringField('Update Your Inoffice / Work from Home')
    location = StringField('Update Your Location')
    submit = SubmitField('Update Position Details')

class Update_Project_Detail(FlaskForm):
    profile = StringField('Update Project\'s Profile Link')
    idea = StringField('Update Project\'s Idea')
    country = StringField('Update Project\'s Country of origin')
    industry = StringField('Update Project\'s Industry (IT / Food / etc.)')
    extra = StringField('Update Anything extra to add')
    category = StringField('Update Project\'s Category (Service / Product)')
    submit = SubmitField('Update Project Detail')

class Profit_Projection(FlaskForm):
    rnd = IntegerField('Relationships')
    marketing = IntegerField('Milestones')
    profit = IntegerField('Is_top500')
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

class Google_Assistant(FlaskForm):
    submit = SubmitField('Ask')

class Ad_recommend(FlaskForm):
    input = StringField('Input a word regarding your advertisement idea',
                        validators=[DataRequired()])
    submit = SubmitField('Recommend')

class Accelerator_Form(FlaskForm):
    name = StringField('Enter your full name',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter your full name"})
    email = StringField('Email Id',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter your email Id"})
    company = StringField('company',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter your company's Name"})
    program_name = StringField('Program Name',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the Program Name"})
    program_desc = StringField('Program Description',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the Program Description"})
    link = StringField('Link',
                        validators=[DataRequired()], render_kw={"placeholder": "Give link to official page for this program"})
    location = StringField('Company Location',
                        validators=[DataRequired()], render_kw={"placeholder": "What is the Company's Location?"})
    open_to = StringField('Open to(within country / worldwide)',
                        validators=[DataRequired()], render_kw={"placeholder": "Open to(within country / worldwide)"})
    resources = StringField('Resources provided to startups',
                        validators=[DataRequired()], render_kw={"placeholder": "Resources provided to startups"})
    submit = SubmitField('Submit')

class Event_Form(FlaskForm):
    summary = StringField('summary',
                        validators=[DataRequired()], render_kw={"placeholder": "Summarize the event in a line"})
    location = StringField('location',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the location of event"})
    description = StringField('description',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the description of the event"})
    start_dateTime = StringField('start time',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the start time for the event"})
    start_timeZone = StringField('start zone',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the start zone"})
    end_dateTime = StringField('end time',
                        validators=[DataRequired()], render_kw={"placeholder": "Ehter the end time for the event"})
    end_timeZone = StringField('end zone',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter the end zone"})
    attendees_one = StringField('Attendees',
                        validators=[DataRequired()], render_kw={"placeholder": "Enter Attendees email id(comma seperated)"})
    submit = SubmitField('Submit')

class Test_Form(FlaskForm):
    name = StringField('Enter your name')
    email = StringField('Enter your email')
    startup_name = StringField('Enter your startup name')
    test_details = StringField('Enter your test details')
    location = StringField('Enter your location')
    age_range = StringField('Enter your age range')
    industry = StringField('Enter your industry')
    credits_given = StringField('Enter your credits given')
    link = StringField('Enter your official link')
    submit = SubmitField('Submit')

class Challenges(FlaskForm):
    challenge_name = StringField('challenge_name')
    email = StringField('email')
    challenge_desc = StringField('challenge_desc')
    eligibility = StringField('eligibility')
    location = StringField('location')
    company_name = StringField('company_name')
    theme = StringField('theme')
    relevant_industry = StringField('relevant_industry')
    incentives = StringField('Incentives')
    timeline = StringField('timeline')
    submit = SubmitField('Submit')