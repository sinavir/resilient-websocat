# Resilient websocat

Simple Go program that plugs a websocket endpoint to `stdin`/`stdout`. It tries to ba as resilient as possible to network deconnexions.

## Building

```
nix-shell
go build
```
