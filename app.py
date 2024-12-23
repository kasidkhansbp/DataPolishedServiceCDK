#!/usr/bin/env python3
import os

import aws_cdk as cdk

from data_polished_service_cdk.MyStages import AppStages


app = cdk.App()

# Create the development stage

# Create the production stage
AppStages(app, 'Prod',
           env=cdk.Environment(account='', region=''),
           )

app.synth()

