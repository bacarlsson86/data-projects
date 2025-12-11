terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.13.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = "us-central1"
}

resource "google_storage_bucket" "auto-expire" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location = var.location
}