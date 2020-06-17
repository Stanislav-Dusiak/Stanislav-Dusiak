"""https://stepik.org/lesson/236236/step/15?unit=208641"""

"""Neural network for regression problems"""


import torch
import matplotlib.pyplot as plt
from tqdm import tqdm


def target_function(x):
    return 2 ** x * torch.sin(2 ** -x)


class RegressionNet(torch.nn.Module):
    def __init__(self, n_hidden_neurons, m_hidden_neurons, z_hidden_neurons):
        super().__init__()
        self.fc1 = torch.nn.Linear(1, n_hidden_neurons)
        self.bn1 = torch.nn.BatchNorm1d(num_features=n_hidden_neurons)
        self.act1 = torch.nn.Tanh()
        self.fc2 = torch.nn.Linear(n_hidden_neurons, m_hidden_neurons)
        self.bn2 = torch.nn.BatchNorm1d(num_features=m_hidden_neurons)
        self.act2 = torch.nn.Tanh()
        self.fc3 = torch.nn.Linear(m_hidden_neurons, z_hidden_neurons)
        self.bn3 = torch.nn.BatchNorm1d(num_features=z_hidden_neurons)
        self.act3 = torch.nn.Tanh()
        self.fc4 = torch.nn.Linear(z_hidden_neurons, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)
        x = self.act1(x)
        x = self.fc2(x)
        x = self.bn2(x)
        x = self.act2(x)
        x = self.fc3(x)
        x = self.bn3(x)
        x = self.act3(x)
        x = self.fc4(x)
        return x


net = RegressionNet(20, 60, 100)

# ------Dataset preparation start--------:
x_train = torch.linspace(-10, 5, 100)
y_train = target_function(x_train)
noise = torch.randn(y_train.shape) / 20.
y_train = y_train + noise
x_train.unsqueeze_(1)
y_train.unsqueeze_(1)

x_validation = torch.linspace(-10, 5, 100)
y_validation = target_function(x_validation)
x_validation.unsqueeze_(1)
y_validation.unsqueeze_(1)
# ------Dataset preparation end--------:


optimizer = torch.optim.Adam(net.parameters(), lr=0.04)


def loss(pred, target):
    squares = (pred - target) ** 2
    return squares.mean()


for epoch_index in tqdm(range(2500), desc='training'):
    optimizer.zero_grad()

    y_pred = net.forward(x_train)
    loss_value = loss(y_pred, y_train)
    loss_value.backward()
    optimizer.step()


def metric(pred, target):
    return (pred - target).abs().mean()


print(metric(net.forward(x_validation), y_validation).item())


def predict(z, x, y):
    y_pred1 = z.forward(x)

    plt.plot(x.numpy(), y.numpy(), 'o', label='Groud truth')
    plt.plot(x.numpy(), y_pred1.data.numpy(), 'o', c='r', label='Prediction')
    plt.legend(loc='upper left')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()


predict(net, x_validation, y_validation)

