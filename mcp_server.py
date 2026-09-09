import sys
import json
from client import BSPNode

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "build_and_order":
        bsp = BSPNode()
        bsp.build_tree(params.get("segments", []))
        return {"order": bsp.depth_order(params.get("eye", (0, 0)))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
