# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Training Management System',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 115,
    'summary': """This module allow you to Training Management System.""",
    'description': """
    
This module allows you to manage subscriptions.

Features:
    - Create & edit subscriptions
    - Modify subscriptions with sales orders
    - Generate invoice automatically at fixed intervals
    - Add the exercises
    - Set Schedule for particular Customer
    - Set nutrition plane
    - BMI Calculation
    - Calory Calculator

Menu:

    - Dashboard
    - Members
    - Service:
        - Training:
            - Body Parts
                - Muscles
            - Plan
                - Exercises
                    - Exercise Overview
            - Workouts:
                - Create Workouts Schedule
                - Workouts Schedules
                - Print Workouts Schedules
            - Equipment
        - Nutrition
            - Ingredients
            - Nutrition Plans        
            - BMI Calculation
            - Daily Calories Calculator
            - Weight Entry Overview
""",
    'author': 'TucusitoGroup',
    'website': 'https://www.tucusitogroup.gp',
    'support': 'tucusitogroup@gmail.com',
    'license': 'LGPL-3',
    'images': ['static/description/logo.png'],
    "development_status": "Beta",
    'depends': [
        'sale_subscription',
        'website_enterprise',
        'calendar',
        'product',
        'base',
    ],
    # always loaded
    'data': [],
    'demo': [],
    'assets': {},
    'qweb': [],
    'installable' : True,
    'application' : False,
    'auto_install' : False,

}
