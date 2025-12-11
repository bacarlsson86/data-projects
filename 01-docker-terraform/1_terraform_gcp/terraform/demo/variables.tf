variable "project"{
    description = "Project"
    default = "project-f908862f-6f34-4b61-a39"
}

variable "region" {
    description = "Project region"
    default = "us-central1"
}

variable "location"{
    description = "Project location"
    default = "US"
}

variable "bq_dataset_name"{
    description = "My bigquery dataset name"
    default = "demo_dataset"
}

variable "gcs_bucket_name"{
    description = "My bigquery dataset name"
    default = "project-f908862f-6f34-4b61-a39-terra-bucket"
}

variable "gcs_storage_class"{
    description = "Bucket Storage Class"
    default = "STANDARD"
}