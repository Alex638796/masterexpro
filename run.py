#!/usr/bin/env python3
"""
Supervisor script: runs app.py (Flask health-check server) and main.py
(the Pyrogram bot) as subprocesses, and forwards SIGTERM/SIGINT to both,
so a platform's restart/redeploy/health-check signal reaches the bot
process cleanly instead of only killing the parent shell.
"""

import signal
import subprocess
import sys
import time

procs = []


def start():
    procs.append(subprocess.Popen(["gunicorn", "app:app", "-b", "0.0.0.0:8000"]))
    procs.append(subprocess.Popen([sys.executable, "main.py"]))


def handle_signal(signum, frame):
    print(f"Supervisor received signal {signum}, forwarding to children...")
    for p in procs:
        if p.poll() is None:
            try:
                p.send_signal(signum)
            except Exception as e:
                print(f"Error signaling process {p.pid}: {e}")
    for p in procs:
        try:
            p.wait(timeout=15)
        except subprocess.TimeoutExpired:
            print(f"Process {p.pid} did not exit in time, killing.")
            p.kill()
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

start()

try:
    while True:
        time.sleep(2)
        for p in procs:
            ret = p.poll()
            if ret is not None:
                print(f"Process {p.pid} exited with code {ret}, shutting down supervisor.")
                for other in procs:
                    if other is not p and other.poll() is None:
                        other.terminate()
                sys.exit(ret or 1)
except KeyboardInterrupt:
    handle_signal(signal.SIGINT, None)
