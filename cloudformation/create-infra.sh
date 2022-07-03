#!/bin/bash
aws cloudformation create-stack \
  --stack-name Ansible-EC2-Instance \
  --template-body file://infra.yml \
  --parameters file://infra-parameters.json \
  --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=us-west-2
  