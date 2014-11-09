#!/usr/bin/env python
# -*- coding: utf-8 -*-


print '''{
  "web": {
    "hosts": [
      "54.173.167.190"
    ], 
    "children": [
      "54.173.167.190"
    ], 
    "vars": {
      "floresta": {
        "TIERS": {}, 
        "ELASTIC_IPS": {}, 
        "machine": {
          "profile": {}, 
          "subnet": {
            "instance": {
              "name": "web-subnet", 
              "availability_zone": "us-east-1b", 
              "region": {
                "name": "us-east-1"
              }, 
              "tags": {
                "Tier": "web", 
                "LastFlorestaRun": "2014-11-09T08:11:20.324540", 
                "Role": "Subnet", 
                "Name": "web-subnet", 
                "VPC": "boooks"
              }, 
              "class": "boto.vpc.subnet.Subnet", 
              "cidr_block": "10.0.0.0/24", 
              "id": "subnet-5169c226"
            }, 
            "cidr": "10.0.0.0/24", 
            "name": "web-subnet", 
            "availability_zone": "us-east-1b"
          }, 
          "domain": "boooks.me", 
          "instance_profile": null, 
          "name": "boooks-web", 
          "availability_zone": "us-east-1b", 
          "ami-id": "ami-e84d8480", 
          "public": true, 
          "hosted_zone_id": "ZEPX1Q8LGM34G", 
          "instance": {
            "name": "boooks-web", 
            "tags": {
              "LastFlorestaRun": "2014-11-09T08:15:04.238165", 
              "Tier": "web", 
              "Role": "Machine", 
              "Name": "boooks-web", 
              "VPC": "boooks"
            }, 
            "class": "boto.ec2.instance.Instance", 
            "private_ip_address": "10.0.0.203", 
            "ip_address": "54.173.167.190", 
            "id": "i-b7881e5d"
          }, 
          "ansible_roles_path": "~/projects/personal/boooks/deploy", 
          "ansible": {
            "remote_user": "ubuntu", 
            "name": "boooks-web", 
            "roles": [
              "base/common", 
              "base/ntp", 
              "base/postgres", 
              "base/redis", 
              "base/nginx", 
              "base/supervisor", 
              "apps/boooks"
            ], 
            "sudo": true, 
            "hosts": [
              "54.173.167.190"
            ], 
            "user": "ubuntu"
          }, 
          "user": "ubuntu", 
          "keypair": "weedlabs-master", 
          "tier": "web", 
          "security_group": {
            "instance": {
              "id": "sg-bcedfed9", 
              "tags": {
                "LastFlorestaRun": "2014-11-09T08:11:21.908519", 
                "Tier": "web", 
                "Role": "SecurityGroup", 
                "Name": "web", 
                "VPC": "boooks"
              }, 
              "class": "boto.ec2.securitygroup.SecurityGroup", 
              "name": "web", 
              "description": "Tier web security group"
            }, 
            "outbound_rules": [
              {
                "to_port": "80", 
                "from_port": "80", 
                "destination_cidr": "0.0.0.0/0"
              }, 
              {
                "to_port": "443", 
                "from_port": "443", 
                "destination_cidr": "0.0.0.0/0"
              }, 
              {
                "to_port": "22", 
                "from_port": "22", 
                "destination_cidr": "0.0.0.0/0"
              }
            ], 
            "name": "web-sg", 
            "inbound_rules": [
              {
                "to_port": "22", 
                "source_cidr": "0.0.0.0/0", 
                "from_port": "22"
              }, 
              {
                "to_port": "443", 
                "source_cidr": "0.0.0.0/0", 
                "from_port": "443"
              }, 
              {
                "to_port": "80", 
                "source_cidr": "0.0.0.0/0", 
                "from_port": "80"
              }
            ], 
            "description": "Tier web security group"
          }, 
          "instance-type": "m1.small", 
          "instance_name": "boooks-web [web]", 
          "gateway": {
            "id": "igw-6d46e208", 
            "tags": {
              "Name": "boooks-gateway"
            }, 
            "attachments": [
              {
                "vpc_id": "vpc-85911ae0", 
                "state": "available"
              }
            ], 
            "name": "boooks-gateway", 
            "class": "boto.vpc.internetgateway.InternetGateway"
          }
        }, 
        "PUBLIC_IPS": {}, 
        "DOMAINS": {}, 
        "LOAD_BALANCERS": {}, 
        "MACHINES_BY_NAME": {
          "boooks-web": {
            "profile": {}, 
            "subnet": {
              "instance": {
                "name": "web-subnet", 
                "tags": {
                  "Tier": "web", 
                  "LastFlorestaRun": "2014-11-09T08:11:20.324540", 
                  "Role": "Subnet", 
                  "Name": "web-subnet", 
                  "VPC": "boooks"
                }, 
                "region": {
                  "name": "us-east-1"
                }, 
                "availability_zone": "us-east-1b", 
                "id": "subnet-5169c226", 
                "cidr_block": "10.0.0.0/24", 
                "class": "boto.vpc.subnet.Subnet"
              }, 
              "cidr": "10.0.0.0/24", 
              "name": "web-subnet", 
              "availability_zone": "us-east-1b"
            }, 
            "domain": "boooks.me", 
            "instance_profile": null, 
            "name": "boooks-web", 
            "availability_zone": "us-east-1b", 
            "ami-id": "ami-e84d8480", 
            "gateway": {
              "attachments": [
                {
                  "vpc_id": "vpc-85911ae0", 
                  "state": "available"
                }
              ], 
              "class": "boto.vpc.internetgateway.InternetGateway", 
              "id": "igw-6d46e208", 
              "name": "boooks-gateway", 
              "tags": {
                "Name": "boooks-gateway"
              }
            }, 
            "hosted_zone_id": "ZEPX1Q8LGM34G", 
            "instance": {
              "name": "boooks-web", 
              "tags": {
                "LastFlorestaRun": "2014-11-09T08:15:04.238165", 
                "Tier": "web", 
                "Role": "Machine", 
                "Name": "boooks-web", 
                "VPC": "boooks"
              }, 
              "id": "i-b7881e5d", 
              "private_ip_address": "10.0.0.203", 
              "ip_address": "54.173.167.190", 
              "class": "boto.ec2.instance.Instance"
            }, 
            "ansible_roles_path": "~/projects/personal/boooks/deploy", 
            "ansible": {
              "remote_user": "ubuntu", 
              "name": "boooks-web", 
              "roles": [
                "base/common", 
                "base/ntp", 
                "base/postgres", 
                "base/redis", 
                "base/nginx", 
                "base/supervisor", 
                "apps/boooks"
              ], 
              "sudo": true, 
              "hosts": [
                "54.173.167.190"
              ], 
              "user": "ubuntu"
            }, 
            "user": "ubuntu", 
            "keypair": "weedlabs-master", 
            "tier": "web", 
            "security_group": {
              "instance": {
                "class": "boto.ec2.securitygroup.SecurityGroup", 
                "description": "Tier web security group", 
                "id": "sg-bcedfed9", 
                "name": "web", 
                "tags": {
                  "LastFlorestaRun": "2014-11-09T08:11:21.908519", 
                  "Tier": "web", 
                  "Role": "SecurityGroup", 
                  "Name": "web", 
                  "VPC": "boooks"
                }
              }, 
              "outbound_rules": [
                {
                  "to_port": "80", 
                  "from_port": "80", 
                  "destination_cidr": "0.0.0.0/0"
                }, 
                {
                  "to_port": "443", 
                  "from_port": "443", 
                  "destination_cidr": "0.0.0.0/0"
                }, 
                {
                  "to_port": "22", 
                  "from_port": "22", 
                  "destination_cidr": "0.0.0.0/0"
                }
              ], 
              "name": "web-sg", 
              "inbound_rules": [
                {
                  "to_port": "22", 
                  "source_cidr": "0.0.0.0/0", 
                  "from_port": "22"
                }, 
                {
                  "to_port": "443", 
                  "source_cidr": "0.0.0.0/0", 
                  "from_port": "443"
                }, 
                {
                  "to_port": "80", 
                  "source_cidr": "0.0.0.0/0", 
                  "from_port": "80"
                }
              ], 
              "description": "Tier web security group"
            }, 
            "instance-type": "m1.small", 
            "instance_name": "boooks-web [web]", 
            "public": true
          }
        }
      }
    }
  }, 
  "boooks-web": {
    "hosts": [
      "54.173.167.190"
    ], 
    "vars": {
      "machine": {
        "profile": {}, 
        "subnet": {
          "instance": {
            "name": "web-subnet", 
            "tags": {
              "Tier": "web", 
              "LastFlorestaRun": "2014-11-09T08:11:20.324540", 
              "Role": "Subnet", 
              "Name": "web-subnet", 
              "VPC": "boooks"
            }, 
            "region": {
              "name": "us-east-1"
            }, 
            "availability_zone": "us-east-1b", 
            "id": "subnet-5169c226", 
            "cidr_block": "10.0.0.0/24", 
            "class": "boto.vpc.subnet.Subnet"
          }, 
          "cidr": "10.0.0.0/24", 
          "name": "web-subnet", 
          "availability_zone": "us-east-1b"
        }, 
        "domain": "boooks.me", 
        "instance_profile": null, 
        "name": "boooks-web", 
        "availability_zone": "us-east-1b", 
        "ami-id": "ami-e84d8480", 
        "gateway": {
          "attachments": [
            {
              "vpc_id": "vpc-85911ae0", 
              "state": "available"
            }
          ], 
          "class": "boto.vpc.internetgateway.InternetGateway", 
          "id": "igw-6d46e208", 
          "name": "boooks-gateway", 
          "tags": {
            "Name": "boooks-gateway"
          }
        }, 
        "hosted_zone_id": "ZEPX1Q8LGM34G", 
        "instance": {
          "name": "boooks-web", 
          "tags": {
            "LastFlorestaRun": "2014-11-09T08:15:04.238165", 
            "Tier": "web", 
            "Role": "Machine", 
            "Name": "boooks-web", 
            "VPC": "boooks"
          }, 
          "id": "i-b7881e5d", 
          "private_ip_address": "10.0.0.203", 
          "ip_address": "54.173.167.190", 
          "class": "boto.ec2.instance.Instance"
        }, 
        "ansible_roles_path": "~/projects/personal/boooks/deploy", 
        "ansible": {
          "remote_user": "ubuntu", 
          "name": "boooks-web", 
          "roles": [
            "base/common", 
            "base/ntp", 
            "base/postgres", 
            "base/redis", 
            "base/nginx", 
            "base/supervisor", 
            "apps/boooks"
          ], 
          "sudo": true, 
          "hosts": [
            "54.173.167.190"
          ], 
          "user": "ubuntu"
        }, 
        "user": "ubuntu", 
        "keypair": "weedlabs-master", 
        "tier": "web", 
        "security_group": {
          "instance": {
            "class": "boto.ec2.securitygroup.SecurityGroup", 
            "description": "Tier web security group", 
            "id": "sg-bcedfed9", 
            "name": "web", 
            "tags": {
              "LastFlorestaRun": "2014-11-09T08:11:21.908519", 
              "Tier": "web", 
              "Role": "SecurityGroup", 
              "Name": "web", 
              "VPC": "boooks"
            }
          }, 
          "outbound_rules": [
            {
              "to_port": "80", 
              "from_port": "80", 
              "destination_cidr": "0.0.0.0/0"
            }, 
            {
              "to_port": "443", 
              "from_port": "443", 
              "destination_cidr": "0.0.0.0/0"
            }, 
            {
              "to_port": "22", 
              "from_port": "22", 
              "destination_cidr": "0.0.0.0/0"
            }
          ], 
          "name": "web-sg", 
          "inbound_rules": [
            {
              "to_port": "22", 
              "source_cidr": "0.0.0.0/0", 
              "from_port": "22"
            }, 
            {
              "to_port": "443", 
              "source_cidr": "0.0.0.0/0", 
              "from_port": "443"
            }, 
            {
              "to_port": "80", 
              "source_cidr": "0.0.0.0/0", 
              "from_port": "80"
            }
          ], 
          "description": "Tier web security group"
        }, 
        "instance-type": "m1.small", 
        "instance_name": "boooks-web [web]", 
        "public": true
      }
    }
  }, 
  "boooks": {
    "children": [
      "boooks-web"
    ], 
    "vars": {}
  }, 
  "boooks-load-balancers": {
    "hosts": [], 
    "children": [], 
    "vars": {}
  }
}'''