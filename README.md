# d0rz-status

[![CI](https://github.com/d0raka/d0rz-status/actions/workflows/ci.yml/badge.svg)](https://github.com/d0raka/d0rz-status/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Public workstation snapshot for the Live System strip on the [d0rz](https://github.com/d0raka/d0rz) homepage.

This repository is a data bridge. It does not contain the website, private server configuration, or credentials.

## Demo

The live document the site reads:

https://raw.githubusercontent.com/d0raka/d0rz-status/main/status.json

The homepage that renders it is [d0rz.is-a.dev](https://d0rz.is-a.dev).

## Features

- One public JSON document, `status.json`
- A fixed schema: health, CPU, memory, disk, uptime, agent count, service count, platform, and timestamp
- No hostnames, addresses, ports, or tokens

## Tech stack

JSON only. There is no build step and no runtime. CI checks that `status.json` parses.

## Setup

Clone the repository. There is nothing to install.

## Usage

The site reads:

https://raw.githubusercontent.com/d0raka/d0rz-status/main/status.json

The committed file is a schema bootstrap. A workstation exporter overwrites it. Keep `agent_count` a number. Do not add private fields.

```json
{
  "status": "healthy | degraded | offline | unknown",
  "cpu_percent": 0,
  "memory_percent": 0,
  "disk_percent": 0,
  "uptime_seconds": 0,
  "agent_count": 0,
  "service_count": 0,
  "platform": "Ubuntu / ARM64",
  "amd64_emulation": true,
  "updated_at": "2026-09-21T00:51:40Z"
}
```

## License

MIT. See [LICENSE](LICENSE).
