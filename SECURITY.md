# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2026.x  | Yes       |
| < 2025  | No        |

## Reporting a Vulnerability

If you discover a security issue in `my-project` (e.g. unsafe deserialization
of profile files, insecure update channel, local privilege issues), please
open a private security advisory on the repository or email the maintainers
listed in the project metadata. Do not open a public issue for vulnerabilities
that could be actively exploited.

Please include:

- A description of the issue and affected file(s)
- Steps to reproduce
- Impact assessment (local only, network, etc.)

We aim to acknowledge reports within 5 business days.

## Scope Notes

This tool interacts with a running Crossout client on the same machine and
with a remote update endpoint. Reports about the game's own anti-cheat or
server infrastructure are out of scope for this repository and should be
directed to the game publisher.