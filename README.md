# Quantum Statevector Simulation for simulating temporal consistency in the presence of retrocausality and coexisting multiverse configurations (Qiskit)

This is the ideal simulation in a classical machine of a minimal quantum circuit model for simulating temporal consistency in the presence of retrocausality and coexisting multiverse configurations. This project uses Qiskit's statevector simulation to visualize the final quantum state of a 3-qubit circuit. No measurements are used, so the circuit's output is interpreted as a probability distribution over quantum states.

---

## Features

-  3-qubit quantum circuit
-  Statevector simulation using `Statevector.from_instruction`
-  Visualization of output state probabilities
-  Clean matplotlib histogram plot

---

## Circuit Overview

```plaintext
  q0: ──H─■────■────
           │      │
  q1: ──H──X──X───■───
                 │
  q2: ──X─────────X───
```

- Qubit 2 is initialized to `|1⟩`
- Bell pair created between `q0` and `q1`
- Toffoli (CCX) gate with `q0`, `q1` controlling `q2`

---

## Requirements

Install dependencies:

```bash
pip install qiskit matplotlib
```

---

## How to Run

Save the code as `statevector_simulation.py`, then run:

```bash
python statevector_simulation.py
```

This will:
1. Construct the quantum circuit (without measurement)
2. Simulate it using the statevector
3. Plot a histogram of the quantum state's probabilities

---

## Output Example

The output is a histogram of quantum state probabilities:

![Statevector Histogram](statevector_histogram.png)

Each state is labeled in **little endian** format (`q2 q1 q0`), consistent with Qiskit's output conventions.

---

## License

MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions and suggestions are welcome via pull requests or issues.

---

## Contact

Questions? Reach out via [GitHub Issues](https://github.com/your-username/your-repo/issues).

