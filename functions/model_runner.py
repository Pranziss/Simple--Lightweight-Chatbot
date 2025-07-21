import subprocess

def run_model(prompt):
    result = subprocess.run(
        ["ollama", "run", "phi", prompt],#change model "phi"(to the nmodel u want)
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.stderr:
        print("[MODEL STDERR]", result.stderr)

    raw_output = result.stdout.strip()
    lines = raw_output.split("\n")
    response_lines = [line for line in lines if not line.strip().startswith(">>>")]
    reply = "\n".join(response_lines).strip()
    return reply or "I'm here, but something glitched—try asking me again?"

def summarize_convo(summary_prompt):
    result = subprocess.run(
        ["ollama", "run", "nova", summary_prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.stderr:
        print("[SUMMARY STDERR]", result.stderr)

    return result.stdout.strip()