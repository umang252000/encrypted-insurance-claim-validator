# Encrypted Insurance Claim Validator

A privacy-preserving Health–FinTech fraud detection engine that validates insurance claims using encrypted medical and financial embeddings.

## Problem
Insurance providers must validate claims against medical records, but hospitals cannot share patient health information due to privacy regulations. This creates slow, manual processes and enables large-scale fraud.

## Solution
This project introduces an encrypted claim validation system powered by CyborgDB. Hospitals and insurers store only encrypted embeddings, enabling semantic validation without exposing sensitive data.

## Key Features
- Encrypted medical & financial embeddings
- Zero-knowledge similarity search
- Fraud risk scoring without PHI exposure
- Multi-hospital & multi-insurer architecture
- Auditability and compliance-ready design

## Architecture
- Hospital Agent (medical embeddings)
- Insurer Agent (claim embeddings)
- Validation Engine (encrypted similarity + anomaly detection)
- CyborgDB encrypted vector database

## Status
🚧 Prototype under active development (Hackathon submission)