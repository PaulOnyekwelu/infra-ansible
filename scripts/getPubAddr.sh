#!/bin/bash

aws ec2 describe-instances \
--query 'Reservations[].Instances[].PublicIpAddress' \
--filters "Name=tag:Project,Values=Ansible" \
--output text >> inventory