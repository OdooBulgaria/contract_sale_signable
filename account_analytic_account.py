from openerp import models, fields, api
import collections

class account_analytic_account_signable(models.Model):
    _inherit = ['account.analytic.account']
    
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
