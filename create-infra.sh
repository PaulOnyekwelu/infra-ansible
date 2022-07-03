#!/bin/bash

# for aws cloudformation create-stack
# aws cloudformation create-stack \
#   --stack-name Ansible-EC2-Instance \
#   --template-body file://infra.yml \
#   --parameters file://infra-parameters.json \
#   --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=us-west-2

# for aws cloudformation deploy
aws cloudformation deploy \
  --stack-name myStack-${CIRCLE_WORKFLOW_ID:0:5} \
  --template-file "./cloudformation/infra.yml" \
  --parameter-overrides file://"./cloudformation/deploy-parameters.json" \
  --region=us-west-2

  