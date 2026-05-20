#!/usr/bin/env python3
"""Tiny helper used in Scenario 4 to seed an interesting log file if you need one."""
import random, datetime, sys

USERS = [f"u_{i:03d}" for i in range(50)]
ENDPOINTS = ["/api/orders", "/api/users", "/api/checkout", "/api/inventory", "/api/auth/login"]
STATUS = [200] * 90 + [400] * 4 + [401] * 2 + [500] * 3 + [502] * 1
COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 500

t = datetime.datetime(2026, 5, 19, 9, 0, 0)
for _ in range(COUNT):
    t += datetime.timedelta(seconds=random.randint(1, 6))
    user = random.choice(USERS)
    ep = random.choice(ENDPOINTS)
    s = random.choice(STATUS)
    print(f'{t.isoformat()} user={user} endpoint={ep} status={s}')
