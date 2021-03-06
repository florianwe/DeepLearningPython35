import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

# ---------------------
# - network.py example:
import network


net = network.Network([784, 28, 10])
net.SGD(training_data, 20, 10, 3.0, test_data=test_data)
input("any key to continue")