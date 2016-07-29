from openerp import models, fields, api
import collections
import datetime
from datetime import date


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


class account_analytic_account_signable(models.Model):
    _inherit = ['sale.subscription']
    
    agreement_date = fields.Date(string='Agreement date', default=date.today().strftime('%Y-%m-%d'))
    preventive_maintenance = fields.Boolean(string="Preventive Maintenance", default=False)
    automatic_reneval_of_license = fields.Boolean(string="Automatic reneval of license", default=False)
    monitoring = fields.Boolean(string="Monitoring", default=False)
    backup = fields.Boolean(string="Backup", default=False)

    def get_date_from_string_format(self, a_date, format_from, format_to):
        return datetime.datetime.strptime(a_date, format_from).date().strftime(format_to)
    
    def is_tariff(self, account_id, product_id):
        cr = self.env.cr
        uid = self.env.user.id
        account_analytic_account_obj = self.pool.get('sale.subscription')
        account_analytic_accounts = account_analytic_account_obj.search(cr, uid, [('id','=',account_id)])
        if account_analytic_accounts:
            account_analytic_account = account_analytic_account_obj.browse(cr, uid, account_analytic_accounts[0])
            if account_analytic_account.contract_type.timesheet_product.id == product_id:
                return True
            else:
                return False           
        else:
            return False
    
    def is_travel_cost(self, account_id, product_id):
        cr = self.env.cr
        uid = self.env.user.id
        account_analytic_account_obj = self.pool.get('sale.subscription')
        account_analytic_accounts = account_analytic_account_obj.search(cr, uid, [('id','=',account_id)])
        if account_analytic_accounts:
            account_analytic_account = account_analytic_account_obj.browse(cr, uid, account_analytic_accounts[0])
            if account_analytic_account.on_site_product.id == product_id:
                return True
            else:
                return False           
        else:
            return False
    
    def get_contract_type_products(self):
        cr = self.env.cr
        uid = self.env.user.id
        product_product_obj = self.pool.get('product.product')
        product_product_ids = product_product_obj.search(cr, uid, [('active','=',True),('sale_ok','=',True),('default_code','ilike','SUPPORT_BL')])
        products = []
        if product_product_ids:
            for product in product_product_obj.browse(cr, uid, product_product_ids):
               
                yearly_minimum = int(product.default_code[10:]) #ie.: SUPPORT_BL100
                monthly_installment = product.lst_price*yearly_minimum/12
                #create a round number
                if monthly_installment > 100:
                    monthly_installment = int(round(monthly_installment/100, 1)*100)

                if yearly_minimum > 0:
                    sla = True
                else:
                    sla = False
                   
                
                product_dict = {
                    'name' : product.name,
                    'price' : product.lst_price,
                    'yearly_minimum' : yearly_minimum,
                    'monthly_installment' : monthly_installment,
                    'sla' : sla,
                    'product_id': product.id,
                    }                
                products.append(product_dict)
            products = sorted(products , key=lambda prod: "%03d" % (prod['yearly_minimum']))
        return products
    
    def get_travel_products(self):
        cr = self.env.cr
        uid = self.env.user.id
        product_product_obj = self.pool.get('product.product')
        product_product_ids = product_product_obj.search(cr, uid, [('active','=',True),('sale_ok','=',True),('default_code','ilike','TRAV'),('name','ilike','Travelling costs')])
        products = []
        if product_product_ids:
            for product in product_product_obj.browse(cr, uid, product_product_ids):
                km = product.default_code[4:] #ie.: TRAV15
                if RepresentsInt(km):
                    product_dict = {
                        'km' : int(km),
                        'price' : product.lst_price,
                        'product_id': product.id,
                        }                
                    products.append(product_dict)
                else:
                    product_dict = {
                        'km' : 999,
                        'price' : product.lst_price,
                        'product_id': product.id,
                        }                
                    products.append(product_dict)
            products = sorted(products , key=lambda prod: "%03d" % (prod['km']))
        return products