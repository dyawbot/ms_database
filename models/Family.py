# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ms_Family(models.Model):
    _name = 'ms.family'
    _rec_name = 'ms_household'
    


    ms_household = fields.Char(string="Respondent Code", required=True)
    ms_family_members = fields.One2many('ms.add.family', 'ms_household_name', string = "Household")
    
  


class Ms_add_family(models.Model):
    _name = 'ms.add.family'

    ms_household_name = fields.Many2one('ms.family', string = "Household name")

    ms_lastname =  fields.Char(string = "Lastname", required=True)
    ms_firstname = fields.Char(string = "Firstname", required=True)
    ms_middlename = fields.Char(string = "Middlename", required=True)
    ms_gender = fields.Char(string = "Gender")
    ms_rel_to_the_head = fields.Char(string = "Relationship to the Household Head")
    ms_residence_permanent =fields.Selection([('yes', 'Yes'), ('no', 'No')], string = "If Residence is Permanent")
    
    ms_barangay = fields.Selection([('capaculan', 'Capaculan'), ('calumpang', 'Calumpang'), ('poblacion_west', 'Poblacion West')],string ="Barangay")

    ms_home_address =fields.Char(string='Home Address')
    ms_num_years_in_the_said_address = fields.Integer(string = "Number of Years in the said Address")
    ms_age = fields.Char(string = "Age")
    ms_birthday = fields.Date("string=Birthday")
    ms_with_birth_certificate = fields.Selection([('yes', 'Yes'), ('no', 'No')], string = "With Birth Certificate")
    ms_beneficiaries = fields.Selection([('_4ps', '4P\'s'), ('slp', 'SLP')], string = "Beneficiaries")
    ms_religion = fields.Selection([('christians', 'Christians'), ('inc', 'INC'), ('traditional', 'Traditional'), ('muslims', 'Musilims')], string = "Religions")
    ms_if_with_specific_type_of_disability = fields.Char(string="If with Disability Specific Type of Disability")
    ms_provided_with_eccd_service =fields.Selection([('yes', 'Yes'), ('no', 'No')], string = "Provided with ECCD Service")
    ms_if_yes_specify = fields.Char(string = "If Yes, Specify ECCD Facility")




# /mnt/hgfs/dot/MsDataBase/ms_database