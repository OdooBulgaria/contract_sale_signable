{
    'name': "AbAKUS signable contract",
    'version': '9.0.1.0',
    'depends': [
        'report',
        'account_analytic_account_improvements',
        'sla',
    ],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Contract',
    'description': 
    """
    AbAKUS Contract Signable Report

    This module adds a new report for contracts that could be printed and sent to the customer to be negociated and signed.

    Info:
    - Products that will be listed in rates: products that have a default code like 'SUPPORT_BL'
    - Products that will be listed in travel: products that have a default code like 'TRAV'
    
    This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.
    """,
    'data': [
        'report/contract_sale_signable.xml',
        'report/contract_conditions.xml',
        'view/account_analytic_account_view.xml'
            ],
}

