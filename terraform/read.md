# Terraform Part 2: Infrastructure Provisioning on GCP

This section outlines the Terraform configuration used to provision the infrastructure for the Citi Bike data pipeline on Google Cloud Platform (GCP).

## 📁 Directory Structure
citi-bike-terraform/
├── auth_key/
│ └── keys.json # Service account credentials
├── main.tf # Primary resource definitions
├── provider.tf # Provider configuration
├── variables.tf # Input variables
└── README.md # This file


## 📄 main.tf – Compute Engine Instance Configuration

This file defines the virtual machine (VM) used for data processing.

- **VM Naming**: Includes environment prefix (e.g., dev, prod)
- **Machine Type**: e2-standard-4
- **Boot Disk**: Ubuntu 22.04 LTS, 30GB
- **Service Account**: `citi-bike-capstone-project@stellar-mercury-455917-d9.iam.gserviceaccount.com`

**Startup Script Installs**:
- Python
- Docker
- Git
- Google Cloud BigQuery client library

**Features**:
- Enables OS Login
- Starts Docker automatically

## 📄 provider.tf – GCP Provider Configuration

This file specifies the Terraform provider and authentication method.

- **Provider**: `hashicorp/google` (version 6.27.0)
- **Authentication**: JSON key file (`auth_key/keys.json`)

**Configuration Includes**:
- GCP Project ID
- Region
- Zone

## 📄 variables.tf – Reusable Variables

Defines flexible variables to make the infrastructure portable and configurable:

- `project_id`: GCP project identifier
- `credentials_file`: Path to your JSON service account key
- `region`: GCP region for resource deployment
- `zone`: GCP zone for VM placement
- `environment`: Deployment environment (dev, staging, prod)
- `service_account_email`: IAM service account email
- `vm_config`: Optional object to override VM specs

## ⚙️ Deployment Steps

1. **Initialize Terraform**
   ```bash
   terraform init
2. **Review Execution Plan
   '''bash
    terraform plan
3. **Apply Configuration 
   '''bash
    terraform apply
4. **Destroy Resources (when needed)
    '''bash
    terraform destroy
## 🔐 Required IAM Roles
  - Make sure the service account has the following permissions:
  
  - roles/compute.instanceAdmin.v1
  
  - roles/iam.serviceAccountUser
  
  - roles/serviceusage.serviceUsageConsumer

## 🔒 Security Best Practices
    - ❌ Never commit sensitive files like keys.json to Git
    
    - 🔐 Restrict SSH access to trusted IP addresses only
    
    - 🔁 Rotate service account keys regularly

    
