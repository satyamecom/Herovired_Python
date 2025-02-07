instances = [
{"name": "web-server", "type": "t2.micro", "ami": "ami-12345678"},
{"name": "db-server", "type": "t2.large", "ami": "ami-87654321"}
]

emlist=[]
for i in instances:
    name=i.get("name")
    i_type=i.get("type")
    ami_id=i.get("ami")
    command=(f"aws ec2 run-instances --instance-type {i_type} --image-id {ami_id}" 
    f"--tag-specifications 'ResourceType=instance,Tags=[{{Key=Name,Value={name}}}]'")
    print(command)