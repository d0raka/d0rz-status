# d0rz-status

Public JSON for the Live System strip on [d0rz.is-a.dev](https://d0rz.is-a.dev).

This repository is a data bridge only. It does not contain the website, private server configuration, or credentials.

## status.json

`status.json` is the only payload the public site should fetch. The file in this repository is a schema bootstrap. A workstation exporter will overwrite it later.

Public raw URL:

https://raw.githubusercontent.com/d0raka/d0rz-status/main/status.json

## Schema

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

`agent_count` must stay a number. Do not add hostnames, IP addresses, ports, SSH details, Docker data, filesystem paths, tokens, or other private fields.
