from flask_wtf import FlaskForm
from wtforms import (PasswordField, StringField, SubmitField, ValidationError, DateField, BooleanField, 
                                DateTimeField, IntegerField, SelectField, RadioField, TextField, 
                                TextAreaField, SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo
from models import Admin, Employee


class AdminSignUpForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField("Comfirm Password:", validators=[DataRequired()])
    signup = SubmitField('SignUp')

    def validate_username(self, field):
        if Admin.query.filter(Admin.username == field.data).first():
            raise ValidationError('Sorry, this username already exists!')

class AdminLoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddEmployeeForm(FlaskForm):
    pin = IntegerField("Personal Identification Number (PIN):", validators=[DataRequired()])
    title = RadioField("Title", choices=[('mr', 'Mr'), ('miss', 'Miss'),
                                  ('mrs', 'Mrs'), ('dr', 'Dr'), ('engr', 'Engr'),('prof', 'Prof')], validators=[DataRequired()])
    name = StringField('Name (In Full)', validators=[DataRequired()])
    appointedDesignation = StringField("Appointed Designation:", validators=[DataRequired()])
    dateOfBirth =  DateTimeField('Date Of Birth', format='%d/%m/%y', validators=[DataRequired()])
    dateOfFirstAppointment = DateTimeField('Date of First Appointment', 
                                format='%d/%m/%y', validators=[DataRequired()])
    gradeLevel = StringField("Grade Level:", validators=[DataRequired()])
    salaryPerAnnum = IntegerField("First Salary Per Annum:", validators=[DataRequired()])
    nationality = StringField("Nationality:", validators=[DataRequired()])
    stateOfOrigin = StringField("State of Origin:", validators=[DataRequired()])
    homeTown = StringField("Home Town", validators=[DataRequired()])
    localGovernment = StringField("Local Government Area:", validators=[DataRequired()])
    senatorialDistrict = StringField("Senatorial District:", validators=[DataRequired()])
    maritalStatus = SelectField('Indicate your marital status:',
                                choices= [('single', 'Single'), ('married', 'Married'),
                 ('divorced', 'Divorced'), ('widowed', 'Widowed')], validators=[DataRequired()])
    noOfChildren = IntegerField("Indicate number of Children:")
    agesOfChildren = StringField("Indicate their ages respectively:")
    nextOfKin= StringField("Next of Kin and Addresses respectively (*only two required please):", validators=[DataRequired()])
    presentAddress = StringField("Present Address:", validators=[DataRequired()])
    permanentHomeAddress = StringField("Permanent Home Adress:", validators=[DataRequired()])
    email = StringField("*E-mail Address:", validators=[DataRequired()])
    phoneNo = IntegerField("Phone Number:", validators=[DataRequired()])
    educationalCert = StringField("Educational Certificates /Diploma (with dates):", validators=[DataRequired()])
    professionalQualifications = StringField("Professional Qualifications, Certificates, Honors, etc. (with dates):")
    qualification = RadioField("What's your educational qualification?",
                                                   choices=[('school_cert', 'School_cert'), ('bsc', 'Bsc'),
                                                            ('msc', 'Msc'), ('phd', 'Phd'), ('others', 'Others')], validators=[DataRequired()])
    religion = SelectField('indicate your religion:', choices= [('christianity', 'Christianity'),
                                                                  ('islam',  'Islam'), ('traditional', 'Traditional')], validators=[DataRequired()])
    submit = SubmitField('Submit')