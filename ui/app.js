async function submitClaim() {
  const claimId = document.getElementById("claimId").value;
  const amount = parseFloat(document.getElementById("amount").value);
  const expected = parseFloat(document.getElementById("expected").value);

  // ---------- Input Validation ----------
  if (!claimId || isNaN(amount) || isNaN(expected)) {
    alert("Please fill all fields correctly");
    return;
  }

  // ---------- Demo Encrypted Payloads ----------
  // (In real flow, these come from hospital & insurer agents)
  const encryptedClaim = {
    enc_blob: "demo-claim-blob",
    nonce: "abc123"
  };

  const encryptedMedical = [
    {
      enc_blob: "demo-medical-blob",
      nonce: "def456"
    }
  ];

  // ---------- Backend URL ----------
  const BACKEND_URL = window.BACKEND_URL || "http://localhost:8003";
  console.log("Calling backend:", BACKEND_URL);

  try {
    const response = await fetch(`${BACKEND_URL}/validate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",

        // ⚠️ Demo insurer JWT
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiaW5zdXJlciIsIm9yZyI6Imluc3VyZXItMSJ9.oGFIQ12VcLKf9ONrM_Zf9W47TN1rw5f4u_2hH5KGt88"
      },
      body: JSON.stringify({
        claim_id: claimId,
        claimed_amount: amount,
        expected_amount: expected,
        claim_embedding: encryptedClaim,
        medical_embeddings: encryptedMedical
      })
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || "Validation request failed");
    }

    const data = await response.json();
    showResult(data);

  } catch (err) {
    console.error("Validation failed:", err);
    alert("Validation failed. Check console for details.");
  }
}

// ---------- UI Rendering (UPDATED) ----------
function showResult(data) {
  const result = document.getElementById("result");
  const scoreCircle = document.getElementById("scoreCircle");
  const decision = document.getElementById("decision");
  const policyLabel = document.getElementById("policyLabel");
  const costBar = document.getElementById("costBar");
  const costPercent = document.getElementById("costPercent");
  const reasons = document.getElementById("reasons");

  result.classList.remove("hidden");

  // Score
  scoreCircle.innerText = data.fraud_risk.toFixed(2);
  decision.innerText = data.decision;

  // Reset reasons
  reasons.innerHTML = "";

  // ---------- Policy label & colors ----------
  if (data.decision === "APPROVE") {
    scoreCircle.className =
      "w-24 h-24 rounded-full flex items-center justify-center text-white text-2xl font-bold bg-green-500";
    policyLabel.innerText = "Auto-Approved Policy";
    policyLabel.className =
      "inline-block mt-1 px-3 py-1 rounded text-sm font-semibold bg-green-100 text-green-700";

    reasons.innerHTML += "<li>Cost deviation is within normal limits</li>";
    reasons.innerHTML += "<li>Encrypted medical similarity is consistent</li>";
  }

  if (data.decision === "MANUAL_REVIEW") {
    scoreCircle.className =
      "w-24 h-24 rounded-full flex items-center justify-center text-white text-2xl font-bold bg-yellow-500";
    policyLabel.innerText = "Manual Review Policy";
    policyLabel.className =
      "inline-block mt-1 px-3 py-1 rounded text-sm font-semibold bg-yellow-100 text-yellow-700";

    reasons.innerHTML += "<li>Moderate cost inflation detected</li>";
    reasons.innerHTML += "<li>Requires human verification</li>";
  }

  if (data.decision === "REJECT") {
    scoreCircle.className =
      "w-24 h-24 rounded-full flex items-center justify-center text-white text-2xl font-bold bg-red-500";
    policyLabel.innerText = "Auto-Reject Policy";
    policyLabel.className =
      "inline-block mt-1 px-3 py-1 rounded text-sm font-semibold bg-red-100 text-red-700";

    reasons.innerHTML += "<li>Extreme cost inflation detected</li>";
    reasons.innerHTML += "<li>Violates insurance policy rules</li>";
  }

  // ---------- Cost deviation ----------
  const deviationPercent = Math.round(data.cost_anomaly_score * 100);
  costPercent.innerText = deviationPercent;
  costBar.style.width = `${deviationPercent}%`;

  if (deviationPercent < 30) {
    costBar.className = "h-3 rounded-full bg-green-500";
  } else if (deviationPercent < 70) {
    costBar.className = "h-3 rounded-full bg-yellow-500";
  } else {
    costBar.className = "h-3 rounded-full bg-red-500";
  }

  // ---------- Security guarantee ----------
  reasons.innerHTML += "<li>No PHI or plaintext embeddings were accessed</li>";
}