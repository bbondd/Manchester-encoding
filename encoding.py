import numpy as np
import matplotlib.pyplot as plt


def main():
    input_signal = [int(i) for i in input()]

    m_encoded_signal = [0, 0]
    dm_encoded_signal = [0, 1]

    for i in input_signal:
        if int(i) == 0:
            m_encoded_signal += [1, 0]
            dm_encoded_signal += [not dm_encoded_signal[-1], dm_encoded_signal[-1]]

        else:
            m_encoded_signal += [0, 1]
            dm_encoded_signal += [dm_encoded_signal[-1], not dm_encoded_signal[-1]]

    x = np.linspace(-0.5, len(input_signal), len(input_signal) * 2 + 2)

    m_encoded_signal = np.array(m_encoded_signal) - 0.5
    m_encoded_signal[0:2] = 0
    dm_encoded_signal = np.array(dm_encoded_signal) - 0.5
    dm_encoded_signal[0:2] = 0

    print('manchester encoding : ', m_encoded_signal)
    print('differential manchester encoding : ', dm_encoded_signal)

    plt.subplot(211)
    plt.title('manchester encoding')
    plt.step(x, m_encoded_signal)

    plt.subplot(212)
    plt.title('differential manchester encoding')
    plt.step(x, dm_encoded_signal)

    plt.show()


main()
