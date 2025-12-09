import math
import sys
from itertools import combinations
from typing import Iterable, cast

JunctionBox = tuple[int, int, int]
Circuit = set[JunctionBox]


def euclidean(b1: JunctionBox, b2: JunctionBox) -> float:
    return math.sqrt(sum((i1 - i2) ** 2 for i1, i2 in zip(b1, b2)))


def closest_pairs(
    boxes: list[JunctionBox],
) -> Iterable[tuple[JunctionBox, JunctionBox]]:
    sorted_pairs = sorted([(euclidean(a, b), a, b) for a, b in combinations(boxes, 2)])
    seen: set[tuple[JunctionBox, JunctionBox]] = set()
    for _dist, a, b in sorted_pairs:
        pair = (a, b) if a < b else (b, a)
        if pair in seen:
            continue
        seen.add(pair)
        yield pair


def p2(boxes: list[JunctionBox]) -> int:
    box_to_circuit: dict[JunctionBox, Circuit | None] = {b: None for b in boxes}
    circuits: list[Circuit] = []
    boxes_in_circuits: set[JunctionBox] = set()
    for box, nb_box in closest_pairs(boxes):
        box_circuit, nb_circuit = box_to_circuit[box], box_to_circuit[nb_box]
        boxes_in_circuits.add(box)
        boxes_in_circuits.add(nb_box)
        if box_circuit and nb_circuit:
            if box_circuit == nb_circuit:
                pass
            else:
                for n in nb_circuit:
                    box_circuit.add(n)
                    box_to_circuit[n] = box_circuit

                circuits = [c for c in circuits if c != nb_circuit]

        elif box_circuit:
            box_circuit.add(nb_box)
            box_to_circuit[nb_box] = box_circuit
        elif nb_circuit:
            nb_circuit.add(box)
            box_to_circuit[box] = nb_circuit
        else:
            circuit = {box, nb_box}
            circuits.append(circuit)
            box_to_circuit[box] = circuit
            box_to_circuit[nb_box] = circuit

        if len(boxes_in_circuits) == len(boxes) and len(circuits) == 1:
            return box[0] * nb_box[0]

    return -1


def p1(boxes: list[JunctionBox], connections: int = 1000) -> int:
    box_to_circuit: dict[JunctionBox, Circuit | None] = {b: None for b in boxes}
    circuits: list[Circuit] = []
    connections_made = 0
    for box, nb_box in closest_pairs(boxes):
        box_circuit, nb_circuit = box_to_circuit[box], box_to_circuit[nb_box]
        if box_circuit and nb_circuit:
            if box_circuit == nb_circuit:
                pass
            else:
                for n in nb_circuit:
                    box_circuit.add(n)
                    box_to_circuit[n] = box_circuit

                circuits = [c for c in circuits if c != nb_circuit]

        elif box_circuit:
            box_circuit.add(nb_box)
            box_to_circuit[nb_box] = box_circuit
        elif nb_circuit:
            nb_circuit.add(box)
            box_to_circuit[box] = nb_circuit
        else:
            circuit = {box, nb_box}
            circuits.append(circuit)
            box_to_circuit[box] = circuit
            box_to_circuit[nb_box] = circuit

        connections_made += 1
        if connections_made >= connections:
            break

    return math.prod(list(sorted([len(c) for c in circuits], reverse=True))[:3])


def run(filename: str):
    boxes = cast(
        list[JunctionBox],
        [
            tuple(map(int, li.split(",")))
            for li in open(filename).read().strip().split("\n")
        ],
    )
    print(p1(boxes, connections=10 if filename == "test" else 1000))
    print(p2(boxes))


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
