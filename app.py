#!/usr/bin/env python3
import os

import aws_cdk as cdk

from data_polished_service_cdk.MyStages import AppStages

app = cdk.App()

# Retrieve context values for account and region
account_id = app.node.try_get_context("aws:account_id")
region = app.node.try_get_context("aws:region")

# Validate the context values
if not account_id:
    raise ValueError("Account ID is not provided in context")
if not region:
    raise ValueError("Region is not provided in context")

# Log the retrieved values for debugging
print(f"Using Account ID: {account_id}, Region: {region}")

# Create the development stage

# Create the production stage
AppStages(app, 'Prod',
           env=cdk.Environment(account=account_id, region=region),
           )

app.synth()

