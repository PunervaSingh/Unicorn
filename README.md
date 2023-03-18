# Phoenix - Rise From The Ashes
### One-Stop Platform For Budding Entrepreneurs.
* An integrated platform for guiding aspiring entrepreneurs, idea nurturing, connecting with incubators, extending mentoring and handholding support, creating financial and marketing linkages, and complying with legal and statutory compliances for starting a business. 
* This single-window platform for entrepreneurs will bring all the stakeholders under one umbrella.

### 📌 Table of Contents
* [Toolchain](#toolchain)
* [Features](#features)
* [Application Overview](#overview)
* [Learnings](#learning)
* [Challenges faced](#challenges)
* [Future Scope/ What's next?](#scope)
* [Resources](#resources)
* [Setup](#setup)
* [Demo](#demo)
* [FAQs](#faqs)
* [Authors](#authors)
* [Bug Reporting](#bug)
* [Feature Requests](#feature-request)


<a id="toolchain"></a>
## 💻 Toolchain

<img alt="HTML" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/><img alt="CSS" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/><img alt="Javascript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/><img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/><img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" /><img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" /><img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/><img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>

***Frontend*** : HTML, CSS, JS, Bootstrap

***Backend*** : Flask, Jinja

***Database*** : SQLite

***Libraries*** : Pandas, Matplotlib, Seaborn, Pycountry

***API*** : Google Translate, Kommunicate, Listennotes, Quotable, Razorpay

***Other*** : Dialogflow, Git - Version Control, Visual Studio Code


<a id="features"></a>
## 🚀 Features
- Counselling/ Guidance 
- Idea validation 
- Connecting with Incubators/ Accelerators 
- Connecting with industry mentors ideally those who run businesses, for a project or Start-up related discussions. Connect to the interested private sector (individuals, organizations) willing to provide funding support and invest in these enterprises. 
- Registration of the company 
- Mentoring and handholding of new enterprises in Tier I & II and villages in India.
- Financial linkages with various Govt. Sponsored Schemes 
- Linkage with Investor/ Funding Agencies/ Banks 
- Identifying markets and provide market linkage for products and services, with provision for transactions between parties through the same platform. 
- Connecting with Suppliers 
- Linkage with Required Human Resources 
- Legal and Statutory Compliances for ease of starting a business 
- Escort services 
- Policy guidance 
- Making vocal the local products (advertisement guideline guidance) 
- Connect with a pool of skilled laborers for the production/ service generation of the business. 
- Linkage with various Government sponsored schemes for finance, and loans.
- Track delivery of products on the go 
- [Add more features](#feature-request)...

<a id="overview"></a>
## 📖 Application Overview
### Home Page
![Website Image]()
### Register Page 
![Website Image]()
### Login Page
![Website Image]()
### Women Entrepreneur Page
![Website Image]()
### Idea Generation Page
![Website Image]()
### StartUps Page
![Website Image]()
### Mentorship/Counsellor Page 
![Website Image]()
### Legal Advisor Page 
![Website Image]()
### Linkage Agent Page
![Website Image]()
<!-- ### Terms and condition Page 
![Website Image](flaskblog/static/img/terms.png?raw=true "Title") -->
### Team Building Page 
![Website Image]()
### Advertisement Agent Page
![Website Image]()
### Funding Agent Page
![Website Image]()
### Profile Page
![Website Image]()
### Motivational Corner Page
![Website Image]()
### Trending Startups Page
![Website Image]()
### Brand Name Genrator Page
![Website Image]()

<a id="learning"></a>
## 💡 Learnings
- Establishing connections between different tables in the database and retrieving information based on the currently logged-in user.
- Using multiple flask extensions such as flask mail, flask admin, etc.
- Process to call an API and display data on our website.
- Uploading images and integrating them with the database.
- Implementing Dialogflow bot into our web application with the help of kommunicate.

<a id="challenges"></a>
## 💡 Challenges faced
- Technical setup issue while working with SMTP requests using flask mail extension.
- Integrating various schemas of the database and keeping track of the status of requests.
- Gathering dataset for performing EDA regarding startup success rate.
- Designing admin dashboard with built-in styling.
- Finding free APIs that met all of our requirements.

<a id="scope"></a>
## 🚧 Future Scope/ What's next?

- [ ] Building Voice Assistant and webpage customization feature for people with visual disabilities
- [ ] Making the website responsive for multiple devices
- [ ] Providing packaging feature for startups (AI-generated design from inputted keywords/phrases)
- [ ] Update job description for different job tracks
- [ ] Implementing raw material with Map API to search nearby suppliers

<a id="resources"></a>
## 📚 Resources

- [HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JS Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)


<a id="setup"></a>
## ⚙️ Set Up

Take These Steps to configure the Project :

* Clone The Repository
```
git clone https://github.com/PunervaSingh/Phoenix
```

* Create a virtual environment(Code is for Windows Only)
```
virtualenv venv 
```

* Download all required modules using
```
pip install -r requirements.txt
```

* Create database by running the following command using python in command prompt
```
from flask_app import db
db.create_all()
exit()
```

*  Run the app.py file in command prompt 
```
python app.py
```
* Now Head on to ['http://127.0.0.1:5000/'](http://127.0.0.1:5000/)

## 💻 Demo

Insert gif or link to demo

## 🙋 FAQs

### Why Phoenix?

We recognised that getting started with one's own business is often a daunting task. So many times, entrepreneurs have great ideas but lack the execution because of not knowing much about the managerial or financial aspects of running their business. Phoenix brings together all of the stakeholders under one umbrella to faciliate efficient and convenient collaboration among all parties, thereby creating a win-win situation.

### What are the pre-requisites of running this application locally

You must have python and an IDE installed in your local system. The rest of the steps are provided in the "Run Locally" section above


<a id="authors"></a>
## ✍️ Authors

Contributors names and contact info :

Punerva Singh<br> 
[@Linkedin](https://www.linkedin.com/in/punerva-singh-958305204)
<br>
[@Github](https://github.com/punervasingh)
<br>

Samya Jain<br>
[@Linkedin](https://www.linkedin.com/in/samya-jain-a68443204)
<br>
[@Github](https://github.com/samya02)
<br>

Sanya Bansal<br> 
[@Linkedin](https://www.linkedin.com/in/bansal-sanya/)
<br>
[@Github](https://github.com/san-ya)
<br>


<a id="bug"></a>
## 🐛 Bug Reporting
Feel free to [open an issue](https://github.com/PunervaSingh/Phoenix/issues) on GitHub if you find bugs.

<a id="feature-request"></a>
## ⭐ Feature Request
- Feel free to [open an issue](https://github.com/PunervaSingh/Phoenix/issues) on GitHub to add any additional features you feel could enhance this project.  