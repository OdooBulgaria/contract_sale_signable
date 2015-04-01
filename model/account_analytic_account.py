from openerp import models, fields, api
import collections
import datetime
from datetime import date

class account_analytic_account_signable(models.Model):
    _inherit = ['account.analytic.account']
    
    agreement_date = fields.Date('Agreement date')
    preventive_maintenance = fields.Boolean(string="Preventive Maintenance", default=False)
    automatic_reneval_of_license = fields.Boolean(string="Automatic reneval of license", default=False)
    monitoring = fields.Boolean(string="Monitoring", default=False)
    backup = fields.Boolean(string="Backup", default=False)

    def get_date_from_string_format(self, a_date, format_from, format_to):
        return datetime.datetime.strptime(a_date, format_from).date().strftime(format_to)
    
    def is_tariff(self, id, price, hour):
        cr = self.env.cr
        uid = self.env.user.id
        account_analytic_account_obj = self.pool.get('account.analytic.account')
        account_analytic_accounts = account_analytic_account_obj.search(cr, uid, [('id','=',id)])
        if account_analytic_accounts:
            account_analytic_account = account_analytic_account_obj.browse(cr, uid, account_analytic_accounts[0])
            if str(hour) in account_analytic_account.contract_type.timesheet_product.name and account_analytic_account.timesheet_product_price == price:
                return True
            else:
                return False           
        else:
            return False
    
    def is_travel_cost(self, id, price):
        cr = self.env.cr
        uid = self.env.user.id
        account_analytic_account_obj = self.pool.get('account.analytic.account')
        account_analytic_accounts = account_analytic_account_obj.search(cr, uid, [('id','=',id)])
        if account_analytic_accounts:
            account_analytic_account = account_analytic_account_obj.browse(cr, uid, account_analytic_accounts[0])
            if account_analytic_account.on_site_product.lst_price == price:
                return True
            elif account_analytic_account.on_site_product.lst_price == 0:
                return True
            else:
                return False           
        else:
            return False
    
    """
    def get_contract_type_products(self):
        result = []
        cr = self.env.cr
        uid = self.env.user.id
        account_analytic_account_type_obj = self.pool.get('account.analytic.account.type')
        account_analytic_account_types = account_analytic_account_type_obj.search(cr, uid, [])
        if account_analytic_account_types:
            product_dict = {}
            for type in account_analytic_account_type_obj.browse(cr, uid, account_analytic_account_types):
                if type.timesheet_product:
                    product_dict[type.timesheet_product.name] = type.timesheet_product.lst_price
            #product_dict = collections.OrderedDict(sorted(product_dict.items()))
            #for product_name in product_dict.keys():
            for key, value in sorted(product_dict.iteritems(), key=lambda (k,v): (v,k)):
                res = {
                    'name' : key,
                    'price' : value,
                    }                
                result.append(res)
        return result
    
    def get_travel_products(self):
        result = []
        cr = self.env.cr
        uid = self.env.user.id
        product_product_obj = self.pool.get('product.product')
        product_products = product_product_obj.search(cr, uid, [('name','ilike','Travelling costs')])
        if product_products:
            product_dict = {}
            for product in product_product_obj.browse(cr, uid, product_products):
                product_dict[product.name] = product.lst_price
            #product_dict = collections.OrderedDict(sorted(product_dict.items()))
            #for product_name in product_dict.keys():
            for key, value in sorted(product_dict.iteritems(), key=lambda (k,v): (v,k)):
                res = {
                    'name' : key,
                    'price' : value,
                    }                
                result.append(res)
        return result
    """