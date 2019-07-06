import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim
import os


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.lin1 = nn.Linear(10, 10)
        self.lin2 = nn.Linear(10, 10)
        self.lin3 = nn.Linear(10, 10)

    def forward(self, x):
        x = F.relu(self.lin1(x))
        x = F.hardtanh(self.lin2(x))
        x = self.lin3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num = 1
        for i in size:
            num *= i
        return num


netz = MyNet()
netz = netz.cuda()
file = 'netz.pt'

for i in range(100):

    if os.path.isfile(file):
        netz = torch.load(file)
        netz = netz.cuda()

    x = [0,1,0,1,0,1,0,1,0,1]
    input = Variable(torch.Tensor([x for _ in range(10)]))
    input = input.cuda()
    out = netz(input)

    x = [1,0,1,0,1,0,1,0,1,0]
    target = Variable(torch.Tensor([x for _ in range(10)]))
    target = target.cuda()
    crit = nn.MSELoss()
    loss = crit(out, target)
    print(loss)
    netz.zero_grad()
    loss.backward()
    optimizer = optim.SGD(netz.parameters(), lr=0.1)
    optimizer.step()

    torch.save(netz, file)