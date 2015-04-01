{
    'name': "AbAKUS signable contract",
    'version': '1.0',
    'depends': ['sale', 'report', 'contract_timesheet_activities_on_site_management', 'account_analytic_account_improvements', 'sla'],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Contract',
    'description': 
    """
    This module adds a new report for contracts that could be printed and sent to the customer to be negociated and signed.    
    
    This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.
    """,
    'data': [
        'report/contract_sale_signable.xml',
        'view/account_analytic_account_view.xml'
            ],
}

