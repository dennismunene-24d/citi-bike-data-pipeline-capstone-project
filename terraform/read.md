# 🚲 Terraform: GCP Infrastructure Provisioning for Citi Bike Data Pipeline

This Terraform project provisions compute infrastructure for a data analytics pipeline using the Citi Bike dataset on **Google Cloud Platform (GCP)**. It deploys a VM configured for Docker-based data processing.

---

## 📁 Project Structure


---

## ⚙️ Core Configuration Files

### 📄 `provider.tf` – GCP Provider Setup

Configures the Google Cloud provider:

- Uses `hashicorp/google` provider version `~> 6.27.0`
- Authenticates using a service account JSON key
- Sets default project and region/zone

---

### 📄 `main.tf` – Compute Resources

Defines the VM instance used for data processing:

- **Instance Name**: `{environment}-citi-bike-processor` (e.g., `dev-citi-bike-processor`)
- **Machine Type**: `e2-standard-4` (4 vCPUs, 16 GB RAM)
- **OS**: Ubuntu 22.04 LTS
- **Disk**: 30 GB boot disk
- **Service Account**:  
  `citi-bike-capstone-project@stellar-mercury-455917-d9.iam.gserviceaccount.com`
- **Features**:
  - OS Login enabled
  - Docker auto-start via startup script
  - Network tags for firewall rules

---

### 📄 `variables.tf` – Customizable Parameters

```hcl
variable "project_id" {
  description = "GCP Project ID"
  default     = "stellar-mercury-455917-d9"
}

variable "environment" {
  description = "Deployment environment (dev/staging/prod)"
  default     = "dev"
}

variable "vm_config" {
  description = "Customizable VM specifications"
  type = object({
    machine_type = string
    disk_size_gb = number
    image        = string
  })
  default = {
    machine_type = "e2-standard-4"
    disk_size_gb = 30
    image        = "ubuntu-os-cloud/ubuntu-2204-lts"
  }
}

� Deployment Workflow
1. Prerequisites
Terraform v1.0+ installed

GCP service account with required roles

Valid credentials JSON in auth_key/keys.json

2. Initialize Terraform
bash
Copy
terraform init
3. Review Execution Plan
bash
Copy
terraform plan
4. Apply Configuration
bash
Copy
terraform apply
5. Destroy Resources (when needed)
bash
Copy
terraform destroy
🔐 IAM Requirements
The service account (citi-bike-capstone-project@...) requires these roles:

Role	Purpose
roles/compute.instanceAdmin.v1	VM creation/management
roles/iam.serviceAccountUser	Service account permissions
roles/serviceusage.serviceUsageConsumer	API enablement
roles/storage.admin	Cloud Storage access
roles/bigquery.admin	BigQuery dataset management
💡 Best Practices
Version Control: Never commit credential files (keys.json)

Environment Separation: Use different variable files for dev/staging/prod

State Management: Configure remote state storage (GCS recommended)

Variable Defaults: Set sensible defaults but allow overrides

Tagging: Include environment tags on all resources

🛠️ Troubleshooting
Authentication Errors: Verify service account has correct permissions

Quota Issues: Check your GCP project quotas

Provider Errors: Run terraform providers to verify plugin versions



    
