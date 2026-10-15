import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StatusDocumentTest(unittest.TestCase):
    def setUp(self):
        self.status = json.loads((ROOT / "status.json").read_text())

    def test_required_fields(self):
        for key in (
            "status",
            "cpu_percent",
            "memory_percent",
            "disk_percent",
            "uptime_seconds",
            "agent_count",
            "service_count",
            "platform",
            "updated_at",
        ):
            self.assertIn(key, self.status)

    def test_status_is_a_known_value(self):
        self.assertIn(
            self.status["status"],
            {"healthy", "degraded", "offline", "unknown"},
        )

    def test_counts_are_numbers(self):
        self.assertIsInstance(self.status["agent_count"], (int, float))
        self.assertIsInstance(self.status["service_count"], (int, float))


if __name__ == "__main__":
    unittest.main()
