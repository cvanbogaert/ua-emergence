import os, json, time, uuid
RUNS_DIR = os.environ.get("UA_RUNS_DIR", "./runs")
os.makedirs(RUNS_DIR, exist_ok=True)

def run(intent="Plan-only demo", constraints=None):
    rid = str(uuid.uuid4())[:8]
    rdir = os.path.join(RUNS_DIR, rid)
    os.makedirs(rdir, exist_ok=True)
    bundle = {
        "intent": intent,
        "constraints": constraints or {},
        "plan": [{"id":"n1","type":"ToolNode","tool":"report_pack","inputs":{}}],
        "dag": {"nodes":["n1"], "edges":[]},
        "policy_checks": [{"ok": True, "why":"Tier A, local-only"}],
        "decisions": [],
        "costs": {"estimated_usd": 0.00},
        "artifacts": [],
        "created_at": time.time()
    }
    with open(os.path.join(rdir, "plan.json"), "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)
    print(json.dumps({"ok": True, "run_id": rid, "dir": rdir}))

if __name__ == "__main__":
    run()
