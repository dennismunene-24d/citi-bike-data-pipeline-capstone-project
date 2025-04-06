resource "google_compute_instance" "citi_bike_data_processor" {
  name         = "citi-bike-data-processor-${var.environment}"
  zone         = var.zone
  machine_type = "e2-standard-4"
  project      = var.project_id
  tags         = ["citibike", "data-processing"]

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 30
      type  = "pd-balanced"
    }
    auto_delete = false
  }

  labels = {
    environment = var.environment
    project     = "citibike-analytics"
    department  = "data-engineering"
    terraform   = "true"
    component   = "data-processing"
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral public IP
    }
  }

  service_account {
    email  = "citi-bike-capstone-project@stellar-mercury-455917-d9.iam.gserviceaccount.com"
    scopes = ["cloud-platform"]
  }

  metadata = {
    enable-oslogin = "TRUE"
    startup-script = <<-EOF
      #!/bin/bash
      apt-get update
      apt-get install -y \
        python3-pip \
        docker.io \
        git
      pip3 install google-cloud-bigquery
      systemctl enable docker
    EOF
  }

}