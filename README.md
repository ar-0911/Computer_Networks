# Computer Networks

Python implementations of core networking protocols and algorithms, written for the Computer Networks lab at VIT. Each file is a standalone, interactive script.

## Error detection and correction

| File | What it does |
|---|---|
| `parity.py` | Even/odd parity check |
| `checksum.py`, `checksum2.py` | Internet-style ones' complement checksum with carry wraparound |
| `crc.py`, `crc2.py` | Cyclic redundancy check via modulo-2 division |
| `hamming.py`, `hammingprac.py` | Hamming code: redundant-bit placement, parity calculation and single-bit error location |

## Flow control (data link layer)

| File | What it does |
|---|---|
| `stopWait.py`, `stopWaitProtocol.py` | Stop-and-wait ARQ with simulated loss and retransmission |
| `goBackN.py`, `Sliding_Window_GoN.py` | Go-Back-N sliding window |
| `selective_repeat.py`, `Sliding_Window_SelectiveRep.py` | Selective Repeat sliding window |

## Routing (network layer)

| File | What it does |
|---|---|
| `djikstras.py`, `LSR.py` | Link-state routing with Dijkstra's shortest paths and path reconstruction |
| `bellman.py`, `distanceVector.py` | Distance-vector routing with Bellman-Ford, hop counts and negative-cycle detection |

## Sockets (transport layer)

| File | What it does |
|---|---|
| `server.py`, `client.py` | TCP chat over Python sockets; run `server.py`, then `client.py` in another terminal |

## Run

```bash
python3 crc.py
```

No dependencies beyond the Python 3 standard library.
