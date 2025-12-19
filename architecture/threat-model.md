# Threat Model & Security Analysis

## Threats Addressed

### 1. PHI Leakage
- Raw medical records are never transmitted
- Embeddings are encrypted at source
- Validator cannot decrypt vectors

### 2. Embedding Inversion Attacks
- Plain embeddings are never stored
- Encrypted vectors are impervious to inversion
- CyborgDB-style encryption-in-use is applied

### 3. Unauthorized Access
- JWT-based RBAC enforced
- Hospitals, insurers, and admins are role-isolated

### 4. Insider Threats
- No plaintext access at validator
- Audit logs capture all validation actions

## Trust Assumptions
- Encryption keys never leave tenant boundary
- Validator operates under zero-trust principles

## Compliance Alignment
- HIPAA: No PHI exposure
- Financial compliance: Auditable, explainable decisions
