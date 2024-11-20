import qiskit
import matplotlib.pyplot as plt


def add(a0, a1, b0, b1, show=False):
    qc = qiskit.QuantumCircuit(9, 3)

    if a0:
        qc.x(0)
    if a1:
        qc.x(1)
    if b0:
        qc.x(2)
    if b1:
        qc.x(3)

    qc.x(4)

    qc.barrier()

    qc.ccx(0, 2, 5)
    qc.ccx(0, 4, 6)
    qc.ccx(2, 4, 6)

    qc.barrier()

    qc.ccx(1, 3, 8)
    qc.ccx(1, 4, 7)
    qc.ccx(3, 4, 7)

    qc.barrier()

    qc.ccx(5, 7, 8)
    qc.ccx(4, 5, 7)

    qc.barrier()

    qc.measure([6, 7, 8], [0, 1, 2])

    if show and (not a0 and not a1 and not b0 and not b1):
        qc.draw(output="mpl")
        plt.show()

    return qc


backend = qiskit.Aer.get_backend("qasm_simulator")
for i in range(2):
    for j in range(2):
        for k in range(2):
            for m in range(2):
                num1, num2 = j * 2 + i, m * 2 + k
                print(f"{j}{i} + {m}{k} = ", end="")
                sum = list(
                    qiskit.execute(add(i, j, k, m, True), backend)
                    .result()
                    .get_counts()
                    .keys()
                )[0]
                print(sum, "!" if int(sum, 2) != num1 + num2 else "")
