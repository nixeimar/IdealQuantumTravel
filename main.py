from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create the same quantum circuit without measurement
qc = QuantumCircuit(3)
qc.x(2)
qc.h(0)
qc.h(1)
qc.cx(0, 1)
qc.x(1)
qc.ccx(0, 1, 2)
qc.x(1)

# Display the circuit
#print("\nQuantum Circuit:")
#qc.draw("mpl")  # Use 'mpl' for a matplotlib figure (pretty and color-coded)

# Show the circuit drawing
#plt.figure(figsize=(8, 2))
#qc.draw("mpl", style="iqp")
#plt.title("Quantum Circuit Diagram")
#plt.show()

# Get the statevector
sv = Statevector.from_instruction(qc)
probs = sv.probabilities_dict()

# Flip keys to match measurement output style (little endian)
#formatted_probs = {format(int(k, 2), "03b")[::-1]: v for k, v in probs.items()}

# Plot
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#plot_histogram(formatted_probs)
plot_histogram(probs)
plt.title("Statevector Simulation: Timeline Consistency (q₂ q₁ q₀)")
plt.xlabel("Measurement outcomes (little endian)")
plt.ylabel("Probability")
plt.show()
