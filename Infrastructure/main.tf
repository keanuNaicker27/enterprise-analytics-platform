# AWS S3 Bucket for Ingestion
resource "aws_s3_bucket" "data_lake" {
  bucket = "enterprise-data-lake-raw"
}

# GCP BigQuery Dataset for Analytics
resource "google_bigquery_dataset" "analytics_layer" {
  dataset_id = "gold_layer"
  location   = "US"
}

# Azure Resource Group
resource "azurerm_resource_group" "data_factory_rg" {
  name     = "rg-enterprise-analytics"
  location = "East US"
}
