terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.13.0"
    }
  }
}

provider "google" {
  project     = "project-f908862f-6f34-4b61-a39"
  region      = "us-central1"
}

resource "google_storage_bucket" "auto-expire" {
  name          = "project-f908862f-6f34-4b61-a39-terra-bucket"
  location      = "US"
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