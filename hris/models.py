from django.db import models
from django.contrib.auth.models import User
from datetime import time
# Create your models here.



class Employee(models.Model):
    # PERSONAL INFORMATION 
    user = models.OneToOneField(User, null=True, blank=True,unique=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="Default_pfp.jpg", null=True, blank=True)
    employee_id = models.CharField(max_length=20,unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    employment_status = models.CharField(max_length=100, null=True, blank=True)
    name_ext = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True, null=True)
    gsis_no = models.CharField(max_length=20, blank=True, null=True)
    pagibig_no = models.CharField(max_length=20, blank=True, null=True)
    philhealth_no = models.CharField(max_length=20, blank=True, null=True)
    sss_no = models.CharField(max_length=20, blank=True, null=True)
    tin_no = models.CharField(max_length=20, blank=True, null=True)
    agency_em = models.CharField(max_length=100, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)

    # PERSONAL ADDRESS
    residential_house_no = models.CharField(max_length=10, blank=True, null=True)
    residential_street = models.CharField(max_length=100, blank=True, null=True)
    residential_subd = models.CharField(max_length=100, blank=True, null=True)
    residential_brgy = models.CharField(max_length=100, blank=True, null=True)
    residential_city = models.CharField(max_length=100, blank=True, null=True)
    residential_province = models.CharField(max_length=100, blank=True, null=True)
    residential_zipcode = models.CharField(max_length=10, blank=True, null=True)
    permanent_house_no = models.CharField(max_length=10, blank=True, null=True)
    permanent_street = models.CharField(max_length=100, blank=True, null=True)
    permanent_subd = models.CharField(max_length=100, blank=True, null=True)
    permanent_brgy = models.CharField(max_length=100, blank=True, null=True)
    permanent_city = models.CharField(max_length=100, blank=True, null=True)
    permanent_province = models.CharField(max_length=100, blank=True, null=True)
    permanent_zipcode = models.CharField(max_length=10, blank=True, null=True)

    #PERSONAL CONTACT
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)

    # FAMILY BACKGROUND
    spouse_surname = models.CharField(max_length=100, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_name_ext = models.CharField(max_length=10, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    spouse_employer = models.CharField(max_length=100, blank=True, null=True)
    spouse_business_address = models.CharField(max_length=200, blank=True, null=True)
    spouse_telephone = models.CharField(max_length=20, blank=True, null=True)

    children1_name = models.CharField(max_length=100, blank=True, null=True)
    children1_BDAY = models.DateField(blank=True, null=True)

    children2_name = models.CharField(max_length=100, blank=True, null=True)
    children2_BDAY = models.DateField(blank=True, null=True)

    children3_name = models.CharField(max_length=100, blank=True, null=True)
    children3_BDAY = models.DateField(blank=True, null=True)

    children4_name = models.CharField(max_length=100, blank=True, null=True)
    children4_BDAY = models.DateField(blank=True, null=True)

    children5_name = models.CharField(max_length=100, blank=True, null=True)
    children5_BDAY = models.DateField(blank=True, null=True)

    children6_name = models.CharField(max_length=100, blank=True, null=True)
    children6_BDAY = models.DateField(blank=True, null=True)

    children7_name = models.CharField(max_length=100, blank=True, null=True)
    children7_BDAY = models.DateField(blank=True, null=True)

    children8_name = models.CharField(max_length=100, blank=True, null=True)
    children8_BDAY = models.DateField(blank=True, null=True)

    children9_name = models.CharField(max_length=100, blank=True, null=True)
    children9_BDAY = models.DateField(blank=True, null=True)

    children10_name = models.CharField(max_length=100, blank=True, null=True)
    children10_BDAY = models.DateField(blank=True, null=True)

    children11_name = models.CharField(max_length=100, blank=True, null=True)
    children11_BDAY = models.DateField(blank=True, null=True)

    children12_name = models.CharField(max_length=100, blank=True, null=True)
    children12_BDAY = models.DateField(blank=True, null=True)

    father_surname = models.CharField(max_length=100, blank=True, null=True)
    father_first_name = models.CharField(max_length=100, blank=True, null=True)
    father_middle_name = models.CharField(max_length=100, blank=True, null=True)
    father_name_ext = models.CharField(max_length=10, blank=True, null=True)
    mother_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_first_name = models.CharField(max_length=100, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=100, blank=True, null=True)


    # EDUCATIONAL PROGRAM

    # ELEMENTARY
    ELEMENTARY = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    ELEMENTARY_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    ELEMENTARY_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)

    # SECONDARY
    SECONDARY = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    SECONDARY_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    SECONDARY_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)


    # VOCATIONAL
    VOCATIONAL = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    VOCATIONAL_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    VOCATIONAL_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)


    # COLLEGE
    COLLEGE = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    COLLEGE_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    COLLEGE_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)

    # GRADUATE
    GRADUATE = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    GRADUATE_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    GRADUATE_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)

    # DATE FILL UP
    DATE_OF_FILLUP = models.DateField(blank=True, null=True)
    
    # C2
    credentials = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 1
    rating = models.CharField(max_length=5, blank=True, null=True)
    exam_date = models.DateField(null=True, blank=True)
    exam_location = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=20, blank=True, null=True)
    license_date = models.DateField(null=True, blank=True)
    credentials2 = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 2
    rating2 = models.CharField(max_length=5, blank=True, null=True)
    exam_date2 = models.DateField(null=True, blank=True)
    exam_location2 = models.CharField(max_length=100, blank=True, null=True)
    license_number2 = models.CharField(max_length=20, blank=True, null=True)
    license_date2 = models.DateField(null=True, blank=True)
    credentials3 = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 3
    rating3 = models.CharField(max_length=5, blank=True, null=True)
    exam_date3 = models.DateField(null=True, blank=True)
    exam_location3 = models.CharField(max_length=100, blank=True, null=True)
    license_number3 = models.CharField(max_length=20, blank=True, null=True)
    license_date3 = models.DateField(null=True, blank=True)
    credentials4 = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 4
    rating4 = models.CharField(max_length=5, blank=True, null=True)
    exam_date4 = models.DateField(null=True, blank=True)
    exam_location4 = models.CharField(max_length=100, blank=True, null=True)
    license_number4 = models.CharField(max_length=20, blank=True, null=True)
    license_date4 = models.DateField(null=True, blank=True)
    credentials5 = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 5
    rating5 = models.CharField(max_length=5, blank=True, null=True)
    exam_date5 = models.DateField(null=True, blank=True)
    exam_location5 = models.CharField(max_length=100, blank=True, null=True)
    license_number5 = models.CharField(max_length=20, blank=True, null=True)
    license_date5 = models.DateField(null=True, blank=True)
    credentials6 = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 6
    rating6 = models.CharField(max_length=5, blank=True, null=True)
    exam_date6 = models.DateField(null=True, blank=True)
    exam_location6 = models.CharField(max_length=100, blank=True, null=True)
    license_number6 = models.CharField(max_length=20, blank=True, null=True)
    license_date6 = models.DateField(null=True, blank=True)
    credentials7 = models.CharField(max_length=100, blank=True, null=True)                     #pds2 Civil Service Eligibility row 7
    rating7 = models.CharField(max_length=5, blank=True, null=True)
    exam_date7 = models.DateField(null=True, blank=True)
    exam_location7 = models.CharField(max_length=100, blank=True, null=True)
    license_number7 = models.CharField(max_length=20, blank=True, null=True)
    license_date7 = models.DateField(null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 1
    date_to = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    workplace_name = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade = models.CharField(max_length=20, blank=True, null=True)
    step = models.CharField(max_length=20, blank=True, null=True)
    status_appointment = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N = models.CharField(max_length=1, blank=True, null=True)
    date_from2 = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 2
    date_to2 = models.DateField(null=True, blank=True)
    position2 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name2 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary2 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade2 = models.CharField(max_length=20, blank=True, null=True)
    step2 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment2 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N2 = models.CharField(max_length=1, blank=True, null=True)
    date_from3 = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 3
    date_to3 = models.DateField(null=True, blank=True)
    position3 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name3 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary3 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade3 = models.CharField(max_length=20, blank=True, null=True)
    step3 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment3 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N3 = models.CharField(max_length=1, blank=True, null=True)
    date_from4 = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 4
    date_to4 = models.DateField(null=True, blank=True)
    position4 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name4 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary4 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade4 = models.CharField(max_length=20, blank=True, null=True)
    step4 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment4 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N4 = models.CharField(max_length=1, blank=True, null=True)
    date_from5 = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 5
    date_to5 = models.DateField(null=True, blank=True)
    position5 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name5 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary5 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade5 = models.CharField(max_length=20, blank=True, null=True)
    step5 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment5 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N5 = models.CharField(max_length=1, blank=True, null=True)
    date_from6 = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 6
    date_to6 = models.DateField(null=True, blank=True)
    position6 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name6 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary6 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade6 = models.CharField(max_length=20, blank=True, null=True)
    step6 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment6 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N6 = models.CharField(max_length=1, blank=True, null=True)
    date_from7 = models.DateField(null=True, blank=True)                                        #pds2 Work Experience row 7
    date_to7 = models.DateField(null=True, blank=True)
    position7 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name7 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary7 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade7 = models.CharField(max_length=20, blank=True, null=True)
    step7 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment7 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N7 = models.CharField(max_length=1, blank=True, null=True)

    organization_name_1 = models.CharField(max_length=150, blank=True, null=True)           #For PDS3 VI row 1
    organization_address_1 = models.CharField(max_length=100, blank=True, null=True)
    from_date_1 = models.DateField(blank=True, null=True)
    to_date_1 = models.DateField(blank=True, null=True)
    number_of_hours_1 = models.PositiveIntegerField(default=0)
    position_nature_of_work_1 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_2 = models.CharField(max_length=150, blank=True, null=True )          #For PDS3 VI row 2
    organization_address_2 = models.CharField(max_length=100, blank=True, null=True)
    from_date_2 = models.DateField(blank=True, null=True)
    to_date_2 = models.DateField(blank=True, null=True)
    number_of_hours_2 = models.PositiveIntegerField(default=0)
    position_nature_of_work_2 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_3 = models.CharField(max_length=150, blank=True, null=True )          #For PDS3 VI row 3
    organization_address_3 = models.CharField(max_length=100, blank=True, null=True)
    from_date_3 = models.DateField(blank=True, null=True)
    to_date_3 = models.DateField(blank=True, null=True)
    number_of_hours_3 = models.PositiveIntegerField(default=0)
    position_nature_of_work_3 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_4 = models.CharField(max_length=150, blank=True, null=True )          #For PDS3 VI row 4
    organization_address_4 = models.CharField(max_length=100, blank=True, null=True)
    from_date_4 = models.DateField(blank=True, null=True)
    to_date_4 = models.DateField(blank=True, null=True)
    number_of_hours_4 = models.PositiveIntegerField(default=0)
    position_nature_of_work_4 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_5 = models.CharField(max_length=150, blank=True, null=True )          #For PDS3 VI row 5
    organization_address_5 = models.CharField(max_length=100, blank=True, null=True)
    from_date_5 = models.DateField(blank=True, null=True)
    to_date_5 = models.DateField(blank=True, null=True)
    number_of_hours_5 = models.PositiveIntegerField(default=0)
    position_nature_of_work_5 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_6 = models.CharField(max_length=150, blank=True, null=True)           #For PDS3 VI row 6
    organization_address_6 = models.CharField(max_length=100, blank=True, null=True)
    from_date_6 = models.DateField(blank=True, null=True)
    to_date_6 = models.DateField(blank=True, null=True)
    number_of_hours_6 = models.PositiveIntegerField(default=0)
    position_nature_of_work_6 = models.CharField(max_length=150, blank=True, null=True)     #For PDS3 VI row 7
    organization_name_7 = models.CharField(max_length=150, blank=True, null=True)
    organization_address_7 = models.CharField(max_length=100, blank=True, null=True)
    from_date_7 = models.DateField(blank=True, null=True)
    to_date_7 = models.DateField(blank=True, null=True)
    number_of_hours_7 = models.PositiveIntegerField(default=0)
    position_nature_of_work_7 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_1 = models.CharField(max_length=150, blank=True, null=True)            #For PDS3 VII row 1
    from_date_A1 = models.DateField(blank=True, null=True)
    to_date_A1 = models.DateField(blank=True, null=True)
    number_of_hours_A1 = models.PositiveIntegerField(default=0)
    type_of_ld_1 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_1 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_2 = models.CharField(max_length=150, blank=True, null=True)            #For PDS3 VII row 2
    from_date_A2 = models.DateField(blank=True, null=True)
    to_date_A2 = models.DateField(blank=True, null=True)
    number_of_hours_A2 = models.PositiveIntegerField(default=0)
    type_of_ld_2 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_2 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_3 = models.CharField(max_length=150, blank=True, null=True)             #For PDS3 VII row 3
    from_date_A3 = models.DateField(blank=True, null=True)
    to_date_A3 = models.DateField(blank=True, null=True)
    number_of_hours_A3 = models.PositiveIntegerField(default=0)
    type_of_ld_3 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_3 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_4 = models.CharField(max_length=150, blank=True, null=True)             #For PDS3 VII row 4
    from_date_A4 = models.DateField(blank=True, null=True)
    to_date_A4 = models.DateField(blank=True, null=True)
    number_of_hours_A4 = models.PositiveIntegerField(default=0)
    type_of_ld_4 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_4 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_5 = models.CharField(max_length=150, blank=True, null=True)             #For PDS3 VII row 5
    from_date_A5 = models.DateField(blank=True, null=True)
    to_date_A5 = models.DateField(blank=True, null=True)
    number_of_hours_A5 = models.PositiveIntegerField(default=0)
    type_of_ld_5 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_5 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_6 = models.CharField(max_length=150, blank=True, null=True)             #For PDS3 VII row 6
    from_date_A6 = models.DateField(blank=True, null=True)
    to_date_A6 = models.DateField(blank=True, null=True)
    number_of_hours_A6 = models.PositiveIntegerField(default=0)
    type_of_ld_6 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_6 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_7 = models.CharField(max_length=150, blank=True, null=True)             #For PDS3 VII row 7
    from_date_A7 = models.DateField(blank=True, null=True)
    to_date_A7 = models.DateField(blank=True, null=True)
    number_of_hours_A7 = models.PositiveIntegerField(default=0)
    type_of_ld_7 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_7 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_1 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 1
    special_skills_1 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_1 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_2 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 2
    special_skills_2 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_2 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_3 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 3
    special_skills_3 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_3 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_4 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 4
    special_skills_4 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_4 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_5 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 5
    special_skills_5 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_5 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_6 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 6
    special_skills_6 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_6 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_7 = models.CharField(max_length=150, blank=True, null=True)     #For PDS3 VIII row 7
    special_skills_7 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_7 = models.CharField(max_length=150, blank=True, null=True)

    ref_name_1 = models.CharField(max_length=100, blank=True, null=True)                      #For PDS4 REFERENCES row 1
    ref_adress1 = models.CharField(max_length=100, blank=True, null=True)
    ref_num_1 = models.CharField(max_length=20, blank=True, null=True)
    ref_name_2 = models.CharField(max_length=100, blank=True, null=True)                      #For PDS4 REFERENCES row 2
    ref_adress_2 = models.CharField(max_length=100, blank=True, null=True)
    ref_num_2 = models.CharField(max_length=20, blank=True, null=True)
    ref_name_3 = models.CharField(max_length=100, blank=True, null=True)                      #For PDS4 REFERENCES row 3
    ref_adress_3 = models.CharField(max_length=100, blank=True, null=True)
    ref_num_3 = models.CharField(max_length=20, blank=True, null=True)
    gov_s_id = models.CharField(max_length=50, blank=True, null=True)                         #For PDS4 REFERENCES row 1
    ids_num = models.CharField(max_length=20, blank=True, null=True)
    date_place_i = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.surname}"


class OfficialTime(models.Model):
    employee_id = models.CharField(max_length=20)
    day = models.CharField(max_length = 10)
    semester_id = models.CharField(max_length = 10, null= True, blank = True)
    official_office_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_office_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_honorarium_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_honorarium_time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_servicecredit_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_servicecredit_time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_overtime_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_overtime_time_out = models.TimeField(default='00:00:00', null=True, blank=True)


class AttendanceRecord(models.Model):
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    break_in = models.TimeField(default='00:00:00', null=True, blank=True)
    break_out = models.TimeField(default='00:00:00', null=True, blank=True)
    time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    surplusHour_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    surplusHour_time_out = models.TimeField(default='00:00:00', null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.date}" if self.date else self.employee_id


class EditLogs(models.Model):
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    logged_data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)