# Resilient websocat

Simple Python program that plugs a websocket endpoint to `stdin`/`stdout`. It tries to be as resilient as possible to network deconnexions.

## Building

```
nix-build
```

## Running

```
./result/bin/rwebsocat [ws url]
```

