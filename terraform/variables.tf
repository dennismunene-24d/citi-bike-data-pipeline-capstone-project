variable "project_id" {
  description = "The GCP Project ID for Citi Bike analytics"
  type        = string
  default     = "stellar-mercury-455917-d9" # Your actual project ID
}

variable "credentials_file" {
  description = "Path to service account JSON key"
  type        = string
  default     = "auth_key/keys.json" # Relative path to your key
}

variable "region" {
  description = "GCP region for resources"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "GCP zone for compute resources"
  type        = string
  default     = "us-central1-a"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "service_account_email" {
  description = "Pre-configured service account email"
  type        = string
  default     = "citi-bike-capstone-project@stellar-mercury-455917-d9.iam.gserviceaccount.com"
}

variable "vm_config" {
  description = "Compute Engine VM configuration"
  type = object({
    machine_type = string
    disk_size    = number
    image        = string
  })
  default = {
    machine_type = "e2-standard-4"
    disk_size    = 30
    image        = "ubuntu-os-cloud/ubuntu-2204-lts"
  }
}
