"""Local-only symbolic-equivalence grading server.

Runs on localhost only, never deployed, no auth (single-user local tool).
Checks whether a student's symbolic answer is mathematically equivalent to the
reference expression. Primary method is numeric sampling at random points
(robust to expressions that are equal but shaped very differently, e.g. a
sigmoid-derivative written via exp(.) vs. via cosh(.) — plain sympy.simplify()
on their difference can fail to find zero for such cases even though they ARE
equal everywhere). Symbolic simplify is used only as a secondary, informational
check for the reported "difference" string, not as the pass/fail decision.

Run: .venv/bin/python scripts/grading/sympy_server.py
"""
import random
from flask import Flask, request, jsonify
import sympy

app = Flask(__name__)

ALLOWED_ORIGIN = "http://localhost:4321"


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGIN
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/check-symbolic", methods=["POST", "OPTIONS"])
def check_symbolic():
    if request.method == "OPTIONS":
        return "", 204

    body = request.get_json(force=True, silent=True) or {}
    expr_str = body.get("expr", "")
    expected_str = body.get("expected", "")
    variable_names = body.get("variables", [])

    if not expr_str.strip():
        return jsonify({"equivalent": False, "error": "empty expression"}), 400

    try:
        symbols = {name: sympy.Symbol(name) for name in variable_names}
        local_dict = {**symbols, "exp": sympy.exp, "log": sympy.log, "sin": sympy.sin,
                      "cos": sympy.cos, "tanh": sympy.tanh, "cosh": sympy.cosh, "sinh": sympy.sinh,
                      "sqrt": sympy.sqrt, "pi": sympy.pi}
        user_expr = sympy.sympify(expr_str, locals=local_dict)
        expected_expr = sympy.sympify(expected_str, locals=local_dict)
    except (sympy.SympifyError, TypeError, ValueError) as e:
        return jsonify({"equivalent": False, "error": f"could not parse expression: {e}"}), 400

    free_syms = sorted((user_expr.free_symbols | expected_expr.free_symbols), key=str)
    if not free_syms:
        diff = sympy.simplify(user_expr - expected_expr)
        return jsonify({"equivalent": bool(diff == 0), "difference": str(diff)})

    rng = random.Random(1234)  # deterministic across requests, not security-sensitive
    n_ok, n_tested = 0, 0
    for _ in range(25):
        sample = {s: sympy.Float(rng.uniform(-3, 3)) for s in free_syms}
        try:
            uv = complex(user_expr.evalf(subs=sample))
            ev = complex(expected_expr.evalf(subs=sample))
        except (TypeError, ValueError):
            continue  # domain error (e.g. log of negative) at this sample point — skip it
        n_tested += 1
        if abs(uv - ev) < 1e-6 * max(1.0, abs(ev)):
            n_ok += 1

    if n_tested < 5:
        # Too many domain errors to trust numeric sampling — fall back to symbolic simplify.
        diff = sympy.simplify(user_expr - expected_expr)
        return jsonify({"equivalent": bool(diff == 0), "difference": str(diff)})

    equivalent = n_ok == n_tested
    diff_report = sympy.simplify(user_expr - expected_expr) if not equivalent else 0
    return jsonify({"equivalent": equivalent, "difference": str(diff_report), "samplesAgreeing": f"{n_ok}/{n_tested}"})


if __name__ == "__main__":
    print("Symbolic grading server on http://localhost:5055 (local only, Ctrl+C to stop)")
    app.run(host="127.0.0.1", port=5055, debug=False)
