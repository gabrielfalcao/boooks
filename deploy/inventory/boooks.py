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
        "TIERS": {
          "web": {
            "subnet": {
              "instance": {
                "name": "web-subnet", 
                "tags": {
                  "Tier": "web", 
                  "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
            "name": "web", 
            "availability_zone": "us-east-1b", 
            "firewall": {
              "inbound": [
                {
                  "source": "0.0.0.0/0", 
                  "protocol": "TCP", 
                  "port": 22, 
                  "label": "SSH from anywhere"
                }, 
                {
                  "source": "0.0.0.0/0", 
                  "protocol": "TCP", 
                  "port": 443, 
                  "label": "HTTPS in"
                }, 
                {
                  "source": "0.0.0.0/0", 
                  "protocol": "TCP", 
                  "port": 80, 
                  "label": "HTTP in"
                }
              ], 
              "outbound": [
                {
                  "destination": "0.0.0.0/0", 
                  "protocol": "TCP", 
                  "port": 80, 
                  "label": "HTTP out"
                }, 
                {
                  "destination": "0.0.0.0/0", 
                  "protocol": "TCP", 
                  "port": 443, 
                  "label": "HTTPS out"
                }, 
                {
                  "destination": "0.0.0.0/0", 
                  "protocol": "TCP", 
                  "port": 22, 
                  "label": "SSH out"
                }
              ]
            }, 
            "region": "us-east-1", 
            "security_group_name": "web-sg", 
            "subnet_name": "web-subnet", 
            "route_table": {
              "subnet": {
                "instance": {
                  "name": "web-subnet", 
                  "tags": {
                    "Tier": "web", 
                    "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
              "subnets": [
                {
                  "instance": {
                    "name": "web-subnet", 
                    "tags": {
                      "Tier": "web", 
                      "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
                }
              ], 
              "name": "web-route-table", 
              "association": "rtbassoc-2dddbc48", 
              "instance": {
                "routes": [
                  {
                    "gateway_id": "local", 
                    "instance_id": null, 
                    "state": "active", 
                    "destination": "10.0.0.0/16"
                  }, 
                  {
                    "gateway_id": "igw-6d46e208", 
                    "instance_id": null, 
                    "state": "active", 
                    "destination": "0.0.0.0/0"
                  }
                ], 
                "class": "boto.vpc.routetable.RouteTable", 
                "tags": {
                  "LastFlorestaRun": "2014-11-11T05:07:38.506550", 
                  "Tier": "web", 
                  "Role": "RouteTable", 
                  "Name": "web-route-table", 
                  "VPC": "boooks"
                }, 
                "name": "web-route-table", 
                "id": "rtb-c7ad3aa2"
              }
            }, 
            "security_group": {
              "instance": {
                "description": "Tier web security group", 
                "class": "boto.ec2.securitygroup.SecurityGroup", 
                "tags": {
                  "LastFlorestaRun": "2014-11-11T05:07:39.278219", 
                  "Tier": "web", 
                  "Role": "SecurityGroup", 
                  "Name": "web", 
                  "VPC": "boooks"
                }, 
                "name": "web", 
                "id": "sg-bcedfed9"
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
            "route_table_name": "web-route-table", 
            "cidr": "10.0.0.0/24", 
            "public": true
          }
        }, 
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
                "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
              "LastFlorestaRun": "2014-11-11T05:07:46.587676", 
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
            "sudo": true, 
            "hosts": [
              "boooks-web"
            ], 
            "user": "ubuntu", 
            "roles": [
              "base/common", 
              "base/ntp", 
              "base/postgres", 
              "base/redis", 
              "base/nodejs", 
              "base/nginx", 
              "base/supervisor", 
              "apps/boooks"
            ], 
            "remote_user": "ubuntu"
          }, 
          "user": "ubuntu", 
          "keypair": "weedlabs-master", 
          "tier": "web", 
          "security_group": {
            "instance": {
              "id": "sg-bcedfed9", 
              "tags": {
                "LastFlorestaRun": "2014-11-11T05:07:39.278219", 
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
        "PUBLIC_IPS": {
          "54.173.167.190": {
            "subnet": {
              "instance": {
                "name": "web-subnet", 
                "tags": {
                  "Tier": "web", 
                  "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
            "instance_profile": null, 
            "name": "boooks-web", 
            "availability_zone": "us-east-1b", 
            "hosted_zone_id": "ZEPX1Q8LGM34G", 
            "instance": {
              "name": "boooks-web", 
              "tags": {
                "LastFlorestaRun": "2014-11-11T05:07:46.587676", 
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
            "keypair": "weedlabs-master", 
            "security_group": {
              "instance": {
                "description": "Tier web security group", 
                "class": "boto.ec2.securitygroup.SecurityGroup", 
                "tags": {
                  "LastFlorestaRun": "2014-11-11T05:07:39.278219", 
                  "Tier": "web", 
                  "Role": "SecurityGroup", 
                  "Name": "web", 
                  "VPC": "boooks"
                }, 
                "name": "web", 
                "id": "sg-bcedfed9"
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
            "gateway": {
              "attachments": [
                {
                  "vpc_id": "vpc-85911ae0", 
                  "state": "available"
                }
              ], 
              "class": "boto.vpc.internetgateway.InternetGateway", 
              "tags": {
                "Name": "boooks-gateway"
              }, 
              "name": "boooks-gateway", 
              "id": "igw-6d46e208"
            }
          }
        }, 
        "DOMAINS": {
          "boooks.me": {
            "subnet": {
              "instance": {
                "name": "web-subnet", 
                "tags": {
                  "Tier": "web", 
                  "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
            "instance_profile": null, 
            "name": "boooks-web", 
            "availability_zone": "us-east-1b", 
            "hosted_zone_id": "ZEPX1Q8LGM34G", 
            "instance": {
              "name": "boooks-web", 
              "tags": {
                "LastFlorestaRun": "2014-11-11T05:07:46.587676", 
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
            "keypair": "weedlabs-master", 
            "security_group": {
              "instance": {
                "description": "Tier web security group", 
                "class": "boto.ec2.securitygroup.SecurityGroup", 
                "tags": {
                  "LastFlorestaRun": "2014-11-11T05:07:39.278219", 
                  "Tier": "web", 
                  "Role": "SecurityGroup", 
                  "Name": "web", 
                  "VPC": "boooks"
                }, 
                "name": "web", 
                "id": "sg-bcedfed9"
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
            "gateway": {
              "attachments": [
                {
                  "vpc_id": "vpc-85911ae0", 
                  "state": "available"
                }
              ], 
              "class": "boto.vpc.internetgateway.InternetGateway", 
              "tags": {
                "Name": "boooks-gateway"
              }, 
              "name": "boooks-gateway", 
              "id": "igw-6d46e208"
            }
          }
        }, 
        "LOAD_BALANCERS": {}, 
        "MACHINES_BY_NAME": {
          "boooks-web": {
            "profile": {}, 
            "subnet": {
              "instance": {
                "name": "web-subnet", 
                "tags": {
                  "Tier": "web", 
                  "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
              "tags": {
                "Name": "boooks-gateway"
              }, 
              "name": "boooks-gateway", 
              "id": "igw-6d46e208"
            }, 
            "hosted_zone_id": "ZEPX1Q8LGM34G", 
            "instance": {
              "name": "boooks-web", 
              "tags": {
                "LastFlorestaRun": "2014-11-11T05:07:46.587676", 
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
              "sudo": true, 
              "hosts": [
                "boooks-web"
              ], 
              "user": "ubuntu", 
              "roles": [
                "base/common", 
                "base/ntp", 
                "base/postgres", 
                "base/redis", 
                "base/nodejs", 
                "base/nginx", 
                "base/supervisor", 
                "apps/boooks"
              ], 
              "remote_user": "ubuntu"
            }, 
            "user": "ubuntu", 
            "keypair": "weedlabs-master", 
            "tier": "web", 
            "security_group": {
              "instance": {
                "description": "Tier web security group", 
                "class": "boto.ec2.securitygroup.SecurityGroup", 
                "tags": {
                  "LastFlorestaRun": "2014-11-11T05:07:39.278219", 
                  "Tier": "web", 
                  "Role": "SecurityGroup", 
                  "Name": "web", 
                  "VPC": "boooks"
                }, 
                "name": "web", 
                "id": "sg-bcedfed9"
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
              "LastFlorestaRun": "2014-11-11T05:07:37.856104", 
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
          "tags": {
            "Name": "boooks-gateway"
          }, 
          "name": "boooks-gateway", 
          "id": "igw-6d46e208"
        }, 
        "hosted_zone_id": "ZEPX1Q8LGM34G", 
        "instance": {
          "name": "boooks-web", 
          "tags": {
            "LastFlorestaRun": "2014-11-11T05:07:46.587676", 
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
          "sudo": true, 
          "hosts": [
            "boooks-web"
          ], 
          "user": "ubuntu", 
          "roles": [
            "base/common", 
            "base/ntp", 
            "base/postgres", 
            "base/redis", 
            "base/nodejs", 
            "base/nginx", 
            "base/supervisor", 
            "apps/boooks"
          ], 
          "remote_user": "ubuntu"
        }, 
        "user": "ubuntu", 
        "keypair": "weedlabs-master", 
        "tier": "web", 
        "security_group": {
          "instance": {
            "description": "Tier web security group", 
            "class": "boto.ec2.securitygroup.SecurityGroup", 
            "tags": {
              "LastFlorestaRun": "2014-11-11T05:07:39.278219", 
              "Tier": "web", 
              "Role": "SecurityGroup", 
              "Name": "web", 
              "VPC": "boooks"
            }, 
            "name": "web", 
            "id": "sg-bcedfed9"
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