#!/usr/bin/env python3
import argparse, json, os
ap=argparse.ArgumentParser()
ap.add_argument("--changed",required=True); ap.add_argument("--plan-json",default=""); ap.add_argument("--plan-log",default=""); ap.add_argument("--out",required=True)
a=ap.parse_args()
def read(p):
  try:
    with open(p,"r",encoding="utf-8",errors="replace") as f: return f.read()
  except FileNotFoundError:
    return ""
changed=read(a.changed); plan_raw=read(a.plan_json); plan={}
if plan_raw.strip():
  try: plan=json.loads(plan_raw)
  except: plan={"status":"unknown","summary":"Invalid plan.json"}
status=plan.get("status","unknown"); summary=(plan.get("summary","") or "").strip(); issues=plan.get("issues",[])
body=["### PR Draft (plan-only) report","",f"**Plan status:** `{status}`"]
if summary: body.append(f"**Summary:** {summary}")
if issues: body+=["","**Issues detected:**"]+[f"- {i}" for i in issues]
body+=["","<details><summary>Changed files</summary>","","```text",(changed.strip() or "(none)"),"```","</details>",""]
os.makedirs(os.path.dirname(a.out),exist_ok=True)
with open(a.out,"w",encoding="utf-8") as f:
  f.write("<!-- pr-draft:marker -->\n"+"\n".join(body)+"\n")
