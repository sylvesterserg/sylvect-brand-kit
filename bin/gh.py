"""GitHub helper for the brand-kit deploy. Uses the stored custom.github
connector via the surrogate helpers; raw tokens are never handled here."""
import json
import sys
import base64
import urllib.parse
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import (
    add_surrogate_to_request,
    read_json_response,
    DynamicCredentialError,
)

BASE = "https://api.github.com"
CREDENTIAL = "custom.github"
ALLOWED_HOSTS = ["api.github.com"]
OWNER = "sylvesterserg"


def api(method, path, body=None, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("User-Agent", "spaa-brand-kit-deploy")
    req.add_header("Accept", "application/vnd.github+json")
    if data:
        req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, CREDENTIAL, allowed_hosts=ALLOWED_HOSTS)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            if resp.status == 204:
                return {}
            return read_json_response(resp)
    except urllib.error.HTTPError as e:
        try:
            detail = e.read().decode()[:600]
        except Exception:
            detail = ""
        raise SystemExit(f"GitHub API error {method} {path} -> HTTP {e.code}: {detail}")


def cmd_repos(_args):
    out = api("GET", f"/users/{OWNER}/repos", params={"per_page": 100, "sort": "updated"})
    print(json.dumps([{"name": r["name"], "private": r["private"], "html_url": r["html_url"]}
                      for r in out], indent=2))


def cmd_create_repo(args):
    name = args[0]
    out = api("POST", "/user/repos", body={
        "name": name,
        "description": "Official Sylvect IT Services brand kit — logos, colors, typography, templates and usage guidelines.",
        "private": False,
        "auto_init": False,
        "has_issues": False,
        "has_wiki": False,
        "has_projects": False,
    })
    print(json.dumps({"name": out["name"], "html_url": out["html_url"], "default_branch": out["default_branch"]}, indent=2))


def cmd_put_file(args):
    """put-file <repo> <path-in-repo> <local-file> [commit-message]"""
    repo, repo_path, local_file = args[0], args[1], args[2]
    message = args[3] if len(args) > 3 else f"Add {repo_path}"
    with open(local_file, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    body = {"message": message, "content": content}
    # update needs the sha of the existing file
    try:
        existing = api("GET", f"/repos/{OWNER}/{repo}/contents/{repo_path}")
        body["sha"] = existing["sha"]
    except SystemExit:
        pass
    out = api("PUT", f"/repos/{OWNER}/{repo}/contents/{repo_path}", body=body)
    print(json.dumps({"path": out["content"]["path"], "sha": out["content"]["sha"][:8],
                      "commit": out["commit"]["sha"][:8]}, indent=2))


COMMANDS = {"repos": cmd_repos, "create-repo": cmd_create_repo, "put-file": cmd_put_file}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in COMMANDS:
        print("usage: gh.py repos | create-repo <name> | put-file <repo> <path> <file> [msg]")
        sys.exit(1)
    COMMANDS[cmd](sys.argv[2:])
