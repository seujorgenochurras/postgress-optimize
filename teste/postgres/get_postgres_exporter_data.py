import datetime
import json
import time
import subprocess
from typing import Any

json_path = "teste/data.json"

data: list[dict[str, Any]] = []


def get_docker_stats():
    result = subprocess.run(
        [
            "docker",
            "stats",
            "postgress-optimize-db-1",
            "--no-stream",
            "--format",
            "{{json .}}",
        ],
        stdout=subprocess.PIPE,
    )

    stats = []
    for line in result.stdout.decode().splitlines():
        stats.append(json.loads(line))
    stats[0]["timestamp"] = datetime.datetime.now().isoformat()
    return stats


while True:
    stats = get_docker_stats()
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.extend(stats)
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)
    time.sleep(5)
