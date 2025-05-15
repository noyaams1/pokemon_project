# Step 1: creating public rsa key and import it to AWS
# Step 2: creating settings to the ec2 server
#Amazon linux ami id on region us-west-2
image_id=ami-04999cd8f2624f834 
instance_type=t2.micro
#Replace with your imported key name
key_pair=my-imported-key 
# Step 3: creating the ec2 pokemon game server and extracting the instance-id
instance_id=$(aws ec2 run-instances \
  --image-id $image_id \
  --instance-type $instance_type \
  --key-name $key_pair \
  --user-data file://user_data.sh \
  --query "Instances[0].InstanceId" \
  --output text)
echo "Instance launched: $instance_id"

security_group_id=$(aws ec2 describe-instances \
  --instance-ids "$instance_id" \
  --query "Reservations[0].Instances[0].SecurityGroups[0].GroupId" \
  --output text)

echo "Security Group ID: $security_group_id"
#Step 4: extracting the security group id to add role: open port 22 for SSH 
aws ec2 authorize-security-group-ingress \
  --group-id "$security_group_id" \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0

