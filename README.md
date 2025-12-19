# Encrypted Insurance Claim Validator
Zero-Knowledge Fraud Detection using Encrypted Medical & Financial Embeddings

<img width="1024" height="1024" alt="Gemini_Generated_Image_bun3iybun3iybun3" src="https://github.com/user-attachments/assets/e58986a1-e5c2-416c-b7e9-2c068da5d5de" />

## Overview

Healthcare insurance fraud detection requires validating insurance claims against medical records.
However, privacy regulations (HIPAA, data protection laws) strictly prohibit sharing patient health information (PHI) between hospitals and insurers.

As a result:

- Fraud detection is slow and manual
- Insurers approve incorrect or inflated claims
- Hospitals cannot safely share medical data
- Fraud losses run into billions of dollars annually

This project solves that problem using encrypted AI.

## What This Project Does

Encrypted Insurance Claim Validator is a privacy-preserving, zero-knowledge fraud detection engine that validates insurance claims without ever accessing patient data or plaintext embeddings.

It enables:

- Secure medical–financial validation
- Automated fraud detection
- Regulatory compliance by design

All similarity search and reasoning happen on encrypted vectors, powered by a CyborgDB-style encrypted vector search abstraction.

## Core Innovation
### Traditional Approach (Broken)

- Hospitals share medical summaries
- Insurers store embeddings in plaintext
- Embeddings are mathematically invertible
- A database breach can reconstruct sensitive patient data

### Our Approach (Secure by Design)

- Hospitals generate encrypted medical embeddings
- Insurers generate encrypted claim embeddings
- Similarity is computed directly on encrypted vectors
- No plaintext, no raw embeddings, no PHI exposure

Even in the event of a full database breach, patient data cannot be reconstructed.

This makes the system impervious to vector inversion attacks.

## Why CyborgDB Matters

Traditional vector databases focus on performance — not privacy.

CyborgDB introduces encryption-in-use, enabling:

- Encrypted vector storage
- Encrypted similarity search
- Zero-knowledge AI workflows

This project demonstrates a real-world, deployable use case for CyborgDB in Health + FinTech, one of the most regulated domains.

## System Architecture
### Components
#### Component	    →        Responsibility
Hospital Agent	    →    Generates encrypted medical embeddings

Insurer Agent	    →      Generates encrypted claim embeddings

Validation Engine	   →   Encrypted similarity + fraud scoring

CyborgDB (abstracted)	→  Encrypted vector search

UI (Tailwind)	    →      Claim submission & explainable results

## High-Level Flow

1. Hospital processes medical records → encrypted embeddings

2. Insurer processes claim details → encrypted embeddings

3. Validator performs encrypted similarity search

4. Fraud risk score is computed

5. Decision returned with full explainability

At no point is patient data decrypted or shared.

## Fraud Detection Logic

The fraud score is computed using multiple independent signals:

### Signals Used
#### Signal → Description
Encrypted medical similarity → Diagnosis ↔ procedure consistency

Cost anomaly detection → Claimed vs expected amount

Policy rules	Insurance → rule enforcement

### Fraud Risk Score (0–1)
#### Score Range	→ Decision
0.0 – 0.3	→ ✅ Auto-Approve

0.3 – 0.7	→  Manual Review

0.7 – 1.0 →	❌ Auto-Reject

This mirrors real insurance decision engines.

## Professional Demo UI

The Tailwind UI provides:

- Claim submission form
- Visual fraud risk score
- Decision explanation
- Policy rule applied
- Privacy guarantee statement

## Example Scenarios
### Auto-Approved

- Cost deviation within policy limits
- Encrypted medical similarity consistent

### Manual Review

- Moderate cost inflation
- Requires human verification

### Auto-Rejected

- Extreme cost inflation
- Policy violation detected

“The UI explains every decision — showing cost deviation, policy rule applied, and encrypted AI reasoning — without exposing any patient data.”

## Security & Zero-Trust Model
### Encryption Guarantees

- No plaintext medical data
- No raw embeddings stored
- No decryption at validator
- Similarity computed on encrypted vectors only

### Role-Based Access Control (RBAC)
#### Role → Permissions
Hospital → Submit encrypted medical embeddings

Insurer → Submit claims for validation

Validator → Perform encrypted validation

Admin → View audit logs

JWT-based authentication enforces strict trust boundaries.

## Auditability & Compliance

- Every validation is recorded in an audit log
- Decisions are explainable and reproducible
- No PHI exposure — compliant by architecture

## Compliance Alignment

- HIPAA (no PHI sharing)
- Healthcare data minimization
- Financial audit requirements
- Zero-trust security principles

## Tech Stack

- Backend: FastAPI, Python
- AI: Deterministic embeddings (upgrade-ready to BioClinicalBERT / FinBERT)
- Security: Encrypted vector abstraction (CyborgDB-style), JWT, RBAC
- Frontend: Tailwind CSS (CDN)
- Infra: Docker, Render
- Architecture: Microservices, zero-knowledge design

## Live Demo
### UI
https://encrypted-insurance-claim-validator-ui.onrender.com

### API
https://encrypted-insurance-claim-validator.onrender.com

## Repository Structure
encrypted-insurance-claim-validator/

├── architecture/

│   ├── architecture.png

│   └── threat-model.md

├── docs/

│   ├── problem.md

│   ├── innovation.md

│   ├── compliance.md

│   └── demo-flow.md

├── hospital-agent/

├── insurer-agent/

├── validation-engine/

├── ui/

├── docker-compose.yml

└── README.md

## This Project Have

- Real-world problem (billion-dollar fraud)
- Strong CyborgDB relevance
- True zero-knowledge AI
- Encrypted vector search (not just claims)
- Explainable & auditable decisions
- Professional UI & deployment
- Production-ready architecture

This is not a demo —
it is a deployable privacy-first AI system.

## Future Roadmap

- Replace deterministic embeddings with:
- BioClinicalBERT (medical)
- FinBERT (financial)
- Real CyborgDB SDK integration
- Multi-hospital federation
- Historical fraud pattern learning
- Regulatory reporting dashboard

## Final Note

This project demonstrates how encrypted AI can unlock cross-industry collaboration between healthcare and finance — without compromising privacy, trust, or compliance.

Encrypted Insurance Claim Validator shows the future of secure, compliant AI systems.
